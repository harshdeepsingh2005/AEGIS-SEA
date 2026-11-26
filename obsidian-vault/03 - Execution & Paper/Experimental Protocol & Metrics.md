---
tags:
  - execution
  - experiments
  - metrics
source: Aegis-Sea_Research_Documentation/SET_3_EXECUTION_AND_EXPERIMENTS/09_experimental_protocol_and_metrics.md
created: 2026-11-26
---

# Experimental Protocol and Metrics

> [!NOTE] Source
> Distilled from `09_experimental_protocol_and_metrics.md`. Parent: [[MOC - Execution & Paper]].

## 1. General Rules
Predefine experiments before inspecting test results; use spatially separated train/val/test blocks; fit preprocessing on training data only; repeat stochastic models with multiple seeds; report CIs (block bootstrap); preserve failed runs and negative findings; separate synthetic-reference validation from real geological validation.

## 2. Core Experiment Matrix (E1–E14)
| ID | Experiment | Main Question |
|---|---|---|
| **E1** | Bathymetry-only baseline | What can terrain alone detect? |
| **E2** | Gravity-only baseline | What information does gravity contribute? |
| **E3** | Magnetic-only baseline | Is magnetic info usable and informative? *(only if feasibility passes)* |
| **E4** | Other usable modality baselines | What is the individual contribution? |
| **E5** | Early-fusion baseline | Does simple feature concatenation help? |
| **E6** | Multimodal model | Does learned fusion help? |
| **E7** | Modality ablation | Which inputs drive the result? |
| **E8** | Resolution degradation | How sensitive is the model to resampling? |
| **E9** | Missing modality | What happens when an input is unavailable? |
| **E10** | Measurement degradation | How do realistic data-quality changes affect outputs? |
| **E11** | Adversarial attack | Can constrained model-directed inputs manipulate scores? |
| **E12** | Defense comparison | Which intervention improves robustness? |
| **E13** | Spatial holdout | Does performance transfer to unseen spatial blocks? |
| **E14** | Environmental strata | Does reliability vary by terrain, depth, or coverage? |

## 3. Evaluation Metrics
- **When reference labels exist:** Precision, Recall/TPR, FPR, FNR, F1, AUROC, AUPRC, Precision@K, Recall@K, IoU/spatial overlap.
- **When reference labels do NOT exist:** Score stability under controlled transformations, rank correlation (clean vs. perturbed), reconstruction error distributions, detector agreement, spatial coherence (without rewarding oversmoothing), expert-reviewed agreement with published features. *Never present unsupervised metrics as geological ground truth.*
- **Robustness metrics:** Absolute/relative performance drop, score displacement, rank displacement, feature-level sensitivity, worst-case performance within budget, recovery under defense.
- **Environmental reliability strata:** Terrain complexity, depth regime, survey coverage/quality, modality availability (report sample count, spatial extent, metric estimate, uncertainty, worst-group).

## 4. Reference-Feature Catalogue & Required Figures
- **Reference catalogue fields:** Feature ID, Name, Geometry, Reference source, Survey date, Positional uncertainty, Confidence level, Feature type, Inclusion rationale. *(A polygon does not label every cell inside it as anomalous.)*
- **12 Required Figures:** (1) Study-area map & boundary, (2) Per-modality coverage, (3) Native-resolution comparison, (4) Data-quality & missingness, (5) Spatial train/val/test split, (6) Single-modality vs. fusion, (7) Resolution-degradation curves, (8) Missing-modality results, (9) Attack/defense curves, (10) Environmental-stratum performance, (11) Geological interpretation with uncertainty, (12) Ablation results.
- **Results table:** Currently all `TBD` across Isolation Forest, PCA reconstruction, Dense Autoencoder, Feature fusion, Multimodal model, Robust multimodal model.

