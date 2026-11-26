"""Geospatial raster ingestion, alignment, and terrain/gravity feature extraction."""

import numpy as np
import rasterio
from rasterio.warp import Resampling, reproject
from scipy.ndimage import binary_erosion, gaussian_filter, generic_filter


def _read_reference(path):
    """Read the reference bathymetry raster and return array, validity mask, and CRS metadata."""
    with rasterio.open(path) as ds:
        arr = ds.read(1).astype("float32")
        profile = ds.profile.copy()
        transform = ds.transform
        crs = ds.crs
        nodata = ds.nodata
    valid = np.isfinite(arr)
    if nodata is not None:
        valid &= arr != nodata
    arr[~valid] = np.nan
    return arr, valid, profile, transform, crs


def _align_to_reference(src_path, ref_transform, ref_crs, shape):
    """Reproject a secondary raster onto the reference grid using bilinear interpolation."""
    dst = np.full(shape, np.nan, dtype="float32")
    with rasterio.open(src_path) as src:
        src_arr = src.read(1).astype("float32")
        src_valid = np.isfinite(src_arr)
        if src.nodata is not None:
            src_valid &= src_arr != src.nodata
        src_arr[~src_valid] = np.nan
        reproject(
            source=src_arr,
            destination=dst,
            src_transform=src.transform,
            src_crs=src.crs,
            src_nodata=np.nan,
            dst_transform=ref_transform,
            dst_crs=ref_crs,
            dst_nodata=np.nan,
            resampling=Resampling.bilinear,
        )
        src_meta = {
            "source": str(src_path),
            "crs": str(src.crs),
            "width": src.width,
            "height": src.height,
            "bounds": list(src.bounds),
            "resolution": [float(abs(src.transform.a)), float(abs(src.transform.e))],
            "nodata": src.nodata,
        }
    return dst, src_meta


def _roughness(arr):
    """Local standard deviation in a 3x3 window, ignoring NaNs (ponytail: O(N) Python callback; swap for vectorized window if grids exceed ~1e7 cells)."""
    def _std_valid(vals):
        v = vals[np.isfinite(vals)]
        return float(np.std(v)) if len(v) >= 3 else np.nan

    return generic_filter(arr, _std_valid, size=3, mode="nearest").astype("float32")


def _grad_magnitude(arr, dy, dx):
    """Compute finite-difference gradient magnitude; NaNs propagate naturally to boundary cells."""
    gy, gx = np.gradient(arr, dy, dx)
    return np.sqrt(gx**2 + gy**2).astype("float32")


def _extract_feature_arrays(bathy, gravity, dy, dx):
    """Compute the 5 standardized geophysical feature rasters."""
    slope = _grad_magnitude(bathy, dy, dx)
    rough = _roughness(bathy)
    grav_grad = _grad_magnitude(gravity, dy, dx)
    return [bathy, slope, rough, gravity, grav_grad]


def _smooth_raster_nan_aware(arr, valid_mask, sigma_px):
    """Normalized Gaussian smoothing in raster space preserving NaN boundaries."""
    weights = valid_mask.astype("float32")
    num = gaussian_filter(np.where(valid_mask, arr, 0.0), sigma=sigma_px, mode="nearest")
    den = gaussian_filter(weights, sigma=sigma_px, mode="nearest")
    out = np.where(valid_mask & (den > 1e-6), num / np.maximum(den, 1e-6), np.nan)
    return out.astype("float32")


def build_feature_dataset(bathy_path, gravity_path, max_cells=150000, seed=42):
    """Align bathymetry and gravity on a projected grid and extract 5 geophysical features."""
    bathy, bvalid, profile, transform, crs = _read_reference(bathy_path)
    if crs is None or not crs.is_projected:
        raise ValueError(
            "Bathymetry reference raster must use a projected CRS with linear units. "
            "Reproject/crop the source rasters to a suitable local projected CRS first."
        )

    gravity, gmeta = _align_to_reference(gravity_path, transform, crs, bathy.shape)
    gvalid = np.isfinite(gravity)
    # Erode 1-px border around NaNs so finite-difference derivatives never see artificial cliffs.
    stencil = np.ones((3, 3), dtype=bool)
    valid = binary_erosion(bvalid, structure=stencil) & binary_erosion(gvalid, structure=stencil)

    dx = abs(float(transform.a))
    dy = abs(float(transform.e))
    if dx <= 0 or dy <= 0:
        raise ValueError("Invalid raster pixel dimensions.")

    arrays = _extract_feature_arrays(bathy, gravity, dy, dx)
    names = [
        "bathymetry",
        "bathymetry_slope",
        "bathymetry_roughness",
        "gravity",
        "gravity_gradient_magnitude",
    ]

    rows, cols = np.where(valid)
    if len(rows) == 0:
        raise ValueError("No overlapping valid bathymetry/gravity cells.")
    if len(rows) > max_cells:
        rng = np.random.default_rng(seed)
        take = rng.choice(len(rows), size=max_cells, replace=False)
        rows, cols = rows[take], cols[take]

    X = np.column_stack([a[rows, cols] for a in arrays]).astype("float32")
    finite = np.isfinite(X).all(axis=1)
    rows, cols, X = rows[finite], cols[finite], X[finite]
    if len(X) == 0:
        raise ValueError("No finite feature rows remaining after derivative edge filtering.")

    xs, ys = rasterio.transform.xy(transform, rows, cols, offset="center")
    coords = np.column_stack([np.asarray(xs), np.asarray(ys)]).astype("float64")
    rc = np.column_stack([rows, cols]).astype("int32")

    metadata = {
        "bathymetry": {
            "path": str(bathy_path),
            "crs": str(crs),
            "width": profile["width"],
            "height": profile["height"],
            "transform": list(transform),
            "resolution_map_units": [dx, dy],
            "bounds": list(rasterio.transform.array_bounds(profile["height"], profile["width"], transform)),
        },
        "gravity": gmeta,
        "alignment": "gravity reprojected to bathymetry grid using bilinear interpolation",
        "feature_names": names,
        "valid_overlap_cells_before_sampling": int(valid.sum()),
        "sampled_cells_after_filtering": int(len(X)),
        "random_seed": seed,
        "warning": "Target grid does not increase native information content of source data.",
    }
    return X, coords, rc, names, metadata


def extract_resolution_degraded_features(bathy_path, gravity_path, rc, sigma_px):
    """Apply raster-space Gaussian smoothing (sigma_px) to bathymetry before recomputing terrain derivatives."""
    bathy, bvalid, _, transform, crs = _read_reference(bathy_path)
    gravity, _ = _align_to_reference(gravity_path, transform, crs, bathy.shape)
    dx, dy = abs(float(transform.a)), abs(float(transform.e))

    bathy_deg = _smooth_raster_nan_aware(bathy, bvalid, sigma_px)
    arrays = _extract_feature_arrays(bathy_deg, gravity, dy, dx)
    rows, cols = rc[:, 0], rc[:, 1]
    return np.column_stack([a[rows, cols] for a in arrays]).astype("float32")
