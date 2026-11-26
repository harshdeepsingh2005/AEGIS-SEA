# 04 — Publication Strategy and Manuscript Plan

## 1. Recommended paper type

**Original methodological research article with a geophysical case study.**

The manuscript should introduce a reproducible evaluation methodology and report experiments. It should not be framed as a generic application of an autoencoder to a volcano.

## 2. Working title

*Reliability and Adversarial Robustness of Multimodal Geophysical Anomaly Detection Under Spatial and Sensor Uncertainty: A Case Study of Lō‘ihi Seamount*

Alternative:
*Evaluating Multimodal Geophysical Anomaly Detection Under Resolution Mismatch, Missing Data and Constrained Perturbations*

## 3. Recommended manuscript structure

1. Abstract
2. Introduction
3. Related Work
4. Study Area and Geophysical Data
5. Data Quality, Spatial Alignment and Feature Engineering
6. Anomaly Detection Models
7. Degradation and Adversarial Threat Models
8. Robustness Interventions
9. Experimental Design and Validation
10. Results
11. Discussion
12. Limitations
13. Conclusions
14. Data and Code Availability
15. References

## 4. What each section must establish

### Abstract
State the problem, study area, datasets actually used, models actually tested, experimental design, key quantitative findings and limitations. Write it last.

### Introduction
Explain why heterogeneous marine geophysical data complicate ML reliability. Identify the precise gap from the completed literature review. State research questions and contributions.

### Related Work
Cover seamount detection, multimodal geophysical ML, anomaly detection, sensor uncertainty, adversarial robustness and spatial validation. Compare methods rather than listing papers.

### Study Area and Data
Give coordinates and boundary rationale, source names, survey identifiers, acquisition dates, native resolution, coverage, processing history and uncertainty.

### Methodology
Provide enough mathematical and implementation detail to reproduce the models, feature transformations, fusion and anomaly-score calculation.

### Threat Model
Specify attacker knowledge, accessible modalities, perturbation budget, spatial support, physical/instrumental constraints and success criterion.

### Results
Report all pre-registered experiments, including negative results. Include uncertainty intervals and spatially separated evaluation.

### Discussion
Explain what results mean geologically and methodologically. Separate evidence from speculation.

### Limitations
Discuss sparse coverage, label uncertainty, survey bias, spatial dependence, transferability and synthetic perturbations.

## 5. Potential venues

These are candidates only. Verify scope, indexing, fees, review model, publication timelines and current author instructions before submission.

- IEEE International Geoscience and Remote Sensing Symposium (IGARSS): https://www.ieeeigarss.org/
- AGU meetings and publications: https://www.agu.org/
- JGR: Machine Learning and Computation: https://agupubs.onlinelibrary.wiley.com/journal/28344592
- Frontiers in Earth Science: https://www.frontiersin.org/journals/earth-science
- IEEE Access: https://ieeeaccess.ieee.org/
- Remote Sensing: https://www.mdpi.com/journal/remotesensing

Venue choice should follow the actual contribution:
- Strong geophysical interpretation: Earth-science journal/conference.
- Strong geospatial data and mapping method: remote-sensing venue.
- Strong general robustness methodology: ML/engineering venue.

## 6. Submission readiness

Before submission:
- Complete systematic novelty search.
- Verify every citation and DOI.
- Confirm data-use and redistribution licences.
- Release code and configuration files where permitted.
- Document data sources and processing.
- Include spatial validation.
- Report baselines and ablations.
- Include limitations and negative results.
- Follow the venue's authorship, ethics and reproducibility policies.
- Do not submit simultaneously to multiple journals where prohibited.
