"""Multi-block spatial cross-validation (5 longitudinal blocks) with 95% CIs across E8, E11, E12."""

import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import t as t_dist
from .defenses import _fit_late_fusion, _fit_pca, _pca_err, _score_late_fusion
from .geodata import extract_resolution_degraded_features
from .models import MODALITIES
from .robustness import _rank_corr, _top_overlap


def assign_spatial_blocks(coords, n_blocks=5):
    """Partition projected x-coordinates into n_blocks equal-count longitudinal blocks."""
    edges = np.quantile(coords[:, 0], np.linspace(0.0, 1.0, n_blocks + 1))
    edges[0] -= 1.0
    edges[-1] += 1.0
    return np.digitize(coords[:, 0], edges[1:-1])


def run_spatial_cv(region, npz_path, bathy_path, grav_path, n_blocks=5, seed=7):
    data = np.load(npz_path)
    X, coords, rc = data["X"], data["coords"], data["rc"]
    blocks = assign_spatial_blocks(coords, n_blocks=n_blocks)
    rng = np.random.default_rng(seed)

    # Precompute 4x degraded features once for the whole sampled set
    X_deg4 = extract_resolution_degraded_features(bathy_path, grav_path, rc, sigma_px=2.0)

    block_rows = []
    oof_late = np.full(len(X), np.nan, dtype="float64")
    oof_comb = np.full(len(X), np.nan, dtype="float64")

    for b in range(n_blocks):
        te = blocks == b
        tr = ~te
        X_tr, X_te = X[tr], X[te]

        c_sc, c_pca = _fit_pca(X_tr)
        Z_te = c_sc.transform(X_te)
        c_clean = _pca_err(c_sc, c_pca, X_te, z_override=Z_te)
        oof_comb[te] = c_clean

        lf = _fit_late_fusion(X_tr)
        lf_clean = _score_late_fusion(lf, X_te)
        oof_late[te] = lf_clean

        # 1. Gaussian noise sigma=0.20
        noise = rng.normal(0, 0.20, Z_te.shape)
        c_noise = _pca_err(c_sc, c_pca, X_te, z_override=Z_te + noise)
        # Apply same standardized noise to each modality's standardized space
        Z_b_noise = lf[0][0].transform(X_te[:, MODALITIES["bathymetry"]]) + noise[:, MODALITIES["bathymetry"]]
        Z_g_noise = lf[1][0].transform(X_te[:, MODALITIES["gravity"]]) + noise[:, MODALITIES["gravity"]]
        lf_noise = 0.5 * (
            _pca_err(lf[0][0], lf[0][1], None, z_override=Z_b_noise) / lf[0][2]
            + _pca_err(lf[1][0], lf[1][1], None, z_override=Z_g_noise) / lf[1][2]
        )

        # 2. Modality dropout
        Z_bdrop = Z_te.copy(); Z_bdrop[:, MODALITIES["bathymetry"]] = 0.0
        Z_gdrop = Z_te.copy(); Z_gdrop[:, MODALITIES["gravity"]] = 0.0
        c_bdrop = _pca_err(c_sc, c_pca, X_te, z_override=Z_bdrop)
        c_gdrop = _pca_err(c_sc, c_pca, X_te, z_override=Z_gdrop)
        lf_bdrop = _score_late_fusion(lf, X_te, bathy_missing=True)
        lf_gdrop = _score_late_fusion(lf, X_te, grav_missing=True)

        # 3. E8 Raster-space 4x resolution degradation
        X_te_deg = X_deg4[te]
        fin = np.isfinite(X_te_deg).all(axis=1)
        c_deg4 = _pca_err(c_sc, c_pca, X_te_deg[fin])
        lf_deg4 = _score_late_fusion(lf, X_te_deg[fin])

        # 4. E11 Bounded L_inf PCA residual step (eps=0.10)
        recon = c_pca.inverse_transform(c_pca.transform(Z_te))
        res = Z_te - recon
        step = 0.10 * res / (np.max(np.abs(res), axis=1, keepdims=True) + 1e-12)
        c_adv = _pca_err(c_sc, c_pca, X_te, z_override=Z_te + step)

        tests = [
            ("noise_0.20", c_clean, c_noise, lf_clean, lf_noise),
            ("bathy_missing", c_clean, c_bdrop, lf_clean, lf_bdrop),
            ("gravity_missing", c_clean, c_gdrop, lf_clean, lf_gdrop),
            ("res_deg_4x", c_clean[fin], c_deg4, lf_clean[fin], lf_deg4),
            ("pca_linf_0.10", c_clean, c_adv, lf_clean, lf_clean),  # lf_clean placeholder for combined-only attack
        ]
        for cond, c_ref, c_p, l_ref, l_p in tests:
            block_rows.append({
                "region": region,
                "block": b,
                "condition": cond,
                "n_test": int(len(c_ref)),
                "comb_spearman": _rank_corr(c_ref, c_p),
                "comb_top5": _top_overlap(c_ref, c_p, 0.05),
                "late_spearman": np.nan if cond == "pca_linf_0.10" else _rank_corr(l_ref, l_p),
                "late_top5": np.nan if cond == "pca_linf_0.10" else _top_overlap(l_ref, l_p, 0.05),
            })

    return pd.DataFrame(block_rows), oof_comb, oof_late


def summarize_cv(df):
    t_crit = float(t_dist.ppf(0.975, df=df["block"].nunique() - 1))
    summary = []
    for (reg, cond), grp in df.groupby(["region", "condition"], sort=False):
        row = {"region": reg, "condition": cond, "n_blocks": len(grp)}
        for col in ("comb_spearman", "comb_top5", "late_spearman", "late_top5"):
            vals = grp[col].dropna()
            if len(vals) == 0:
                row[f"{col}_mean"] = np.nan
                row[f"{col}_ci95"] = np.nan
            else:
                row[f"{col}_mean"] = float(vals.mean())
                row[f"{col}_ci95"] = float(t_crit * vals.std(ddof=1) / np.sqrt(len(vals)))
        summary.append(row)
    return pd.DataFrame(summary)


def main():
    p = argparse.ArgumentParser(description="Run 5-block spatial CV on ANS and NER")
    p.add_argument("--out-dir", default="data/processed")
    args = p.parse_args()
    out = Path(args.out_dir)

    dfs = []
    for reg in ("ans", "ner"):
        df_b, oof_c, oof_l = run_spatial_cv(
            reg.upper(),
            out / reg / "feature_dataset.npz",
            f"data/raw/{reg}/bathymetry.tif",
            f"data/raw/{reg}/gravity.tif",
        )
        dfs.append(df_b)
        np.savez_compressed(out / reg / "oof_scores.npz", oof_combined=oof_c, oof_late_fusion=oof_l)

    all_blocks = pd.concat(dfs, ignore_index=True)
    summary = summarize_cv(all_blocks)
    all_blocks.to_csv(out / "spatial_cv_blocks.csv", index=False)
    summary.to_csv(out / "spatial_cv_summary.csv", index=False)
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()

