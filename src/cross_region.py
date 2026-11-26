"""Cross-region spatial generalization (E13 / H6) between ANS and NER."""

import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from .models import MODALITIES, _fit_pair, spatial_holdout
from .robustness import _rank_corr, _top_overlap


def _eval_transfer(X_src, X_tgt, coords_tgt, src_name, tgt_name):
    """Train on all samples of src_name, score held-out test block of tgt_name, compare to in-region baseline."""
    _, tgt_test = spatial_holdout(coords_tgt)
    X_comb = np.vstack([X_src, X_tgt[tgt_test]])
    tr_mask = np.zeros(len(X_comb), dtype=bool)
    tr_mask[: len(X_src)] = True
    te_mask = ~tr_mask

    tgt_train, _ = spatial_holdout(coords_tgt)
    rows = []
    for mod, cols in MODALITIES.items():
        iso_xfer, pca_xfer, _, _ = _fit_pair(X_comb[:, cols], tr_mask, te_mask)
        iso_in, pca_in, _, _ = _fit_pair(X_tgt[:, cols], tgt_train, tgt_test)
        rows.append({
            "train_region": src_name,
            "test_region": tgt_name,
            "modality": mod,
            "test_samples": int(tgt_test.sum()),
            "iso_spearman_vs_in_region": _rank_corr(iso_in, iso_xfer),
            "iso_top_5pct_overlap": _top_overlap(iso_in, iso_xfer, 0.05),
            "pca_spearman_vs_in_region": _rank_corr(pca_in, pca_xfer),
            "pca_top_5pct_overlap": _top_overlap(pca_in, pca_xfer, 0.05),
        })
    return rows


def main():
    p = argparse.ArgumentParser(description="Cross-region transfer evaluation (ANS <-> NER)")
    p.add_argument("--ans-npz", default="data/processed/ans/feature_dataset.npz")
    p.add_argument("--ner-npz", default="data/processed/ner/feature_dataset.npz")
    p.add_argument("--output", default="data/processed/cross_region_transfer.csv")
    args = p.parse_args()

    ans = np.load(args.ans_npz)
    ner = np.load(args.ner_npz)
    rows = []
    rows.extend(_eval_transfer(ans["X"], ner["X"], ner["coords"], "ANS", "NER"))
    rows.extend(_eval_transfer(ner["X"], ans["X"], ans["coords"], "NER", "ANS"))

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(rows)
    df.to_csv(out, index=False)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()

