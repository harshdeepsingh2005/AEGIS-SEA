"""E12 Defense Comparison (H5): Per-modality score aggregation vs. combined PCA under dropout and cross-region transfer."""

import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from .models import MODALITIES, spatial_holdout
from .robustness import _rank_corr, _top_overlap


def _fit_pca(X_tr, seed=42):
    scaler = StandardScaler()
    Z_tr = scaler.fit_transform(X_tr)
    ncomp = max(1, min(3, Z_tr.shape[1] - 1))
    pca = PCA(n_components=ncomp, random_state=seed)
    pca.fit(Z_tr)
    return scaler, pca


def _pca_err(scaler, pca, X_te, z_override=None):
    Z = scaler.transform(X_te) if z_override is None else z_override
    recon = pca.inverse_transform(pca.transform(Z))
    return np.mean((Z - recon) ** 2, axis=1)


def _fit_late_fusion(X_tr):
    """Defense D: train independent per-modality PCA detectors and normalize each score by its training mean."""
    b_sc, b_pca = _fit_pca(X_tr[:, MODALITIES["bathymetry"]])
    g_sc, g_pca = _fit_pca(X_tr[:, MODALITIES["gravity"]])
    b_scale = float(np.mean(_pca_err(b_sc, b_pca, X_tr[:, MODALITIES["bathymetry"]])) + 1e-12)
    g_scale = float(np.mean(_pca_err(g_sc, g_pca, X_tr[:, MODALITIES["gravity"]])) + 1e-12)
    return (b_sc, b_pca, b_scale), (g_sc, g_pca, g_scale)


def _score_late_fusion(model, X_te, bathy_missing=False, grav_missing=False):
    (b_sc, b_pca, b_scale), (g_sc, g_pca, g_scale) = model
    parts = []
    if not bathy_missing:
        parts.append(_pca_err(b_sc, b_pca, X_te[:, MODALITIES["bathymetry"]]) / b_scale)
    if not grav_missing:
        parts.append(_pca_err(g_sc, g_pca, X_te[:, MODALITIES["gravity"]]) / g_scale)
    return np.mean(parts, axis=0)


def eval_region_dropout(X, coords, region_name):
    """Compare Combined PCA vs. Late-Fusion Per-Modality Aggregation under modality dropout."""
    train, test = spatial_holdout(coords)
    X_tr, X_te = X[train], X[test]

    c_sc, c_pca = _fit_pca(X_tr)
    c_clean = _pca_err(c_sc, c_pca, X_te)
    Z_te = c_sc.transform(X_te)

    lf = _fit_late_fusion(X_tr)
    lf_clean = _score_late_fusion(lf, X_te)

    rows = []
    for label, cols, b_miss, g_miss in [
        ("bathymetry_missing", MODALITIES["bathymetry"], True, False),
        ("gravity_missing", MODALITIES["gravity"], False, True),
    ]:
        Z_drop = Z_te.copy()
        Z_drop[:, cols] = 0.0
        c_drop = _pca_err(c_sc, c_pca, X_te, z_override=Z_drop)
        lf_drop = _score_late_fusion(lf, X_te, bathy_missing=b_miss, grav_missing=g_miss)
        rows.append({
            "benchmark": f"{region_name}_{label}",
            "combined_pca_spearman": _rank_corr(c_clean, c_drop),
            "combined_pca_top5": _top_overlap(c_clean, c_drop, 0.05),
            "late_fusion_spearman": _rank_corr(lf_clean, lf_drop),
            "late_fusion_top5": _top_overlap(lf_clean, lf_drop, 0.05),
        })
    return rows


def eval_cross_region_defense(X_src, X_tgt, coords_tgt, src_name, tgt_name):
    """Compare Combined PCA vs. Late-Fusion Per-Modality Aggregation on cross-region transfer."""
    tgt_train, tgt_test = spatial_holdout(coords_tgt)
    X_te = X_tgt[tgt_test]

    # In-region references
    c_in_sc, c_in_pca = _fit_pca(X_tgt[tgt_train])
    c_in = _pca_err(c_in_sc, c_in_pca, X_te)
    lf_in = _score_late_fusion(_fit_late_fusion(X_tgt[tgt_train]), X_te)

    # Transferred models
    c_xf_sc, c_xf_pca = _fit_pca(X_src)
    c_xf = _pca_err(c_xf_sc, c_xf_pca, X_te)
    lf_xf = _score_late_fusion(_fit_late_fusion(X_src), X_te)

    return [{
        "benchmark": f"transfer_{src_name}_to_{tgt_name}",
        "combined_pca_spearman": _rank_corr(c_in, c_xf),
        "combined_pca_top5": _top_overlap(c_in, c_xf, 0.05),
        "late_fusion_spearman": _rank_corr(lf_in, lf_xf),
        "late_fusion_top5": _top_overlap(lf_in, lf_xf, 0.05),
    }]


def main():
    p = argparse.ArgumentParser(description="E12 Defense Comparison (Late-Fusion Aggregation vs Combined PCA)")
    p.add_argument("--ans-npz", default="data/processed/ans/feature_dataset.npz")
    p.add_argument("--ner-npz", default="data/processed/ner/feature_dataset.npz")
    p.add_argument("--output", default="data/processed/defense_comparison.csv")
    args = p.parse_args()

    ans = np.load(args.ans_npz)
    ner = np.load(args.ner_npz)

    rows = []
    rows.extend(eval_region_dropout(ans["X"], ans["coords"], "ANS"))
    rows.extend(eval_region_dropout(ner["X"], ner["coords"], "NER"))
    rows.extend(eval_cross_region_defense(ans["X"], ner["X"], ner["coords"], "ANS", "NER"))
    rows.extend(eval_cross_region_defense(ner["X"], ans["X"], ans["coords"], "NER", "ANS"))

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(rows)
    df.to_csv(out, index=False)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()

