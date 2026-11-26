"""End-to-end smoke test on tiny synthetic projected GeoTIFFs (verifies pipeline mechanics only)."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path
import numpy as np
import pandas as pd
import rasterio
from rasterio.transform import from_origin


def _write_tif(path, arr, crs="EPSG:32605", res=100.0):
    transform = from_origin(250000.0, 2100000.0, res, res)
    with rasterio.open(
        path,
        "w",
        driver="GTiff",
        height=arr.shape[0],
        width=arr.shape[1],
        count=1,
        dtype="float32",
        crs=crs,
        transform=transform,
        nodata=-9999.0,
    ) as ds:
        ds.write(arr.astype("float32"), 1)


def test_pipeline_smoke():
    rng = np.random.default_rng(0)
    bathy = -3000.0 + rng.normal(0, 25.0, (24, 24)).astype("float32")
    bathy[0, 0] = -9999.0  # verify nodata masking
    gravity = 50.0 + rng.normal(0, 2.0, (24, 24)).astype("float32")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        b_path, g_path, out_dir = tmp_path / "bathy.tif", tmp_path / "grav.tif", tmp_path / "out"
        _write_tif(b_path, bathy)
        _write_tif(g_path, gravity)

        subprocess.run(
            [
                sys.executable,
                "-m",
                "src.run_pipeline",
                "--bathymetry",
                str(b_path),
                "--gravity",
                str(g_path),
                "--output",
                str(out_dir),
                "--max-cells",
                "500",
            ],
            check=True,
        )

        for fname in ("feature_dataset.npz", "metadata.json", "baseline_scores.csv", "robustness.csv", "anomaly_map.png"):
            assert (out_dir / fname).exists(), f"Missing expected output: {fname}"

        meta = json.loads((out_dir / "metadata.json").read_text())
        assert meta["sampled_cells_after_filtering"] <= 500
        rob = pd.read_csv(out_dir / "robustness.csv")
        assert "NOT_RUN" in rob.loc[rob["condition"] == "resolution_degradation", "status"].values[0]


if __name__ == "__main__":
    test_pipeline_smoke()
    print("Smoke test PASSED.")

