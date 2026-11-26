# 05 — Dataset Acquisition and Feasibility

## 1. Objective

Establish which geophysical observations are actually available around Lō‘ihi, at what resolution, over what geographic and temporal extent, with what uncertainty and under what licence. Dataset feasibility is a project gate, not an administrative task.

## 2. Candidate datasets

| Modality | Candidate source | Intended use | Main concern |
|---|---|---|---|
| Regional bathymetry | GEBCO | Regional depth context | Grid spacing is not uniform measurement resolution |
| Survey bathymetry | NOAA NCEI / MGDS | Detailed morphology | Survey-specific coverage and processing |
| Gravity | NOAA NCEI marine gravity | Regional/sub-regional geophysical signal | Trackline or grid coverage may be sparse |
| Magnetics | NOAA NCEI marine geophysics; expedition archives | Magnetic anomaly information | Coverage, corrections and metadata |
| Multibeam | NOAA NCEI / MGDS | High-resolution bathymetry, backscatter if available | Survey footprint and native product type |
| Earthquakes | USGS ComCat / FDSN event service; relevant OBS studies | Auxiliary seismicity features | Offshore completeness and changing detection threshold |
| Geological references | Published maps, papers and survey reports | Independent interpretation/validation | Feature boundaries and confidence may be uncertain |

## 3. Starting portals

- GEBCO: https://www.gebco.net/
- NOAA NCEI: https://www.ncei.noaa.gov/
- NOAA marine gravity: https://www.ngdc.noaa.gov/mgg/gravity/
- NOAA marine geophysical data: https://www.ngdc.noaa.gov/mgg/gdas/
- NOAA multibeam: https://www.ngdc.noaa.gov/mgg/bathymetry/multibeam/
- Marine Geoscience Data System: https://www.marine-geo.org/
- USGS FDSN event service: https://earthquake.usgs.gov/fdsnws/event/1/
- USGS event search: https://earthquake.usgs.gov/earthquakes/search/

## 4. Study-area boundary

Define a reproducible polygon around the seamount and surrounding reference area. Record:
- Coordinate reference system.
- Polygon source and rationale.
- Bounding box.
- Included/excluded geological structures.
- Buffer size and reason.
- Whether the region is intended for local morphology or regional context.

Do not choose the boundary after looking at model results.

## 5. Dataset inventory schema

Create one row per source file or survey product with:

| Field | Meaning |
|---|---|
| dataset_id | Stable internal identifier |
| provider | NOAA, GEBCO, USGS, MGDS, etc. |
| product_title | Exact catalogue title |
| cruise_or_survey_id | Survey identifier |
| url | Stable landing page or download URL |
| download_date | Date retrieved |
| acquisition_start/end | Observation dates |
| modality | Bathymetry, gravity, magnetics, seismicity, backscatter |
| native_format | NetCDF, GeoTIFF, CSV, MB-System, shapefile, etc. |
| native_crs | Source coordinate system |
| native_resolution | Actual stated sampling/resolution |
| spatial_coverage | Footprint or trackline extent |
| uncertainty | Documented uncertainty, if available |
| processing_level | Raw, corrected, gridded, derived |
| licence | Reuse and redistribution conditions |
| checksum | SHA256 or equivalent |
| notes | Quality and provenance comments |

## 6. Feasibility tests

### Test A — Geographic overlap
Create footprints for each modality and calculate:
- Area covered by each modality.
- Area covered by at least two modalities.
- Area covered by all candidate modalities.
- Trackline density for irregular observations.
- Unobserved regions.

### Test B — Resolution compatibility
For each source, document:
- Native sample spacing.
- Effective spatial resolution.
- Interpolation or gridding method.
- Measurement uncertainty.
- Whether the product is a direct observation or a derived grid.

Do not infer effective resolution from pixel size alone.

### Test C — Temporal compatibility
Record observation periods. Decide whether the research is:
- Static morphology analysis.
- Time-aware geophysical analysis.
- A mixed-time composite.

Do not combine temporal features without recording the mismatch.

### Test D — Label/reference availability
Identify published geological features and determine whether their footprints and confidence are sufficient for spatial validation. A named feature is not automatically a pixel-level ground-truth label.

### Test E — Data-use rights
Confirm whether files can be redistributed. If not, publish scripts, metadata and retrieval instructions rather than republishing restricted data.

## 7. Go/no-go thresholds

The team must define numerical thresholds after inspecting actual data. Do not invent thresholds in advance without understanding the source sampling.

A minimum viable dataset should include:
- Bathymetry over the study region.
- At least one additional geophysical modality with documented usable overlap.
- Explicit coverage/quality masks.
- Sufficient independent spatial blocks for validation.
- At least one defensible source of geological reference evidence for interpretation.

If magnetics are unavailable or too sparse, remove them from the primary fusion experiment and report the limitation. Do not fabricate a magnetic raster through unconstrained interpolation.

## 8. Deliverables

1. `data_inventory.csv`
2. `coverage_map.png` or GeoPackage project
3. `resolution_comparison.csv`
4. `temporal_compatibility.md`
5. `reference_features.gpkg` or equivalent, with provenance
6. `data_feasibility_report.md`
7. Download scripts and source checksums

## 9. Decision

The principal model architecture is not approved until the feasibility report demonstrates that the selected modalities have adequate overlap and that the validation plan is realistic.
