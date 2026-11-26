# 02 — Literature Review and Novelty Assessment

## 1. Purpose

This document defines the literature-review work needed to establish whether Aegis-Sea 2.0 addresses a genuine research gap. It is not a completed systematic review. The references below are starting points and must be checked against the final publication records, full texts and citation chains.

## 2. Research areas to review

### A. Seamount detection and seafloor characterization

Review methods based on:
- Satellite-derived gravity anomalies.
- Shipborne multibeam bathymetry.
- Bathymetric derivatives and geomorphometry.
- Classical image processing and object-based methods.
- Supervised, weakly supervised and unsupervised deep learning.
- Seamount inventories and geological validation.

A particularly relevant recent study is *Global Detection and Morphological Characterization of Seamounts With Weakly Supervised Deep Learning*. It is a close comparator because it combines geophysical information and deep learning for seamount detection. The team must inspect its exact input modalities, labels, spatial resolution, validation design and limitations before stating a gap.

### B. Multimodal geophysical machine learning

Review:
- Early fusion, feature-level fusion and decision-level fusion.
- Modality-specific encoders.
- Missing-modality learning.
- Sensor fusion under different resolutions.
- Uncertainty-aware fusion.
- Modality ablation and contribution analysis.

The review must distinguish multimodal learning from simply stacking interpolated raster layers. A scientifically defensible fusion method should preserve modality provenance, resolution and coverage information.

### C. Anomaly detection

Review:
- Isolation Forest.
- Robust covariance and local outlier methods.
- PCA reconstruction.
- Dense and convolutional autoencoders.
- Variational autoencoders, where justified.
- Deep SVDD or other one-class approaches, if suitable.
- Spatial anomaly detection and spatial dependence.

Do not assume that reconstruction error equals geological anomaly probability. A reconstruction model identifies patterns it reconstructs poorly; geological meaning requires independent interpretation.

### D. Robustness and adversarial machine learning

Review:
- Random measurement noise.
- Bias and drift.
- Missing observations.
- Spatial smoothing and resolution degradation.
- Sensor-specific uncertainty.
- Model-directed adversarial attacks.
- White-box and black-box threat models.
- Adversarial training and robust optimization.

Separate ordinary measurement degradation from adversarial attacks. A perturbation should only be called adversarial if it is selected to manipulate model behaviour under a defined threat model.

### E. Spatial validation and distribution shift

Review:
- Spatial autocorrelation.
- Spatial block cross-validation.
- Geographic holdout validation.
- Survey-to-survey domain shift.
- Temporal shifts in observations.
- Resolution-induced distribution shift.
- External validation on a second study area.

Randomly splitting adjacent raster cells is not an adequate primary validation strategy because neighbouring cells can be strongly correlated.

### F. Environmental performance disparity

Use this as an evaluation concept rather than assuming conventional demographic fairness applies. Review group-robust learning, worst-group performance, spatial fairness and distributionally robust optimization. Define groups using scientifically meaningful variables such as terrain complexity, depth regime, survey quality or modality availability.

## 3. Provisional novelty assessment

| Candidate contribution | Initial assessment | Required evidence |
|---|---|---|
| ML applied to Lō‘ihi | Low novelty by itself | Prior-art review |
| Bathymetry plus gravity | Established direction | Compare recent seamount literature |
| Adding magnetic/seismic modalities | Potentially useful, not automatically novel | Verify data and search prior work |
| Multimodal anomaly detection | Broad field already exists | Identify method-specific gap |
| Resolution-mismatch benchmark | Promising | Search geophysical and remote-sensing literature |
| Sensor degradation benchmark | Promising | Define realistic error models and comparators |
| Constrained adversarial evaluation | Promising | Search adversarial geoscience literature |
| Robustness under missing modalities | Promising | Compare missing-modality literature |
| Joint robustness and environmental reliability | Potentially distinctive | Formal systematic review required |

## 4. Literature search protocol

Search combinations of the following terms in Google Scholar, Crossref, OpenAlex, IEEE Xplore, AGU/Wiley, ScienceDirect, SpringerLink and relevant conference proceedings:

- `seamount detection deep learning gravity bathymetry`
- `Loihi seamount magnetic anomaly bathymetry multibeam`
- `multimodal geophysical machine learning anomaly detection`
- `geophysical data fusion missing modality uncertainty`
- `adversarial robustness geophysical machine learning`
- `sensor degradation remote sensing deep learning robustness`
- `spatial block cross validation geoscience machine learning`
- `environmental distribution shift geospatial machine learning`
- `multimodal anomaly detection physically constrained perturbations`

For each close paper, inspect:
1. Its references.
2. Papers that cite it.
3. Related work by the same authors.
4. Dataset and code availability.
5. Whether a newer version or journal extension exists.

Record the search date, database, exact query, number of results screened and reasons for inclusion/exclusion.

## 5. Literature extraction matrix

Create a spreadsheet with these fields:

| Field | Description |
|---|---|
| Citation | Full reference and DOI |
| Year / venue | Publication details |
| Study area | Geographic setting |
| Modalities | Bathymetry, gravity, magnetics, seismicity, imagery, etc. |
| Spatial resolution | Native and model resolution |
| Method | Model and fusion strategy |
| Labels | Source and quality of reference labels |
| Validation | Random, spatial, temporal, external |
| Robustness | Degradation or adversarial tests |
| Metrics | Reported evaluation |
| Limitations | Author-stated and reviewer-identified |
| Relevance | Direct, adjacent or background |

## 6. Novelty statement — provisional wording

A defensible provisional statement is:

> This study investigates the reliability of multimodal geophysical anomaly detection under heterogeneous spatial resolution, incomplete modality coverage and constrained measurement perturbations. Using Lō‘ihi Seamount as a case study, it evaluates the contribution of individual geophysical modalities, quantifies sensitivity to data degradation and tests whether modality-aware training improves prediction stability across spatially separated environmental regimes.

Do not use “first”, “novel” or “state-of-the-art” in the final paper unless the literature review and comparative experiments support those claims.

## 7. Starting references and repositories

- GEBCO: https://www.gebco.net/
- NOAA NCEI: https://www.ncei.noaa.gov/
- NOAA marine gravity: https://www.ngdc.noaa.gov/mgg/gravity/
- NOAA marine geophysics: https://www.ngdc.noaa.gov/mgg/gdas/
- NOAA multibeam: https://www.ngdc.noaa.gov/mgg/bathymetry/multibeam/
- Marine Geoscience Data System: https://www.marine-geo.org/
- USGS earthquake catalog: https://earthquake.usgs.gov/fdsnws/event/1/
- AGU publications: https://agupubs.onlinelibrary.wiley.com/
- JGR: Machine Learning and Computation: https://agupubs.onlinelibrary.wiley.com/journal/28344592
- Remote Sensing: https://www.mdpi.com/journal/remotesensing
- IEEE Xplore: https://ieeexplore.ieee.org/

The team should verify exact titles, authors, publication years and DOIs before using any reference in the manuscript.
