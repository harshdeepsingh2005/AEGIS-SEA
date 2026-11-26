---
tags:
  - research-foundation
  - literature
  - novelty
source: Aegis-Sea_Research_Documentation/SET_1_RESEARCH_FOUNDATION/02_literature_review_and_novelty.md
created: 2026-11-26
---

# Literature Review & Novelty Assessment

> [!NOTE] Source
> Distilled from `02_literature_review_and_novelty.md`. Parent: [[MOC - Research Foundation]].

## 1. Six Research Areas to Review
- **A. Seamount detection & seafloor characterization:** Satellite gravity anomalies, shipborne multibeam bathymetry, geomorphometry, classical/DL methods, seamount inventories. *Key comparator to inspect:* *Global Detection and Morphological Characterization of Seamounts With Weakly Supervised Deep Learning* (inspect exact modalities, labels, resolution, validation, limitations).
- **B. Multimodal geophysical ML:** Early vs. feature-level vs. decision-level fusion, modality-specific encoders, missing-modality learning, multi-resolution fusion, uncertainty-aware fusion, ablation. Must distinguish true multimodal learning from stacking interpolated rasters.
- **C. Anomaly detection:** Isolation Forest, robust covariance/LOF, PCA reconstruction, dense/convolutional AEs, VAEs, Deep SVDD, spatial anomaly detection. Reconstruction error $\neq$ geological anomaly probability.
- **D. Robustness & adversarial ML:** Random noise, bias/drift, missingness, smoothing/resolution loss, white-box/black-box attacks, adversarial training. Separate ordinary degradation from model-directed adversarial attacks.
- **E. Spatial validation & distribution shift:** Spatial autocorrelation, spatial block CV, geographic holdout, survey-to-survey shift, temporal shift, resolution-induced shift, external validation.
- **F. Environmental performance disparity:** Group-robust learning, worst-group performance, spatial fairness, DRO—using scientifically meaningful strata (terrain complexity, depth regime, survey quality, modality availability) rather than demographic fairness.

## 2. Provisional Novelty Assessment
- **Low / Established:** ML on Lō‘ihi alone; bathymetry + gravity; generic multimodal anomaly detection.
- **Promising:** Resolution-mismatch benchmark, sensor degradation benchmark, constrained adversarial evaluation, robustness under missing modalities.
- **Potentially distinctive:** Joint robustness and environmental reliability (requires formal systematic review).

> [!WARNING] Claim Guardrail
> Do **not** use "first", "novel", or "state-of-the-art" in the final manuscript unless the completed literature review and comparative experiments support those claims.

## 3. Search Protocol & Extraction Matrix
- **Databases:** Google Scholar, Crossref, OpenAlex, IEEE Xplore, AGU/Wiley, ScienceDirect, SpringerLink.
- **Citation-chain inspection:** References, citing papers, same-author work, code/data availability, newer journal extensions.
- **Extraction fields:** Citation/DOI, Year/venue, Study area, Modalities, Spatial resolution (native vs. model), Method/fusion, Labels, Validation, Robustness tests, Metrics, Limitations, Relevance (direct/adjacent/background).

## 4. Starting Portals
- GEBCO (`gebco.net`), NOAA NCEI (`ncei.noaa.gov`), NOAA marine gravity (`ngdc.noaa.gov/mgg/gravity/`), NOAA marine geophysics (`ngdc.noaa.gov/mgg/gdas/`), NOAA multibeam (`ngdc.noaa.gov/mgg/bathymetry/multibeam/`), MGDS (`marine-geo.org`), USGS earthquake catalog (`earthquake.usgs.gov/fdsnws/event/1/`), AGU / JGR: Machine Learning and Computation, Remote Sensing (MDPI), IEEE Xplore.

