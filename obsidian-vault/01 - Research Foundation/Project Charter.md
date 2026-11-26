---
tags:
  - research-foundation
  - charter
  - scope
source: Aegis-Sea_Research_Documentation/SET_1_RESEARCH_FOUNDATION/01_project_charter.md
created: 2026-11-26
---

# Project Charter

> [!NOTE] Source
> Distilled from `01_project_charter.md` (controlling scope document). Parent: [[MOC - Research Foundation]].

## 1. Identity
- **Project name:** Aegis-Sea 2.0
- **Working paper title:** *Reliability and Adversarial Robustness of Multimodal Geophysical Anomaly Detection Under Spatial and Sensor Uncertainty: A Case Study of Lō‘ihi Seamount*
- **Study area:** Lō‘ihi Seamount, southeast of Hawaiʻi Island, USA.
- **Domains:** Marine geophysics, geospatial ML, unsupervised anomaly detection, robustness & uncertainty evaluation.

## 2. Problem Statement & Primary Objective
Marine geophysical datasets (bathymetry, gravity, magnetics, multibeam, earthquake catalogs) differ in spatial resolution, sampling geometry, observation period, uncertainty, and coverage. Fused ML models may learn survey-density, interpolation, missingness, or sensor artifacts instead of geological structure, and produce unstable anomaly scores under degradation or perturbation.

**Primary objective:** Develop and evaluate a reproducible multimodal geophysical anomaly-detection workflow for Lō‘ihi Seamount, quantify how resolution mismatch, incomplete coverage, measurement degradation, and constrained adversarial perturbations affect outputs, and test whether modality-aware training and uncertainty-aware inference improve reliability.

## 3. Scope Boundaries

| In Scope | Out of Scope (unless separately approved) |
|---|---|
| Publicly accessible geophysical datasets around Lō‘ihi | Predicting volcanic eruptions or real-time hazard forecasting |
| Bathymetry as primary spatial foundation | Treating anomaly scores as proof of geological novelty |
| Verified gravity & magnetic data; multibeam & coverage metadata | Claiming global seamount generalization from one study area |
| Earthquake catalogs as auxiliary, temporally qualified features | Fabricating labels or converting synthetic labels to ground truth |
| Quality masks, source-resolution metadata, spatial uncertainty | Treating every data-quality failure as a malicious attack |
| Classical & neural anomaly-detection baselines + multimodal fusion | Building an operational marine navigation / hazard product |
| Missing-modality, degradation, and constrained adversarial tests | — |
| Spatially separated validation & independent geological interpretation | — |

## 4. Intended Contributions (Provisional)
1. Whether multimodal fusion provides value over individual geophysical modalities.
2. How resolution mismatch and incomplete coverage affect anomaly scores.
3. How realistic measurement degradation affects model reliability.
4. Whether constrained model-directed perturbations can manipulate predictions.
5. Whether modality-aware training and uncertainty estimation improve reliability.
6. Whether results remain stable across spatially separated geological and survey-quality regimes.

## 5. Key Risks & Mitigations
- **Sparse magnetic coverage:** Use modality availability masks; drop magnetics transparently if infeasible ([[Dataset Acquisition & Feasibility]]).
- **Coarse gravity data:** Preserve native resolution and metadata; never treat pixel size as source resolution.
- **Incomplete earthquake detection:** Treat seismicity as auxiliary and uncertainty-qualified ([[Geospatial Data Pipeline]]).
- **Weak reference labels:** Use expert/reference validation and score-stability metrics rather than fabricated accuracy.
- **Spatial leakage:** Use spatial blocks and held-out regions rather than random cell splits.
- **Unrealistic attacks:** Constrain perturbations using documented error models ([[Adversarial Threat Model & Defenses]]).
- **Overambitious scope:** Prioritize data feasibility and core experiments; a rigorous negative result is publishable.

## 6. Four Decision Gates
1. **Gate 1 — Data feasibility:** Geographic overlap, temporal compatibility, resolution, usable coverage.
2. **Gate 2 — Validation feasibility:** Independent geological reference evidence & anomaly definition.
3. **Gate 3 — Baseline feasibility:** Working data pipeline + at least 2 baseline detectors.
4. **Gate 4 — Robustness feasibility:** Realistic degradation ranges & valid adversarial threat model.

> [!CAUTION]
> Do not proceed to full defense-model development until **Gates 1–3** are passed.

