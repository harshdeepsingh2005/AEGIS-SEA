"""Spatial holdout and baseline anomaly detectors (Isolation Forest & PCA)."""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

MODALITIES = {
    "bathymetry": [0, 1, 2],
    "gravity": [3, 4],
    "combined": [0, 1, 2, 3, 4],
}


def spatial_holdout(coords, test_fraction=0.20):
    """Hold out the easternmost fraction of projected x-coordinates to avoid random cell leakage."""
    x = coords[:, 0]
    threshold = np.quantile(x, 1.0 - test_fraction)
    test = x >= threshold
    train = ~test
    if train.sum() < 100 or test.sum() < 30:
        raise ValueError("Spatial holdout too small; inspect extent or sample count.")
    return train, test


def _fit_pair(X, train, test, seed=42):
    """Fit StandardScaler, IsolationForest, and PCA on training blocks only and score held-out cells."""
    scaler = StandardScaler()
    Xtr = scaler.fit_transform(X[train])
    Xte = scaler.transform(X[test])

    iso = IsolationForest(n_estimators=300, contamination="auto", random_state=seed, n_jobs=-1)
    iso.fit(Xtr)
    iso_score = -iso.score_samples(Xte)

    ncomp = max(1, min(3, Xtr.shape[1] - 1))
    pca = PCA(n_components=ncomp, random_state=seed)
    pca.fit(Xtr)
    recon = pca.inverse_transform(pca.transform(Xte))
    pca_score = np.mean((Xte - recon) ** 2, axis=1)
    return iso_score, pca_score, scaler, pca


def run_baselines(X, coords, out_dir, seed=42):
    """Run single-modality and combined baselines and write baseline_scores.csv."""
    out_dir = Path(out_dir)
    train, test = spatial_holdout(coords)
    result = {"x": coords[test, 0], "y": coords[test, 1]}
    combined_scaler = combined_pca = combined_scores = None

    for label, cols in MODALITIES.items():
        iso_score, pca_score, scaler, pca = _fit_pair(X[:, cols], train, test, seed=seed)
        result[f"{label}_isolation_forest_score"] = iso_score
        result[f"{label}_pca_reconstruction_error"] = pca_score
        if label == "combined":
            combined_scaler, combined_pca = scaler, pca
            combined_scores = np.column_stack([iso_score, pca_score])

    pd.DataFrame(result).to_csv(out_dir / "baseline_scores.csv", index=False)
    split = {"train": train, "test": test, "scaler": combined_scaler, "pca": combined_pca}
    scores = np.full((len(X), 2), np.nan, dtype="float64")
    scores[test] = combined_scores
    return scores, split

