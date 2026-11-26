---
tags:
  - technical-architecture
  - pipeline
  - geospatial
source: Aegis-Sea_Research_Documentation/SET_2_TECHNICAL_ARCHITECTURE/06_geospatial_data_pipeline.md
created: 2026-11-26
---

# Geospatial Data Pipeline

> [!NOTE] Source
> Distilled from `06_geospatial_data_pipeline.md`. Parent: [[MOC - Technical Architecture]].

## 1. Core Principles
- Preserve raw files unchanged; never overwrite raw observations.
- Preserve CRS, units, native resolution, and uncertainty metadata.
- Maintain per-modality validity/coverage masks; distinguish measured vs. interpolated values.
- Prevent spatial leakage between train, validation, and test regions.
- Make every transformation reproducible via configuration.

## 2. Eight Pipeline Stages
1. **Ingestion:** Download & catalogue metadata (provider, survey, date, processing level, licence, SHA-256).
2. **Inspection:** Dimensions, CRS, units, nodata conventions, sampling geometry, outliers, geotransforms/pixel sizes or trackline intervals.
3. **Quality control:** Flag (never silently delete) with reason codes: invalid coords, duplicates, impossible values/units, navigation gaps, sensor artifacts, unreasonable gradients, inconsistent timestamps, coverage gaps.
4. **Coordinate standardization:** Select local projected CRS for metric analysis (never compute terrain derivatives in geographic degrees).
5. **Analysis grids:** Separate regional grid (broad context) and local high-res grid (survey-covered morphology) if needed; grid size justified by coarsest relevant input.
6. **Spatial alignment:** Document native support before raster-to-raster resampling, trackline interpolation, or event aggregation. Match resampling method to data type (continuous vs. categorical vs. counts).
7. **Feature engineering:**
   - *Terrain:* slope, profile/plan curvature, ruggedness, local relief, multiscale BPI, roughness.
   - *Geophysical:* gravity anomaly/local residuals, magnetic anomaly/derivatives (if valid), backscatter stats (if valid), seismic density/magnitude summaries. *Never derive a feature unsupported by source resolution.*
8. **Master dataset:** Stable spatial ID, coords & CRS, source values, per-modality validity masks, uncertainty/quality fields, native resolution metadata, derived features, seismicity temporal window, spatial block ID, split assignment.

## 3. Missing-Data & Seismicity Rules
- **Missing data:** Never replace all missing values with zero without justification. Represent as `(value_array, validity_mask, optional_uncertainty, optional_source_code)`. Compare complete-case, mask-aware modeling, and missing-modality training. Fit imputation on **training data only**.
- **Seismicity:** Record catalog source, time window, magnitude threshold, location/depth uncertainty, aggregation radius/kernel, and network completeness. *Never interpret zero events as proof of seismic quiescence.*

## 4. Spatial Split & Data-Leakage Controls
- Use **spatial blocks** or geographically separated regions (train / validation / held-out test), sized by spatial autocorrelation range, geological scale, and data footprint. Avoid random cell-level splits as primary evaluation.
- Fit normalization & imputation on training blocks only; do not use test statistics for feature selection or threshold tuning; keep reference labels separate from unsupervised training; avoid using survey IDs as shortcuts.

## 5. Suggested Formats & QC Outputs
- **Formats:** Raw (provider), Raster intermediates (COG / NetCDF), Arrays (Zarr / NetCDF), Vectors (GeoPackage), Tables (CSV / Parquet), Configs (YAML), Outputs (JSON/CSV + checkpoints).
- **QC outputs:** Per-modality coverage maps, native-resolution/track plots, missingness maps, uncertainty maps, cross-modality overlap map, pre/post distribution plots, processing log.

