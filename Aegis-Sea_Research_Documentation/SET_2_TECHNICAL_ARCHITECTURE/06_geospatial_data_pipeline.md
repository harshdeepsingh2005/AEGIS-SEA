# 06 — Geospatial Data Pipeline

## 1. Pipeline principles

- Preserve original source files unchanged.
- Never overwrite raw observations with processed outputs.
- Preserve coordinate reference systems and units.
- Store native resolution and uncertainty metadata.
- Maintain a validity/coverage mask for every modality.
- Distinguish measured values from interpolated values.
- Avoid spatial leakage between train, validation and test regions.
- Make every transformation reproducible through configuration.

## 2. Pipeline stages

### Stage 1 — Ingestion
Download source files and catalogue metadata. Record provider, survey, acquisition date, processing level, licence and checksum.

### Stage 2 — Inspection
Inspect dimensions, coordinate systems, units, nodata conventions, sampling geometry, outliers and metadata. For raster products, inspect geotransforms and pixel sizes. For tracklines, inspect navigation and sampling intervals.

### Stage 3 — Quality control
Flag rather than silently delete suspicious observations. Possible checks:
- Missing or invalid coordinates.
- Duplicate observations.
- Impossible values or unit mismatches.
- Navigation gaps.
- Sensor artefacts documented by source metadata.
- Unreasonable local gradients.
- Inconsistent timestamps.
- Coverage gaps.

Keep a QC reason code for each flagged observation.

### Stage 4 — Coordinate standardization
Select an appropriate projected CRS for local metric analysis. Record the transformation. Preserve original coordinates in the provenance layer. Do not calculate terrain derivatives in geographic degrees.

### Stage 5 — Analysis grids
Use separate regional and local grids if needed:
- Regional grid for broad spatial context.
- Local high-resolution grid for survey-covered morphology.

The grid cell size must be justified by the coarsest relevant input and scientific question. A fine output grid does not increase source information content.

### Stage 6 — Spatial alignment
Align modalities only after documenting their native support:
- Raster-to-raster resampling.
- Trackline-to-grid interpolation, if justified.
- Event catalog aggregation over a stated time window.
- Coverage and uncertainty layers.
- Source-specific masks.

Use resampling methods appropriate to data type. Continuous measurements, categorical masks and event counts should not be treated identically.

### Stage 7 — Feature engineering
Candidate terrain features:
- Slope.
- Profile and plan curvature.
- Terrain ruggedness.
- Local relief.
- Bathymetric position index at multiple scales.
- Roughness.
- Multiscale derivatives.

Candidate geophysical features:
- Gravity anomaly and local residuals, if product definitions support them.
- Magnetic anomaly and derivatives, if corrections and reference field are known.
- Backscatter statistics, only if valid backscatter data exist.
- Seismic event density and magnitude summaries over explicit time windows.

Do not derive a feature if the source resolution cannot support it.

### Stage 8 — Master dataset
Each spatial unit should include:
- Stable spatial ID.
- Coordinates and CRS.
- Source values.
- Per-modality validity masks.
- Per-modality uncertainty or quality fields.
- Native resolution metadata.
- Derived terrain/geophysical features.
- Temporal-window metadata for seismicity.
- Spatial block ID.
- Split assignment.

## 3. Missing-data handling

Never replace all missing values with zero without a scientific justification.

Recommended representation:
- Value array.
- Validity mask.
- Optional uncertainty array.
- Optional source/coverage code.

Compare:
1. Complete-case analysis over common coverage.
2. Mask-aware modelling.
3. Missing-modality training, if enough data exist.

Imputation must be fitted using training data only where the method learns from the dataset. Do not leak validation/test information into preprocessing.

## 4. Seismicity feature construction

Earthquake features should include:
- Catalog source.
- Time window.
- Magnitude threshold.
- Event-location uncertainty, if available.
- Depth uncertainty, if available.
- Spatial aggregation radius or kernel.
- Station/network context and completeness limitations.

Possible features:
- Event count.
- Magnitude statistics.
- Magnitude-weighted density.
- Time since last event.
- Temporal rate over defined windows.

Do not interpret zero events as proof of seismic quiescence.

## 5. Spatial split strategy

Use spatial blocks or geographically separated regions. Possible design:
- Training blocks.
- Validation blocks for model selection.
- Held-out test blocks used once for final evaluation.

Choose block size based on spatial autocorrelation range, geological feature scale and data footprint. Report the split map.

Where feasible, repeat with multiple block assignments. Avoid random cell-level splits as the sole evaluation.

## 6. Data leakage controls

- Fit normalization only on training data.
- Fit imputation only on training data.
- Do not use test-region statistics to choose features.
- Do not tune thresholds on the final test set.
- Keep geological reference labels separate from unsupervised training inputs if they are used for evaluation.
- Do not use survey identifiers as unintended shortcuts unless survey effects are explicitly being studied.

## 7. Suggested formats

- Raw: original provider formats.
- Raster intermediates: Cloud Optimized GeoTIFF or NetCDF where suitable.
- Multidimensional arrays: Zarr/NetCDF.
- Vector features: GeoPackage.
- Tabular metadata: CSV or Parquet.
- Configuration: YAML.
- Experiment outputs: JSON/CSV plus model checkpoints.

## 8. Quality-control outputs

Produce:
- Per-modality coverage maps.
- Native-resolution maps or survey-track plots.
- Missingness maps.
- Uncertainty maps where available.
- Cross-modality overlap map.
- Distribution plots before/after preprocessing.
- A processing log with software versions and parameters.
