"""CLI entrypoint for the Aegis-Sea 2.0 geospatial anomaly-detection research starter."""

import argparse
import json
from pathlib import Path
import numpy as np
from .geodata import build_feature_dataset
from .models import run_baselines
from .plots import make_anomaly_map
from .robustness import run_robustness


def main():
    p = argparse.ArgumentParser(description="Aegis-Sea geophysical anomaly research scaffold")
    p.add_argument("--bathymetry", required=True, help="Path to projected bathymetry GeoTIFF")
    p.add_argument("--gravity", required=True, help="Path to gravity GeoTIFF")
    p.add_argument("--output", default="data/processed", help="Output directory")
    p.add_argument("--max-cells", type=int, default=150000, help="Maximum valid cells to sample")
    p.add_argument("--test-blocks", type=int, default=1, help="Reserved for multi-block holdout")
    args = p.parse_args()

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)

    X, coords, rc, names, meta = build_feature_dataset(
        args.bathymetry, args.gravity, max_cells=args.max_cells
    )
    np.savez_compressed(out / "feature_dataset.npz", X=X, coords=coords, rc=rc, feature_names=np.array(names))
    (out / "metadata.json").write_text(json.dumps(meta, indent=2))

    scores, split = run_baselines(X, coords, out)
    run_robustness(X, split, out, bathy_path=args.bathymetry, gravity_path=args.gravity, rc=rc)
    make_anomaly_map(coords, scores, out / "anomaly_map.png")

    print(f"Completed. Valid samples: {len(X)}; features: {len(names)}")
    print(f"Outputs: {out.resolve()}")
    print("Reminder: scores indicate statistical unusualness, not geological truth.")


if __name__ == "__main__":
    main()
