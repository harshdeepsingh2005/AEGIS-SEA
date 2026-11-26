# 09 — Experimental Protocol and Metrics

## 1. General rules

- Predefine experiments before inspecting final test results.
- Use spatially separated train/validation/test regions.
- Fit preprocessing on training data only.
- Repeat stochastic models with multiple seeds.
- Report confidence intervals where appropriate.
- Preserve failed runs and negative findings.
- Separate synthetic-reference evaluation from real geological validation.

## 2. Core experiment matrix

| ID | Experiment | Main question |
|---|---|---|
| E1 | Bathymetry-only baseline | What can terrain alone detect? |
| E2 | Gravity-only baseline | What information does gravity contribute? |
| E3 | Magnetic-only baseline | Is magnetic information usable and informative? |
| E4 | Other usable modality baselines | What is the individual contribution? |
| E5 | Early-fusion baseline | Does simple feature concatenation help? |
| E6 | Multimodal model | Does learned fusion help? |
| E7 | Modality ablation | Which inputs drive the result? |
| E8 | Resolution degradation | How sensitive is the model to resampling? |
| E9 | Missing modality | What happens when an input is unavailable? |
| E10 | Measurement degradation | How do realistic data-quality changes affect outputs? |
| E11 | Adversarial attack | Can constrained model-directed inputs manipulate scores? |
| E12 | Defense comparison | Which intervention improves robustness? |
| E13 | Spatial holdout | Does performance transfer to unseen spatial blocks? |
| E14 | Environmental strata | Does reliability vary by terrain, depth or coverage? |

Only run magnetic experiments if suitable magnetic data pass the feasibility checks.

## 3. Metrics

### When reference labels are available
- Precision.
- Recall / true positive rate.
- False positive rate.
- False negative rate.
- F1-score.
- AUROC.
- AUPRC.
- Precision@K and recall@K.
- Intersection over Union or spatial overlap, where reference polygons are suitable.

### When reference labels are not available
- Score stability under controlled transformations.
- Rank correlation between clean and perturbed inputs.
- Reconstruction error distributions.
- Detector agreement.
- Spatial coherence, with care not to reward oversmoothing.
- Expert-reviewed agreement with published geological features.

Unsupervised metrics must not be presented as substitutes for geological ground truth.

### Robustness metrics
- Absolute and relative performance degradation.
- Score displacement.
- Rank displacement.
- Feature-level sensitivity.
- Worst-case performance within the defined perturbation budget.
- Recovery under defense.

### Environmental reliability metrics
Define strata before final evaluation:
- Terrain complexity.
- Depth regime.
- Survey coverage/quality.
- Modality availability.

For each stratum, report sample count, spatial extent, metric estimate and uncertainty. Report worst-group performance and disparity only when the metric is valid for that group.

## 4. Statistical analysis

Possible methods:
- Bootstrap confidence intervals using spatial blocks rather than treating all neighbouring cells as independent.
- Paired comparisons on the same held-out blocks.
- Multiple random seeds.
- Effect sizes and uncertainty intervals.
- Sensitivity analysis over thresholds and perturbation budgets.

Choose tests based on the actual data distribution and experimental design. Avoid reporting p-values without checking assumptions and practical effect size.

## 5. Spatial validation

Recommended:
1. Create spatial blocks.
2. Assign blocks to train, validation and test.
3. Check that neighbouring blocks do not create severe leakage.
4. Tune only on validation blocks.
5. Evaluate once on held-out test blocks.
6. Repeat with alternative block partitions if feasible.

If an independent second seamount is available, treat it as external validation, not as another random split.

## 6. Reference-feature evaluation

Create a reference catalogue with:
- Feature ID.
- Name.
- Geometry.
- Reference source.
- Survey date.
- Positional uncertainty.
- Confidence level.
- Feature type.
- Inclusion rationale.

A published feature polygon may be used to assess whether it appears among high-scoring regions, but it does not automatically label every cell inside it as anomalous.

## 7. Required figures

1. Study-area map and boundary.
2. Per-modality coverage map.
3. Native-resolution comparison.
4. Data-quality and missingness maps.
5. Spatial train/validation/test split.
6. Single-modality versus fusion comparison.
7. Resolution-degradation curves.
8. Missing-modality results.
9. Attack/defense performance curves.
10. Environmental-stratum performance.
11. Geological interpretation map with uncertainty.
12. Ablation results.

## 8. Results table template

| Model | Clean metric | Degraded metric | Attack metric | Worst-stratum metric | Uncertainty |
|---|---:|---:|---:|---:|---|
| Isolation Forest | TBD | TBD | TBD | TBD | TBD |
| PCA reconstruction | TBD | TBD | TBD | TBD | TBD |
| Dense Autoencoder | TBD | TBD | TBD | TBD | TBD |
| Feature fusion | TBD | TBD | TBD | TBD | TBD |
| Multimodal model | TBD | TBD | TBD | TBD | TBD |
| Robust multimodal model | TBD | TBD | TBD | TBD | TBD |

Never fill this table with illustrative or fabricated values.
