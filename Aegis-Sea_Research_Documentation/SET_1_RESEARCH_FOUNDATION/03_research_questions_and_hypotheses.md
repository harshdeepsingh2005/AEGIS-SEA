# 03 — Research Questions, Hypotheses and Contributions

## 1. Primary research question

How reliably can multimodal machine-learning systems identify geologically meaningful seafloor anomalies when geophysical observations have heterogeneous spatial resolution, incomplete coverage, measurement uncertainty and constrained perturbations?

## 2. Research questions

### RQ1 — Multimodal value
Does combining available geophysical modalities improve anomaly ranking or geological-reference agreement compared with individual modalities?

### RQ2 — Resolution mismatch
How does the mismatch between native data resolution and analysis-grid resolution affect anomaly scores and validation performance?

### RQ3 — Missing and degraded modalities
How sensitive are model outputs to missing, noisy, biased, smoothed or spatially degraded input modalities?

### RQ4 — Adversarial vulnerability
Can model-directed perturbations, constrained by plausible measurement or geophysical bounds, manipulate anomaly scores or rankings?

### RQ5 — Robust defense
Can modality dropout, uncertainty-aware fusion and/or adversarial training improve performance stability under the defined degradation and attack scenarios?

### RQ6 — Spatial generalization
Do model outputs and evaluation results remain stable across spatially separated regions with different terrain complexity, depth and survey quality?

## 3. Hypotheses

Hypotheses must be testable and may be rejected.

**H1:** A multimodal model will provide better agreement with independent geological reference evidence than at least some single-modality baselines.

**H2:** Performance and anomaly-score stability will degrade when high-resolution inputs are downsampled or when coarse modalities are represented as if they had fine spatial resolution.

**H3:** Missing or degraded modalities will produce measurable changes in anomaly ranking, score calibration or reference agreement.

**H4:** A model-directed perturbation within the pre-defined threat budget can change anomaly scores more than a comparable non-targeted perturbation in at least some test conditions.

**H5:** A robustness intervention will reduce degradation under at least one pre-specified stress test without causing an unacceptable loss on clean validation data.

**H6:** Results will vary across spatial/environmental strata, demonstrating that evaluation on randomly split neighbouring cells is insufficient.

Do not write these hypotheses as expected findings. Report outcomes whether positive, negative or inconclusive.

## 4. Operational definitions

### Geophysical anomaly
A location or region assigned an unusual score by a specified statistical or machine-learning detector relative to its training reference distribution. This is a statistical definition, not proof of geological novelty.

### Geological reference feature
A feature independently documented by published mapping, survey observations or expert interpretation. Its spatial footprint, confidence and source must be recorded.

### Measurement degradation
A controlled transformation intended to simulate a data-quality issue, such as noise, bias, missingness, smoothing or resolution reduction.

### Adversarial perturbation
A model-directed input modification designed to change a prediction or anomaly score while remaining within an explicitly defined constraint set.

### Environmental stratum
A pre-defined evaluation subset based on measurable conditions such as terrain complexity, depth, survey quality or modality availability.

### Robustness
The degree to which model outputs, rankings or validation performance remain stable under specified input changes.

## 5. Primary and secondary outcomes

### Primary outcomes
Choose a small number before experiments:
- Agreement with independent geological reference evidence, where labels exist.
- Anomaly-ranking stability under degradation.
- Performance degradation relative to clean inputs.
- Worst-stratum performance.

### Secondary outcomes
- AUROC and AUPRC, only when valid reference labels exist.
- Precision@K and recall@K.
- Spatial overlap with reference features.
- Score correlation and rank correlation between clean and perturbed inputs.
- Calibration error, where a valid probability interpretation exists.
- Uncertainty/error association.
- Runtime and memory use.

## 6. Proposed contributions

1. A documented geophysical data-preparation and quality-metadata workflow for Lō‘ihi.
2. A comparative evaluation of single-modality and multimodal anomaly detection.
3. A controlled benchmark of spatial-resolution mismatch and modality degradation.
4. A constrained adversarial evaluation protocol for geophysical inputs.
5. An assessment of modality-aware robustness interventions.
6. A spatially separated validation and reporting framework.

These are intended contributions. The final manuscript must state only those supported by completed work.

## 7. Claims the paper must avoid

- “The model predicts eruptions.”
- “Every high anomaly score is a new geological feature.”
- “The model is fair” without defining the fairness concept and evidence.
- “The model is robust” without naming the tested perturbations and bounds.
- “The model generalizes globally” based on one seamount.
- “The grid has 250 m resolution” when one or more source modalities are much coarser or irregularly sampled.
