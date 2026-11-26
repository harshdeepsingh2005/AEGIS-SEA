"""Generate publication-quality figures for ANS & NER (maps, 5-block CV, and cross-region transfer)."""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def make_region_maps(out_dir=Path("reports/figures")):
    out_dir.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 3, figsize=(14, 8.5), constrained_layout=True)
    configs = [
        ("ans", "Afanasy Nikitin Seamount (UTM 44S)"),
        ("ner", "Ninety East Ridge (UTM 45S)"),
    ]
    for r_idx, (reg, title) in enumerate(configs):
        d = np.load(f"data/processed/{reg}/feature_dataset.npz")
        oof = np.load(f"data/processed/{reg}/oof_scores.npz")["oof_late_fusion"]
        X, coords = d["X"], d["coords"]
        x_km, y_km = (coords[:, 0] - coords[:, 0].min()) / 1000.0, (coords[:, 1] - coords[:, 1].min()) / 1000.0

        panels = [
            (X[:, 0], "viridis", f"{title}\nBathymetry (m)"),
            (X[:, 3], "coolwarm", f"{title}\nFree-Air Gravity (mGal)"),
            (np.clip(oof, 0, np.nanquantile(oof, 0.99)), "magma", f"{title}\n5-Block OOF Late-Fusion Score"),
        ]
        for c_idx, (vals, cmap, ptitle) in enumerate(panels):
            ax = axes[r_idx, c_idx]
            sc = ax.scatter(x_km, y_km, c=vals, s=1.2, cmap=cmap, linewidths=0, rasterized=True)
            ax.set_title(ptitle, fontsize=10)
            ax.set_xlabel("Easting (km)")
            ax.set_ylabel("Northing (km)")
            fig.colorbar(sc, ax=ax, fraction=0.046, pad=0.03)

    fig.savefig(out_dir / "fig1_ans_ner_maps.png", dpi=240)
    plt.close(fig)


def make_cv_comparison(out_dir=Path("reports/figures")):
    df = pd.read_csv("data/processed/spatial_cv_summary.csv")
    df = df[df["condition"] != "pca_linf_0.10"].copy()
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 4.8), sharey=True, constrained_layout=True)
    conds = ["noise_0.20", "bathy_missing", "gravity_missing", "res_deg_4x"]
    labels = ["Noise\n(σ=0.20)", "Bathy\nMissing", "Gravity\nMissing", "Res. Deg.\n(4x)"]
    x = np.arange(len(conds))
    w = 0.35

    for ax, reg, title in zip(axes, ["ANS", "NER"], ["Afanasy Nikitin Seamount (ANS)", "Ninety East Ridge (NER)"]):
        sub = df[df["region"] == reg].set_index("condition").loc[conds]
        ax.bar(x - w / 2, sub["comb_spearman_mean"], yerr=sub["comb_spearman_ci95"], width=w, label="Combined PCA", capsize=4, color="#d95f02")
        ax.bar(x + w / 2, sub["late_spearman_mean"], yerr=sub["late_spearman_ci95"], width=w, label="Late-Fusion PCA (Defense D)", capsize=4, color="#1b9e77")
        ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_ylim(-0.6, 1.15)
        ax.set_title(title)
        ax.set_ylabel("Spearman Rank Correlation vs. Clean (5-Block CV ± 95% CI)")
        ax.legend(frameon=False, loc="lower left")

    fig.savefig(out_dir / "fig2_spatial_cv_robustness.png", dpi=240)
    plt.close(fig)


def make_transfer_plot(out_dir=Path("reports/figures")):
    df = pd.read_csv("data/processed/defense_comparison.csv")
    xfer = df[df["benchmark"].str.startswith("transfer_")].copy()
    fig, ax = plt.subplots(figsize=(7.5, 4.5), constrained_layout=True)
    x = np.arange(len(xfer))
    w = 0.32
    ax.bar(x - w / 2, xfer["combined_pca_spearman"], width=w, label="Combined PCA (Early Fusion)", color="#d95f02")
    ax.bar(x + w / 2, xfer["late_fusion_spearman"], width=w, label="Late-Fusion PCA (Defense D)", color="#1b9e77")
    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    ax.set_xticks(x)
    ax.set_xticklabels(["ANS → NER", "NER → ANS"])
    ax.set_ylim(-0.2, 1.1)
    ax.set_ylabel("Spearman Rank Correlation vs. In-Region Target")
    ax.set_title("Cross-Region Spatial Transfer (E13 & E12)")
    ax.legend(frameon=False)
    fig.savefig(out_dir / "fig3_cross_region_transfer.png", dpi=240)
    plt.close(fig)


def main():
    make_region_maps()
    make_cv_comparison()
    make_transfer_plot()
    print("Generated publication figures in reports/figures/")


if __name__ == "__main__":
    main()

