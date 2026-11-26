# Aegis-Sea 2.0 — Three-Week Research Starter

This repository is an **executable research scaffold**, not a completed scientific result.
It contains no fabricated measurements, labels, metrics, maps, or conclusions.

## Research focus

Reliability of multimodal geophysical anomaly detection under spatial-resolution mismatch,
missing observations, measurement degradation, and bounded model-directed perturbations.
Initial core modalities: bathymetry + gravity. Magnetic data are optional and must pass
coverage/quality checks before inclusion.

## Hardware target

MacBook Air M4, 16 GB RAM. The starter uses CPU-friendly NumPy/SciPy/scikit-learn workflows.
It deliberately avoids requiring a GPU or training a large neural network.

## 1. Environment setup

Recommended: Python 3.11 in a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If `rasterio` installation fails on macOS, install it using conda-forge:
`conda install -c conda-forge rasterio geopandas`.

## 2. Add data

Place georeferenced GeoTIFFs here:

```text
data/raw/bathymetry.tif
data/raw/gravity.tif
```

The rasters may have different coordinate systems, resolutions, and grids.
The pipeline reprojects gravity onto the bathymetry grid. This does **not** increase
the information content of the coarser source. The selected target grid and resampling
method must be documented in the paper.

Use datasets with documented units, acquisition/source details, licence, and uncertainty.
Do not treat missing cells as zero. No data should be silently filled.

## 3. Run the pipeline

```bash
python -m src.run_pipeline \
  --bathymetry data/raw/bathymetry.tif \
  --gravity data/raw/gravity.tif \
  --output data/processed
```

Optional parameters:

```bash
--max-cells 150000
--test-blocks 1
```

The pipeline writes:
- `feature_dataset.npz` — feature matrix, coordinates, and validity mask
- `metadata.json` — raster metadata and preprocessing record
- `baseline_scores.csv` — test-region anomaly scores for Isolation Forest and PCA
- `robustness.csv` — score stability under noise, modality dropout, and bounded PCA residual-directed perturbation; resolution degradation is explicitly marked not run
- `anomaly_map.png` — exploratory anomaly score map (not geological truth)

## 4. Important scientific safeguards

- The first raster (bathymetry) defines the analysis grid. Check its native resolution.
- Gravity is reprojected using bilinear interpolation. Record source resolution and CRS.
- The study area must be cropped to a documented Lō‘ihi boundary before running.
- The default split is a geographic holdout based on projected x-coordinate blocks.
  Inspect the split map and change it if it does not create a defensible spatial separation.
- Model scores are **unusualness scores**, not confirmed geological discoveries.
- Without independent reference labels, do not report precision, recall, F1, ROC-AUC, or
  detection accuracy. Report score stability and qualitative map inspection instead.
- Synthetic perturbations are controlled stress tests, not evidence of real sensor attacks.
- The PCA residual-directed perturbation is a model-directed score-maximizing stress test
  under an explicit per-feature bound; it is not a claim about a physically feasible attack.
- No results are included until the pipeline is run on verified source data.

## 5. Paper workflow

Start with `paper/manuscript.md`. Keep all results placeholders until experiments finish.
Record every dataset, software version, parameter, random seed, and exclusion decision.
Use `paper/references.bib` as a bibliography starter; verify every citation before submission.

## 6. Three-week schedule

- Days 1–3: verify datasets, define boundary, draft Introduction/Related Work.
- Days 4–7: data QC, coverage maps, common-grid dataset, Methods draft.
- Days 8–11: baseline models and spatial holdout.
- Days 12–15: fusion/ablation and degradation experiments.
- Days 16–18: bounded perturbation, reruns, interpretation.
- Days 19–21: complete manuscript, verify references, format and internal review.

## 7. Team ownership

1. Data engineer: source data, boundary, raster QC, metadata, coverage.
2. ML engineer: features, Isolation Forest, PCA, model comparisons.
3. Robustness engineer: corruptions, bounded perturbation, robustness analysis.
4. Research/evaluation lead: spatial split review, figures, references, manuscript integration.

## 8. Reproducibility

Run from repository root. Keep raw data out of Git if licensing or file size is an issue.
Commit code, configs, metadata, scripts, and non-sensitive derived summaries. Add a `DATA.md`
record describing exact source URLs, access dates, licences, versions, and processing steps.
