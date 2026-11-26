"""Exploratory anomaly score visualization for held-out spatial blocks."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def make_anomaly_map(coords, scores, output_path):
    """Plot PCA reconstruction anomaly scores for held-out points only."""
    vals = scores[:, 1]
    good = np.isfinite(vals)
    if good.sum() == 0:
        return
    fig, ax = plt.subplots(figsize=(8, 6))
    sc = ax.scatter(coords[good, 0], coords[good, 1], c=vals[good], s=5, cmap="magma", linewidths=0)
    ax.set_xlabel("Projected easting (map units)")
    ax.set_ylabel("Projected northing (map units)")
    ax.set_title("PCA reconstruction anomaly score — held-out region")
    fig.colorbar(sc, ax=ax, label="Reconstruction error (standardized feature space)")
    fig.tight_layout()
    fig.savefig(output_path, dpi=220)
    plt.close(fig)

