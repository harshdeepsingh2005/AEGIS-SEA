---
tags:
  - execution
  - reproducibility
  - checklist
source: Aegis-Sea_Research_Documentation/SET_3_EXECUTION_AND_EXPERIMENTS/12_reproducibility_and_publication_checklist.md
created: 2026-11-26
---

# Reproducibility and Publication Checklist

> [!NOTE] Source
> Distilled from `12_reproducibility_and_publication_checklist.md`. Parent: [[MOC - Execution & Paper]].

## 1. Seven Verification Domains (All Currently Unchecked)
1. **Data provenance:** Stable URL/ID, download date/version, cruise/survey ID, acquisition dates, native CRS/units, native vs. effective resolution, uncertainty, licence, checksums, raw data unchanged.
2. **Geospatial processing:** Versioned boundary, documented CRS transforms, justified resampling/interpolation, retained coverage masks, no silent zero-imputation, documented temporal mismatches, saved spatial split maps, leakage checks.
3. **Model reproducibility:** Documented architecture, hyperparameters, random seeds, pinned package versions, saved train/val/test assignments, train-only normalization/imputation, versioned checkpoints, failed runs logged, clean-env inference.
4. **Robustness experiments:** Degradation separated from adversarial attacks, documented rationale/units/budgets/spatial support/smoothness, clean & matched non-targeted controls, pre-defined attack success criteria, defense clean-data trade-offs, threat-model limitations.
5. **Validation & statistics:** Independent reference sources, documented reference geometry/confidence, synthetic refs separated, label-appropriate metrics, spatial dependence in CIs, multi-seed/multi-split, effect sizes + CIs, negative results included, no fabricated values.
6. **Manuscript integrity:** Literature-backed novelty claims, verified citations, regenerable figures, explicit dataset limitations, no anomaly=discovery or eruption-prediction claims, matching generalization claims, author approval, venue compliance.
7. **Final release contents:** README, env spec, data inventory/retrieval scripts, processing/model/eval/figure scripts, configs, checkpoints (if permitted), logs, supplementary methods, licence/citation instructions.

## 2. Six Final Scientific Sign-Off Questions
Before submission, every member must independently answer:
1. What is the precise research gap?
2. What is the strongest competing method?
3. What evidence supports the claimed contribution?
4. What are the most important failure cases?
5. What cannot be concluded from this study?
6. Could another team reproduce the central results?

