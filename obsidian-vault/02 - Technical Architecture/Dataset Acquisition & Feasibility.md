---
tags:
  - technical-architecture
  - data-feasibility
  - datasets
source: Aegis-Sea_Research_Documentation/SET_2_TECHNICAL_ARCHITECTURE/05_dataset_acquisition_and_feasibility.md
created: 2026-11-26
---

# Dataset Acquisition and Feasibility

> [!NOTE] Source
> Distilled from `05_dataset_acquisition_and_feasibility.md`. Parent: [[MOC - Technical Architecture]].

Dataset feasibility is **Gate 1** ([[Project Charter]]), not an administrative task.

## 1. Candidate Datasets
| Modality | Candidate Source | Intended Use | Main Concern |
|---|---|---|---|
| **Regional bathymetry** | GEBCO | Regional depth context | Grid spacing $\neq$ uniform measurement resolution |
| **Survey bathymetry** | NOAA NCEI / MGDS | Detailed morphology | Survey-specific coverage & processing |
| **Gravity** | NOAA NCEI marine gravity | Regional/sub-regional signal | Trackline or grid coverage may be sparse |
| **Magnetics** | NOAA NCEI marine geophysics; expedition archives | Magnetic anomaly info | Coverage, corrections & metadata |
| **Multibeam** | NOAA NCEI / MGDS | High-res bathymetry, backscatter | Survey footprint & native product type |
| **Earthquakes** | USGS ComCat / FDSN; OBS studies | Auxiliary seismicity features | Offshore completeness & changing threshold |
| **Geological references** | Published maps, papers, survey reports | Independent validation | Feature boundaries & confidence uncertain |

## 2. Study-Area Boundary
Define a reproducible polygon around Lō‘ihi **before** inspecting model results. Record CRS, polygon source/rationale, bounding box, included/excluded structures, buffer size, and local vs. regional intent.

## 3. Dataset Inventory Schema (17 Fields)
`dataset_id`, `provider`, `product_title`, `cruise_or_survey_id`, `url`, `download_date`, `acquisition_start/end`, `modality`, `native_format`, `native_crs`, `native_resolution`, `spatial_coverage`, `uncertainty`, `processing_level`, `licence`, `checksum` (SHA-256), `notes`.

## 4. Five Feasibility Tests (A–E)
- **Test A — Geographic overlap:** Area per modality, $\ge 2$ modalities, all modalities, trackline density, unobserved regions.
- **Test B — Resolution compatibility:** Native sample spacing, effective spatial resolution, gridding method, uncertainty, direct vs. derived product. *Never infer effective resolution from pixel size alone.*
- **Test C — Temporal compatibility:** Static morphology vs. time-aware vs. mixed-time composite; record mismatches.
- **Test D — Label/reference availability:** A named geological feature is not automatically a pixel-level ground-truth label.
- **Test E — Data-use rights:** If redistribution is restricted, publish retrieval scripts, metadata, and checksums instead.

## 5. Minimum Viable Dataset & Fallbacks
- Bathymetry over the study region + $\ge 1$ additional geophysical modality with usable overlap (gravity is the primary partner in the starter `README.md`).
- Explicit coverage/quality masks, sufficient independent spatial blocks, and $\ge 1$ geological reference source.
- **Magnetics rule:** If magnetics are unavailable or too sparse, drop them from primary fusion and report the limitation—never fabricate a magnetic raster via unconstrained interpolation.

## 6. Seven Deliverables
`data_inventory.csv`, `coverage_map.png` (or GeoPackage), `resolution_comparison.csv`, `temporal_compatibility.md`, `reference_features.gpkg`, `data_feasibility_report.md`, and download scripts + checksums.

