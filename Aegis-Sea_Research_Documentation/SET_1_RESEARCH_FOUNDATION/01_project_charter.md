# 01 — Project Charter

## 1. Project identity

**Project name:** Aegis-Sea 2.0  
**Working paper title:** *Reliability and Adversarial Robustness of Multimodal Geophysical Anomaly Detection Under Spatial and Sensor Uncertainty: A Case Study of Lō‘ihi Seamount*

**Study area:** Lō‘ihi Seamount, southeast of Hawaiʻi Island, USA.  
**Research domains:** Marine geophysics, geospatial machine learning, unsupervised anomaly detection, robustness and uncertainty evaluation.

## 2. Problem statement

Marine geophysical datasets are heterogeneous. Bathymetry, gravity, magnetic measurements, multibeam surveys and earthquake catalogs differ in spatial resolution, sampling geometry, observation period, uncertainty and geographic coverage. A machine-learning model trained on a fused representation may therefore learn relationships that are partly driven by survey density, interpolation, missingness or sensor-specific artifacts rather than geological structure.

A model may also produce unstable anomaly scores when one modality is degraded, missing, resampled or perturbed. These reliability issues are important if anomaly scores are to support scientific exploration.

This project will investigate the reliability of multimodal geophysical anomaly detection under realistic data-quality variation and controlled adversarial perturbations.

## 3. Primary research objective

Develop and evaluate a reproducible multimodal geophysical anomaly-detection workflow for Lō‘ihi Seamount, then quantify how spatial-resolution mismatch, incomplete modality coverage, measurement degradation and constrained adversarial perturbations affect model outputs. Evaluate whether modality-aware training and uncertainty-aware inference improve reliability.

## 4. Scope

### In scope
- Publicly accessible geophysical datasets relevant to Lō‘ihi.
- Bathymetry as the primary spatial foundation.
- Gravity and magnetic data where suitable observations can be verified.
- Multibeam survey products and coverage metadata.
- Earthquake catalogs as auxiliary, temporally qualified features.
- Quality masks, source-resolution metadata and spatial uncertainty.
- Classical and neural anomaly-detection baselines.
- Multimodal feature fusion.
- Missing-modality and measurement-degradation experiments.
- Physically or instrumentally constrained adversarial perturbations.
- Spatially separated validation.
- Independent geological interpretation where reference evidence exists.

### Out of scope unless separately approved
- Predicting volcanic eruptions.
- Claiming real-time volcanic hazard forecasting.
- Treating anomaly scores as proof of geological novelty.
- Claiming global seamount generalization from one study area.
- Fabricating labels or converting synthetic labels into real-world ground truth.
- Treating every data-quality failure as a malicious adversarial attack.
- Building an operational marine navigation or hazard-warning product.

## 5. Study-area rationale

Lō‘ihi is a submarine volcanic environment with documented volcanic morphology, rift structures, hydrothermal areas and seismic activity. It is a useful case study because published geological mapping and research observations can provide contextual evidence for interpreting model outputs.

The study area is not automatically representative of all seamounts. Any broader generalization claim requires independent validation on another suitable region.

## 6. Intended research contribution

The intended contribution is a reproducible evaluation framework answering:

1. Whether multimodal fusion provides value over individual geophysical modalities.
2. How resolution mismatch and incomplete coverage affect anomaly scores.
3. How realistic measurement degradation affects model reliability.
4. Whether constrained model-directed perturbations can manipulate predictions.
5. Whether modality-aware training and uncertainty estimation improve reliability.
6. Whether results remain stable across spatially separated geological and survey-quality regimes.

The novelty of these contributions is provisional and must be established through a systematic literature search.

## 7. Success criteria

The project is successful if it:
- Produces a documented data inventory and coverage assessment.
- Preserves original data and provenance.
- Builds a reproducible spatial processing pipeline.
- Establishes meaningful baseline models.
- Uses spatially separated evaluation rather than relying only on random cell splits.
- Defines realistic degradation and adversarial threat models.
- Reports uncertainty and limitations.
- Uses independent reference evidence when making geological claims.
- Produces a complete manuscript with reproducible methods and honest results.

A higher-performing proposed model is desirable, but a carefully designed negative result can also be publishable if it answers the research questions rigorously.

## 8. Key risks

| Risk | Consequence | Mitigation |
|---|---|---|
| Sparse magnetic coverage | Full multimodal fusion may be infeasible | Use modality availability masks; reduce scope transparently |
| Coarse gravity data | False impression of fine-scale information | Preserve native resolution and metadata |
| Incomplete earthquake detection | Biased seismicity features | Treat as auxiliary and uncertainty-qualified |
| Weak reference labels | Cannot report standard detection metrics | Use expert/reference validation and score-stability metrics |
| Spatial leakage | Inflated performance | Use spatial blocks and held-out regions |
| Unrealistic attacks | Weak scientific conclusions | Constrain perturbations using documented error models |
| Overambitious scope | Incomplete experiments | Prioritize data feasibility and core experiments |

## 9. Decision gates

**Gate 1 — Data feasibility:** establish geographic overlap, temporal compatibility, resolution and usable coverage.

**Gate 2 — Validation feasibility:** identify independent geological reference evidence and define what constitutes an anomaly.

**Gate 3 — Baseline feasibility:** demonstrate that the data pipeline and at least two baseline detectors work.

**Gate 4 — Robustness feasibility:** define realistic degradation ranges and a valid adversarial threat model.

Do not proceed to full defense-model development until Gates 1–3 have been passed.
