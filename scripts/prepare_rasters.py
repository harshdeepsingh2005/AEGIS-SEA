"""Gate 1 helper: crop/reproject bathymetry & gravity rasters to Lō‘ihi UTM 5N and report provenance."""

import argparse
import hashlib
from pathlib import Path
import numpy as np
import rasterio
from rasterio.warp import Resampling, calculate_default_transform, reproject
from rasterio.windows import from_bounds

# Default regional bounding box around Lō‘ihi Seamount (Kamaʻehuakanaloa) in EPSG:4326
DEFAULT_BOUNDS_4326 = (-155.60, 18.65, -154.95, 19.20)
TARGET_CRS = "EPSG:32605"  # WGS 84 / UTM zone 5N


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _process_raster(src_path, dst_path, bounds_4326=DEFAULT_BOUNDS_4326):
    with rasterio.open(src_path) as src:
        native_crs = str(src.crs)
        native_res = (float(abs(src.transform.a)), float(abs(src.transform.e)))
        nodata = src.nodata

        # If source is geographic, crop to study bounds first if possible
        if src.crs and src.crs.is_geographic:
            win = from_bounds(*bounds_4326, transform=src.transform).round_offsets().round_lengths()
            src_arr = src.read(1, window=win).astype("float32")
            src_transform = src.window_transform(win)
            h, w = src_arr.shape
            b = rasterio.transform.array_bounds(h, w, src_transform)
        else:
            src_arr = src.read(1).astype("float32")
            src_transform = src.transform
            h, w = src_arr.shape
            b = src.bounds

        valid = np.isfinite(src_arr)
        if nodata is not None:
            valid &= src_arr != nodata
        src_arr[~valid] = np.nan

        dst_transform, dst_w, dst_h = calculate_default_transform(
            src.crs, TARGET_CRS, w, h, *b
        )
        dst_arr = np.full((dst_h, dst_w), np.nan, dtype="float32")
        reproject(
            source=src_arr,
            destination=dst_arr,
            src_transform=src_transform,
            src_crs=src.crs,
            src_nodata=np.nan,
            dst_transform=dst_transform,
            dst_crs=TARGET_CRS,
            dst_nodata=np.nan,
            resampling=Resampling.bilinear,
        )

        profile = src.profile.copy()
        profile.update(
            driver="GTiff",
            crs=TARGET_CRS,
            transform=dst_transform,
            width=dst_w,
            height=dst_h,
            dtype="float32",
            nodata=np.nan,
            compress="deflate",
        )
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        with rasterio.open(dst_path, "w", **profile) as dst:
            dst.write(dst_arr, 1)

        valid_pct = 100.0 * float(np.isfinite(dst_arr).sum()) / float(dst_arr.size)
        return {
            "source": str(src_path),
            "sha256_source": _sha256(src_path),
            "native_crs": native_crs,
            "native_resolution": native_res,
            "target_crs": TARGET_CRS,
            "target_resolution_m": (float(abs(dst_transform.a)), float(abs(dst_transform.e))),
            "shape": (dst_h, dst_w),
            "valid_pct": round(valid_pct, 2),
        }


def main():
    p = argparse.ArgumentParser(description="Prepare Lō‘ihi GeoTIFFs in EPSG:32605")
    p.add_argument("--bathymetry-in", required=True)
    p.add_argument("--gravity-in", required=True)
    p.add_argument("--out-dir", default="data/raw")
    args = p.parse_args()

    out = Path(args.out_dir)
    b_info = _process_raster(Path(args.bathymetry_in), out / "bathymetry.tif")
    g_info = _process_raster(Path(args.gravity_in), out / "gravity.tif")
    print("Bathymetry:", b_info)
    print("Gravity:", g_info)


if __name__ == "__main__":
    main()

