"""Gate 1 helper: convert SRTM15+ (.nc) bathymetry and Scripps (.xyz) gravity to UTM GeoTIFFs."""

import argparse
import hashlib
from pathlib import Path
import numpy as np
import rasterio
from rasterio.transform import from_bounds
from rasterio.warp import Resampling, calculate_default_transform, reproject
from scipy.io import netcdf_file

REGIONS = {
    "ans": {
        "name": "Afanasy Nikitin Seamount (Central Indian Basin)",
        "bounds_4326": (81.5, -4.5, 84.5, -1.5),
        "target_crs": "EPSG:32744",  # WGS 84 / UTM zone 44S
    },
    "ner": {
        "name": "Ninety East Ridge segment (Eastern Indian Ocean)",
        "bounds_4326": (87.5, -11.5, 90.5, -8.5),
        "target_crs": "EPSG:32745",  # WGS 84 / UTM zone 45S
    },
}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_nc_subset(nc_path, bounds_4326):
    lon_min, lat_min, lon_max, lat_max = bounds_4326
    with netcdf_file(nc_path, "r", mmap=False) as ds:
        lat_name = "lat" if "lat" in ds.variables else "latitude"
        lon_name = "lon" if "lon" in ds.variables else "longitude"
        var_name = next(k for k in ds.variables if k not in (lat_name, lon_name))
        lats = np.asarray(ds.variables[lat_name].data, dtype="float64")
        lons = np.asarray(ds.variables[lon_name].data, dtype="float64")
        var = ds.variables[var_name]
        data = np.asarray(var.data, dtype="float32")
        fill = getattr(var, "_FillValue", None)
        if fill is not None:
            data = np.where(data == float(fill), np.nan, data)

    lat_idx = np.where((lats >= lat_min) & (lats <= lat_max))[0]
    lon_idx = np.where((lons >= lon_min) & (lons <= lon_max))[0]
    sub = data[np.ix_(lat_idx, lon_idx)].astype("float32")
    sub_lats, sub_lons = lats[lat_idx], lons[lon_idx]
    return sub, sub_lats, sub_lons, var_name


def _load_xyz_grid(xyz_path):
    d = np.loadtxt(xyz_path, dtype="float64")
    lons = np.unique(d[:, 0])
    lats = np.unique(d[:, 1])
    if len(lons) * len(lats) != len(d):
        raise ValueError(f"Expected complete regular grid in {xyz_path}, got {len(d)} != {len(lons)}x{len(lats)}")
    # Sort descending lat, ascending lon for north-up raster
    order = np.lexsort((d[:, 0], -d[:, 1]))
    grid = d[order, 2].reshape(len(lats), len(lons)).astype("float32")
    return grid, lats[::-1], lons, "free_air_gravity_mGal"


def process_to_utm(src_path, dst_path, bounds_4326, target_crs):
    """Load .nc or .xyz, orient north-up in EPSG:4326, reproject to target_crs GeoTIFF."""
    if src_path.suffix.lower() == ".nc":
        sub, sub_lats, sub_lons, var_name = _load_nc_subset(src_path, bounds_4326)
        if sub_lats[0] < sub_lats[-1]:
            sub = sub[::-1, :]
            sub_lats = sub_lats[::-1]
    elif src_path.suffix.lower() == ".xyz":
        sub, sub_lats, sub_lons, var_name = _load_xyz_grid(src_path)
    else:
        raise ValueError(f"Unsupported input format: {src_path.suffix}")

    dlat = abs(float(np.median(np.diff(sub_lats))))
    dlon = abs(float(np.median(np.diff(sub_lons))))
    src_transform = from_bounds(
        float(sub_lons.min()) - dlon / 2.0,
        float(sub_lats.min()) - dlat / 2.0,
        float(sub_lons.max()) + dlon / 2.0,
        float(sub_lats.max()) + dlat / 2.0,
        sub.shape[1],
        sub.shape[0],
    )

    h, w = sub.shape
    b = rasterio.transform.array_bounds(h, w, src_transform)
    dst_transform, dst_w, dst_h = calculate_default_transform("EPSG:4326", target_crs, w, h, *b)
    dst_arr = np.full((dst_h, dst_w), np.nan, dtype="float32")

    reproject(
        source=sub,
        destination=dst_arr,
        src_transform=src_transform,
        src_crs="EPSG:4326",
        src_nodata=np.nan,
        dst_transform=dst_transform,
        dst_crs=target_crs,
        dst_nodata=np.nan,
        resampling=Resampling.bilinear,
    )

    dst_path.parent.mkdir(parents=True, exist_ok=True)
    with rasterio.open(
        dst_path,
        "w",
        driver="GTiff",
        height=dst_h,
        width=dst_w,
        count=1,
        dtype="float32",
        crs=target_crs,
        transform=dst_transform,
        nodata=np.nan,
        compress="deflate",
    ) as dst:
        dst.write(dst_arr, 1)

    valid_pct = 100.0 * float(np.isfinite(dst_arr).sum()) / float(dst_arr.size)
    return {
        "source": str(src_path),
        "variable": var_name,
        "sha256_source": sha256_file(src_path),
        "native_crs": "EPSG:4326",
        "native_resolution_deg": [round(dlon, 6), round(dlat, 6)],
        "target_crs": target_crs,
        "target_resolution_m": [round(abs(dst_transform.a), 2), round(abs(dst_transform.e), 2)],
        "shape": [dst_h, dst_w],
        "valid_pct": round(valid_pct, 2),
        "min": round(float(np.nanmin(dst_arr)), 2),
        "max": round(float(np.nanmax(dst_arr)), 2),
    }


def main():
    p = argparse.ArgumentParser(description="Prepare Indian Ocean GeoTIFFs (ANS & NER)")
    p.add_argument("--region", choices=sorted(REGIONS), required=True)
    p.add_argument("--bathymetry-in", required=True)
    p.add_argument("--gravity-in", required=True)
    p.add_argument("--out-dir", default=None)
    args = p.parse_args()

    cfg = REGIONS[args.region]
    out = Path(args.out_dir or f"data/raw/{args.region}")
    b_info = process_to_utm(Path(args.bathymetry_in), out / "bathymetry.tif", cfg["bounds_4326"], cfg["target_crs"])
    g_info = process_to_utm(Path(args.gravity_in), out / "gravity.tif", cfg["bounds_4326"], cfg["target_crs"])
    print(f"Region: {cfg['name']}")
    print("Bathymetry:", b_info)
    print("Gravity:", g_info)


if __name__ == "__main__":
    main()
