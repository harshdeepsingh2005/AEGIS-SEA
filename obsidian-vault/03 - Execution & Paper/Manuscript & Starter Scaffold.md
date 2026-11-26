---
tags:
  - execution
  - starter
  - manuscript
  - data-provenance
sources:
  - README.md
  - DATA.md
  - requirements.txt
  - paper/manuscript.md
  - paper/references.bib
created: 2026-11-26
---

# Manuscript & Starter Scaffold

> [!NOTE] Sources
> Root `README.md`, `DATA.md`, `requirements.txt`, `paper/manuscript.md`, `paper/references.bib`. Parent: [[MOC - Execution & Paper]].

## 1. Root Starter Configuration (`README.md` & `requirements.txt`)
- **Target environment:** Python 3.11 venv on MacBook Air M4 (16 GB RAM), CPU-only.
- **Dependencies (`requirements.txt`):** `numpy>=1.26`, `scipy>=1.11`, `pandas>=2.1`, `scikit-learn>=1.4`, `matplotlib>=3.8`, `rasterio>=1.3.9` (conda-forge fallback if `rasterio` fails on macOS).
- **Expected raw inputs:** `data/raw/bathymetry.tif` (defines target analysis grid) and `data/raw/gravity.tif` (reprojected onto bathymetry grid via bilinear interpolation).
- **Planned CLI (`README.md`):**
  ```bash
  python -m src.run_pipeline \
    --bathymetry data/raw/bathymetry.tif \
    --gravity data/raw/gravity.tif \
    --output data/processed
  ```
  Optional: `--max-cells 150000`, `--test-blocks 1`.
- **Planned outputs:** `feature_dataset.npz`, `metadata.json`, `baseline_scores.csv`, `robustness.csv`, `anomaly_map.png`.

> [!WARNING] Current Workspace Reality (2026-11-26)
> `src/` and `data/` are **not** currently present in the repository root—only `README.md`, `DATA.md`, `requirements.txt`, `paper/`, and `Aegis-Sea_Research_Documentation/` exist on disk.

## 2. Data Provenance Log (`DATA.md`)
Blank 15-field provenance table for **Bathymetry**, **Gravity**, and **Optional magnetics**: Provider, Product/dataset name, Download URL, Access date, Version/release, Native CRS, Native resolution, Units, NoData value, Spatial bounds, Acquisition date/period, Licence/terms, Uncertainty information, Citation/DOI, File checksum (SHA-256).

## 3. Manuscript Draft (`paper/manuscript.md`) & Bibliography (`paper/references.bib`)
- **Manuscript status:** Working IEEE-style draft with 8 numbered sections (I. Introduction $\rightarrow$ VIII. Conclusion) plus Abstract, Data/Code Availability, Acknowledgment, and References. All empirical sections (V.A–V.E) are explicit placeholders pending pipeline execution.
- **Starter BibTeX (`paper/references.bib`):** 3 unverified starter entries (`igarss2027paperkit`, `loihi_magnetic_structure`, `weakly_supervised_seamount_detection`), each carrying explicit warnings to verify metadata/DOI/authors before citing.

