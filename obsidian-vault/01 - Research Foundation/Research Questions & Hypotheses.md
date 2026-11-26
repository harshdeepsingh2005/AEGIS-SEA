---
tags:
  - research-foundation
  - research-questions
  - hypotheses
source: Aegis-Sea_Research_Documentation/SET_1_RESEARCH_FOUNDATION/03_research_questions_and_hypotheses.md
created: 2026-11-26
---

# Research Questions & Hypotheses

> [!NOTE] Source
> Distilled from `03_research_questions_and_hypotheses.md`. Parent: [[MOC - Research Foundation]].

## 1. Primary Research Question
> How reliably can multimodal machine-learning systems identify geologically meaningful seafloor anomalies when geophysical observations have heterogeneous spatial resolution, incomplete coverage, measurement uncertainty and constrained perturbations?

## 2. Six Research Questions & Testable Hypotheses

| ID | Focus | Hypothesis |
|---|---|---|
| **RQ1 / H1** | **Multimodal value** | Multimodal model provides better agreement with independent geological reference evidence than at least some single-modality baselines. |
| **RQ2 / H2** | **Resolution mismatch** | Performance and score stability degrade when high-res inputs are downsampled or coarse modalities are represented as fine-resolution. |
| **RQ3 / H3** | **Missing & degraded modalities** | Missing or degraded modalities produce measurable changes in anomaly ranking, calibration, or reference agreement. |
| **RQ4 / H4** | **Adversarial vulnerability** | Model-directed perturbations within the threat budget change anomaly scores more than comparable non-targeted perturbations in some conditions. |
| **RQ5 / H5** | **Robust defense** | Robustness interventions (modality dropout, uncertainty-aware fusion, adversarial training) reduce degradation under $\ge 1$ stress test without unacceptable clean loss. |
| **RQ6 / H6** | **Spatial generalization** | Results vary across spatial/environmental strata, showing random cell-level splits are insufficient. |

All hypotheses may be rejected; outcomes must be reported whether positive, negative, or inconclusive.

## 3. Operational Definitions
- **Geophysical anomaly:** Statistical unusualness relative to training reference distribution—**not** proof of geological novelty.
- **Geological reference feature:** Independently documented feature (published map, survey, expert interpretation) with recorded spatial footprint, confidence, and source.
- **Measurement degradation:** Controlled transformation simulating data-quality issues (noise, bias, missingness, smoothing, resolution reduction).
- **Adversarial perturbation:** Model-directed input modification under an explicit constraint set.
- **Environmental stratum:** Pre-defined evaluation subset (terrain complexity, depth regime, survey quality, modality availability).
- **Robustness:** Stability of outputs, rankings, or validation performance under specified input changes.

## 4. Outcomes
- **Primary:** Agreement with independent geological reference evidence (where labels exist), anomaly-ranking stability under degradation, performance drop vs. clean, worst-stratum performance.
- **Secondary:** AUROC/AUPRC (only with valid reference labels), Precision@K / Recall@K, spatial overlap, score/rank correlation, calibration error, uncertainty/error association, runtime & memory.

## 5. Claims the Paper Must Avoid
- "The model predicts eruptions."
- "Every high anomaly score is a new geological feature."
- "The model is fair" (without defining fairness concept and evidence).
- "The model is robust" (without naming tested perturbations and bounds).
- "The model generalizes globally" (based on one seamount).
- "The grid has 250 m resolution" (when a source modality is much coarser or irregularly sampled).

