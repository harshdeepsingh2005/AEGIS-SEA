"""Score-stability stress tests under noise, modality dropout, and bounded PCA perturbations."""

from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import spearmanr


def _rank_corr(a, b):
    """Spearman rank correlation with constant-array guard."""
    if np.std(a) == 0 or np.std(b) == 0:
        return np.nan
    return float(spearmanr(a, b).statistic)


def _top_overlap(a, b, fraction=0.05):
    """Fraction of top-k highest-scoring cells shared between clean and perturbed scores."""
    k = max(1, int(np.ceil(len(a) * fraction)))
    ia = set(np.argpartition(a, -k)[-k:])
    ib = set(np.argpartition(b, -k)[-k:])
    return len(ia & ib) / k


def run_robustness(X, split, out_dir, seed=7):
    """Evaluate PCA anomaly-score stability on held-out spatial cells and write robustness.csv."""
    out_dir = Path(out_dir)
    test = split["test"]
    scaler = split["scaler"]
    pca = split["pca"]

    Xte = scaler.transform(X[test])
    base_recon = pca.inverse_transform(pca.transform(Xte))
    base_score = np.mean((Xte - base_recon) ** 2, axis=1)

    rows = []
    rng = np.random.default_rng(seed)

    def _record(name, altered, status="OK"):
        recon = pca.inverse_transform(pca.transform(altered))
        score = np.mean((altered - recon) ** 2, axis=1)
        rows.append({
            "condition": name,
            "spearman_score_rank_vs_clean": _rank_corr(base_score, score),
            "mean_absolute_score_change": float(np.mean(np.abs(score - base_score))),
            "top_5pct_overlap": float(_top_overlap(base_score, score, 0.05)),
            "status": status,
        })

    for sigma in (0.05, 0.10, 0.20):
        _record(f"standardized_gaussian_noise_{sigma}", Xte + rng.normal(0, sigma, Xte.shape))

    for cols, label in [([0, 1, 2], "bathymetry_features_missing"), ([3, 4], "gravity_features_missing")]:
        altered = Xte.copy()
        altered[:, cols] = 0.0  # standardized training mean
        _record(label, altered)

    # Resolution degradation must be applied in raster space before feature extraction.
    rows.append({
        "condition": "resolution_degradation",
        "spearman_score_rank_vs_clean": np.nan,
        "mean_absolute_score_change": np.nan,
        "top_5pct_overlap": np.nan,
        "status": "NOT_RUN: implement raster-space smoothing/coarsening before sampling",
    })

    # Model-directed PCA residual step under an L-infinity bound in standardized feature space.
    residual = Xte - base_recon
    direction = residual / (np.max(np.abs(residual), axis=1, keepdims=True) + 1e-12)
    for eps in (0.02, 0.05, 0.10):
        _record(f"pca_residual_directed_linf_{eps}", Xte + eps * direction)

    pd.DataFrame(rows).to_csv(out_dir / "robustness.csv", index=False)
    return rows

