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
- `scripts/prepare_rasters.py` — Gate 1 helper to crop/reproject bathymetry & gravity GeoTIFFs to local UTM CRS (`EPSG:32744` for Afanasy Nikitin Seamount, `EPSG:32745` for Ninety East Ridge) and print SHA-256 + native metadata for `DATA.md`.
- **Gate 1 & Gate 3 Executed (2026-11-26):** Downloaded SRTM15+ bathymetry (`ans_srtm15.nc`, `ner_srtm15.nc`) and Scripps 1-min gravity (`ans_grav.xyz`, `ner_grav.xyz`), projected to `EPSG:32744` (ANS) and `EPSG:32745` (NER), and ran `src.run_pipeline` on both (`150,000` sampled cells each; `~460 m` bathy vs `~1830 m` gravity). See `DATA.md` and `data/processed/{ans,ner}/`.
- **E8 Resolution Degradation & E13 Cross-Region Transfer Executed (2026-11-26):**
  - `resolution_degradation_4x` (`sigma=2.0` px raster-space bathymetry smoothing): ANS Spearman `0.997` (top-5% `0.982`), NER Spearman `0.987` (top-5% `0.897`).
  - `cross_region_transfer.csv`: Asymmetric transfer—`NER -> ANS` combined PCA transfers at Spearman `0.926` (top-5% `0.897`), whereas `ANS -> NER` combined PCA collapses to Spearman `-0.029` (top-5% `0.491`) despite strong single-modality transfer (`0.930` bathy, `0.936` gravity).
- **E12 Defense Comparison Executed (`src/defenses.py`, 2026-11-26):**
  - Late-fusion per-modality score aggregation ($S(x) = \frac{1}{|M|} \sum_{m \in M} E_m(x)/\bar{E}_{m,\text{train}}$) fixes `ANS -> NER` collapse (`-0.134 -> 0.936`, top-5% `0.470 -> 0.957`) and improves all missing-modality benchmarks. See `data/processed/defense_comparison.csv`.
- **Gate 2, 5-Block Spatial CV, Figures & Manuscript Integration (2026-11-26):**
  - Fixed raster-edge derivative cliff in `src/geodata.py` via 1-px `binary_erosion` mask around `NaN`s.
  - Verified 7 DOIs in `paper/references.bib`; cross-referenced 5-block OOF peaks against Krishna et al. (2014), Paul et al. (1990), and Sreejith & Krishna (2013).
  - Ran 5-block spatial CV (`src/spatial_cv.py` -> `spatial_cv_summary.csv`), generated 3 publication figures (`reports/figures/fig1..fig3.png`), and integrated all verified results into `paper/manuscript.md`.

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

