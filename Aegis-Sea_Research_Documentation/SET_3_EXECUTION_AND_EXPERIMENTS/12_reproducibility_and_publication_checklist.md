# 12 — Reproducibility and Publication Checklist

## 1. Data provenance

- [ ] Every dataset has a stable source URL or catalogue identifier.
- [ ] Download date and source version are recorded.
- [ ] Survey/cruise identifiers are recorded where applicable.
- [ ] Acquisition dates are recorded.
- [ ] Native CRS and units are documented.
- [ ] Native and effective resolution are distinguished.
- [ ] Measurement uncertainty is recorded where available.
- [ ] Licence and redistribution conditions are checked.
- [ ] Checksums are stored.
- [ ] Raw data remain unchanged.

## 2. Geospatial processing

- [ ] Study-area boundary is versioned.
- [ ] Coordinate transformations are documented.
- [ ] Resampling choices are justified.
- [ ] Interpolation is documented.
- [ ] Per-modality coverage masks are retained.
- [ ] Missingness is not silently converted to zero.
- [ ] Temporal mismatches are documented.
- [ ] Spatial split maps are saved.
- [ ] Leakage checks are completed.

## 3. Model reproducibility

- [ ] Model architecture is documented.
- [ ] All hyperparameters are recorded.
- [ ] Random seeds are recorded.
- [ ] Software and package versions are pinned.
- [ ] Training/validation/test assignments are saved.
- [ ] Normalization and imputation are fitted on training data only.
- [ ] Model checkpoints are versioned.
- [ ] Failed runs are retained in experiment logs.
- [ ] Inference can be reproduced from a clean environment.

## 4. Robustness experiments

- [ ] Measurement degradation is separated from adversarial attacks.
- [ ] Every perturbation has a documented rationale.
- [ ] Perturbation units and budgets are specified.
- [ ] Spatial support and smoothness constraints are specified.
- [ ] Clean controls are included.
- [ ] Matched non-targeted controls are included.
- [ ] Attack success criteria are pre-defined.
- [ ] Defense trade-offs on clean data are reported.
- [ ] Limitations of the tested threat model are stated.

## 5. Validation and statistics

- [ ] Geological reference sources are independent of model training.
- [ ] Reference geometries and confidence are documented.
- [ ] Synthetic references are reported separately.
- [ ] Metrics match the availability and quality of labels.
- [ ] Spatial dependence is considered in uncertainty intervals.
- [ ] Multiple seeds or repeated spatial splits are used where feasible.
- [ ] Effect sizes and confidence intervals are reported.
- [ ] Negative results are included.
- [ ] No fabricated performance values are present.

## 6. Manuscript integrity

- [ ] Novelty claims are supported by a documented literature search.
- [ ] All citations have been checked against source records.
- [ ] Figures can be regenerated.
- [ ] Dataset limitations are explicit.
- [ ] No anomaly score is presented as proof of a geological discovery.
- [ ] No eruption-prediction claim is made.
- [ ] Generalization claims match the validation design.
- [ ] All authors approve the final manuscript.
- [ ] Target venue requirements are followed.

## 7. Final release contents

Recommended release:
- README and environment specification.
- Data inventory and retrieval instructions.
- Data-processing code.
- Configuration files.
- Model code and checkpoints where permitted.
- Experiment logs.
- Evaluation scripts.
- Figure-generation scripts.
- Supplementary methods.
- Licence and citation instructions.

If source datasets cannot legally be redistributed, release retrieval scripts, metadata, checksums and instructions instead.

## 8. Final scientific sign-off

Before submission, each member should independently answer:

1. What is the precise research gap?
2. What is the strongest competing method?
3. What evidence supports the claimed contribution?
4. What are the most important failure cases?
5. What cannot be concluded from this study?
6. Could another team reproduce the central results?

If the team cannot answer these questions, the manuscript is not ready.
