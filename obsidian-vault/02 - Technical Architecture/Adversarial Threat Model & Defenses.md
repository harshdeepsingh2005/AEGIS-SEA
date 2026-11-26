---
tags:
  - technical-architecture
  - adversarial
  - robustness
  - threat-model
source: Aegis-Sea_Research_Documentation/SET_2_TECHNICAL_ARCHITECTURE/08_adversarial_threat_model_and_defenses.md
created: 2026-11-26
---

# Adversarial Threat Model and Defenses

> [!NOTE] Source
> Distilled from `08_adversarial_threat_model_and_defenses.md`. Parent: [[MOC - Technical Architecture]].

> [!IMPORTANT] Core Distinction
> Never call arbitrary Gaussian noise an adversarial attack. Separate **Family A (Measurement degradation)** from **Family B (Adversarial attacks)**, and store all synthetic/adversarial variants separately from authentic public datasets.

## 1. Two Experiment Families
- **Family A — Measurement degradation:** Random noise (from documented uncertainty), constant/spatially varying bias, missing observations, trackline gaps, spatial smoothing, resolution reduction, coordinate perturbation (within navigation uncertainty), temporal sampling differences.
- **Family B — Adversarial attacks:** Model-directed perturbations constrained by modality-specific units, plausible magnitude bounds, spatial smoothness/support, validity masks, physical/instrumental limits, and stated attacker knowledge.

## 2. Nine-Field Threat-Model Specification
For every attack, document: `Attacker knowledge` (white-box / score-based black-box / transfer), `Accessible inputs`, `Spatial support` (cell / patch / trackline / region), `Perturbation budget` (value + units), `Smoothness`, `Validity` (within plausible data bounds), `Objective` (raise/lower score, alter ranking, hide reference feature), `Success criterion`, and `Evaluation set` (held-out spatial blocks only).

## 3. Proposed Experiments (A1–A8)
- **A1:** Gravity noise/bias degradation
- **A2:** Magnetic noise/bias degradation *(if data available)*
- **A3:** Bathymetry depth perturbation & resolution reduction
- **A4:** Seismic-event omission or location uncertainty
- **A5:** Single-modality missingness
- **A6:** Multi-modality missingness
- **A7:** Model-directed single-modality perturbation
- **A8:** Model-directed multi-modality perturbation

Each needs both a **clean-input control** and a **matched non-targeted degradation control**.

## 4. Four Defense Candidates (A–D)
- **Defense A — Modality dropout:** Mask modalities during training to reduce single-source reliance.
- **Defense B — Uncertainty-aware fusion:** Down-weight modalities with high uncertainty or poor coverage.
- **Defense C — Adversarial training:** Train on clean + constrained perturbed examples.
- **Defense D — Robust score aggregation:** Compare per-modality scores so one unreliable modality cannot dominate.
*(Test defenses independently before combining them.)*

## 5. Candidate Loss Function
$$L_{\text{total}} = L_{\text{reconstruction}} + \lambda_{\text{adv}} L_{\text{adv}} + \lambda_{\text{cons}} L_{\text{consistency}} + \lambda_{\text{reg}} L_{\text{regularization}}$$
Do not add a group-fairness penalty without first establishing a measurable environmental performance disparity.

## 6. Evaluation & Limitations
Report clean/degraded/adversarial performance, relative drop, score & rank displacement, reference-feature ranking changes, worst-stratum results, uncertainty behavior, and defense clean-data trade-off. Never describe a model as "universally robust"—always state exact attack budgets and tested constraints.

