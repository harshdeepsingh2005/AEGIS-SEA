# 08 — Adversarial Threat Model and Defenses

## 1. Purpose

Evaluate whether geophysical anomaly detectors are sensitive to input degradation and whether model-directed perturbations can manipulate their outputs. This is a scientific robustness study, not a claim that real-world attackers are targeting the seamount data.

## 2. Separate two experiment families

### Family A — Measurement degradation
Represents plausible data-quality issues:
- Random noise based on documented uncertainty.
- Constant or spatially varying bias.
- Missing observations.
- Trackline gaps.
- Spatial smoothing.
- Resolution reduction.
- Coordinate perturbation within documented navigation uncertainty.
- Temporal sampling differences.

### Family B — Adversarial attacks
Perturbations are selected to change model outputs under a defined threat model. They must be constrained by:
- Modality-specific units.
- Plausible magnitude bounds.
- Spatial smoothness or support constraints where appropriate.
- Validity masks.
- Physical or instrument-derived limits.
- A stated attacker knowledge assumption.

Do not call arbitrary Gaussian noise an adversarial attack.

## 3. Threat-model specification

For every attack, document:

| Field | Required definition |
|---|---|
| Attacker knowledge | White-box, score-based black-box or transfer |
| Accessible inputs | Which modalities can be changed |
| Spatial support | Single cell, patch, trackline or region |
| Perturbation budget | Numerical bound and units |
| Smoothness | Whether neighbouring perturbations are constrained |
| Validity | Must values remain within plausible data bounds? |
| Objective | Increase/decrease score, alter ranking or hide a reference feature |
| Success criterion | Pre-defined quantitative change |
| Evaluation set | Held-out spatial blocks only |

## 4. Proposed experiments

- A1: gravity noise/bias degradation.
- A2: magnetic noise/bias degradation, if data are available.
- A3: bathymetry depth perturbation and resolution reduction.
- A4: seismic-event omission or location uncertainty.
- A5: single-modality missingness.
- A6: multi-modality missingness.
- A7: model-directed single-modality perturbation.
- A8: model-directed multi-modality perturbation.

Each experiment needs a clean-input control and a matched non-targeted degradation control.

## 5. Defense candidates

### Defense A — Modality dropout
Train with selected modalities masked to reduce reliance on a single source.

### Defense B — Uncertainty-aware fusion
Reduce the influence of a modality when its uncertainty or coverage quality indicates low reliability.

### Defense C — Adversarial training
Train on clean and constrained perturbed examples. Define the attack generation procedure and training budget.

### Defense D — Robust score aggregation
Compare per-modality scores and avoid allowing one unreliable modality to dominate without evidence.

Do not implement every defense at once. Test them independently before combining them.

## 6. Loss-function concept

A candidate objective is:

`L_total = L_reconstruction + lambda_adv * L_adv + lambda_cons * L_consistency + lambda_reg * L_regularization`

Where:
- `L_reconstruction` measures reconstruction quality.
- `L_adv` penalizes undesirable behaviour under the defined perturbation set.
- `L_consistency` encourages stable outputs under acceptable transformations.
- `L_regularization` controls model complexity.

The exact objective must match the model and threat model. Do not add a group-fairness penalty simply because it sounds desirable. First establish a measurable environmental performance disparity and define a scientifically appropriate objective.

## 7. Evaluation

Report:
- Clean-input performance.
- Degraded-input performance.
- Adversarial-input performance.
- Relative performance drop.
- Anomaly-score change.
- Rank correlation between clean and perturbed outputs.
- Reference-feature ranking changes.
- Worst-stratum results.
- Uncertainty behaviour.
- Defense cost and clean-data trade-off.

For labeled reference features, use suitable detection metrics. For unlabeled regions, use score stability and expert-reviewed interpretation rather than invented accuracy.

## 8. Important limitations

- A synthetic perturbation is not proof of a naturally occurring geophysical process.
- An attack on a model may exploit model-specific weaknesses.
- Sensor error bounds must come from instrument documentation or justified empirical estimates.
- A defense may improve robustness to tested attacks but fail against unseen perturbations.
- Report the exact attack budget; never describe a model as universally robust.

## 9. Safety and research integrity

The work is intended to evaluate scientific data and model reliability. Do not alter public source datasets or publish manipulated data as authentic measurements. Store all synthetic and adversarial variants separately, clearly labelled and reproducible.
