---
tags:
  - agent-memory
  - invariants
  - sync-log
created: 2026-11-26
---

# Memory Index & Invariants

> [!NOTE] Purpose
> Persistent operational memory for AI agents working in `AEGIS-SEA`, synchronized with the `everything-antigravity_memory` knowledge graph. Parent: [[Home]].

## 1. Verified Repository Inventory (2026-11-26)
- `README.md` — 3-week research starter instructions (references `src.run_pipeline` & `data/raw/`).
- `DATA.md` — Blank 15-field data provenance table (bathymetry, gravity, optional magnetics).
- `requirements.txt` — 6 CPU Python packages (`numpy`, `scipy`, `pandas`, `scikit-learn`, `matplotlib`, `rasterio`).
- `paper/manuscript.md` — Working paper draft with explicit result placeholders.
- `paper/references.bib` — 3 starter BibTeX entries requiring verification.
- `Aegis-Sea_Research_Documentation/` — Complete 12-document research plan across `SET_1_RESEARCH_FOUNDATION/` (01–04), `SET_2_TECHNICAL_ARCHITECTURE/` (05–08), and `SET_3_EXECUTION_AND_EXPERIMENTS/` (09–12).
- `.venv/` — Python 3.11.9 virtual environment with `requirements.txt` installed (`numpy`, `scipy`, `pandas`, `scikit-learn`, `matplotlib`, `rasterio`).
- `src/` — Implemented `geodata.py`, `models.py`, `robustness.py`, `plots.py`, `run_pipeline.py`.
- `tests/test_pipeline_smoke.py` — End-to-end smoke test on synthetic projected GeoTIFFs (PASSED on 2026-11-26).
- `scripts/prepare_rasters.py` — Gate 1 helper to crop/reproject bathymetry & gravity GeoTIFFs to `EPSG:32605` (UTM 5N) and print SHA-256 + native metadata for `DATA.md`.
- **Not present yet:** Real GeoTIFFs in `data/raw/` (`bathymetry.tif`, `gravity.tif`) and `data/processed/` outputs.

## 2. Hard Scientific & Engineering Invariants
1. **No fabricated results:** Never invent metrics, geological labels, maps, or conclusions.
2. **Anomaly $\neq$ Discovery:** Model scores are statistical unusualness scores, never proof of geological features or eruption predictions.
3. **Resolution honesty:** Reprojecting coarse gravity onto a finer bathymetry grid does not increase gravity's information content; never infer effective resolution from pixel size alone.
4. **No silent zero-imputation:** Retain per-modality validity/coverage masks; never replace missing cells with `0`.
5. **Spatial validation first:** Use spatially separated blocks/holdouts; fit normalization and imputation on training blocks only.
6. **Threat-model discipline:** Separate ordinary measurement degradation (Family A) from model-directed adversarial attacks (Family B).
7. **Gate ordering:** Do not build full defense models until Gates 1–3 ([[Project Charter]]) pass.
8. **Claim discipline:** Do not claim "first", "novel", "SOTA", or global generalization without completed literature/empirical support.

## 3. Knowledge Graph Sync Log
- **2026-11-26:** Cleared previous vault and verified empty `everything-antigravity_memory` graph; rebuilt complete vault from fresh full-repo read and populated `everything-antigravity_memory` entities and relations.

