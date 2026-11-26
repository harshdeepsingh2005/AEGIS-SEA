# Aegis-Sea 2.0 — Research Documentation

**Working title:** Reliability and Adversarial Robustness of Multimodal Geophysical Anomaly Detection Under Spatial and Sensor Uncertainty: A Case Study of Lō‘ihi Seamount

**Project type:** Original methodological research with a marine-geophysical case study  
**Team size:** Four researchers, organized into two workstreams  
**Initial planning horizon:** 12 weeks to a complete experimental manuscript draft

## Documentation map

This repository is divided into three sets.

### Set 1 — Research Foundation
1. `01_project_charter.md`
2. `02_literature_review_and_novelty.md`
3. `03_research_questions_and_hypotheses.md`
4. `04_publication_strategy.md`

### Set 2 — Technical Architecture
5. `05_dataset_acquisition_and_feasibility.md`
6. `06_geospatial_data_pipeline.md`
7. `07_model_architecture.md`
8. `08_adversarial_threat_model_and_defenses.md`

### Set 3 — Execution and Experiments
9. `09_experimental_protocol_and_metrics.md`
10. `10_team_roles_and_repository_structure.md`
11. `11_twelve_week_roadmap.md`
12. `12_reproducibility_and_publication_checklist.md`

## How to use these documents

- Treat the project charter as the controlling scope document.
- Do not start full-scale model development until the data-feasibility gates in Set 2 are passed.
- Record all changes to the research questions, datasets, model architecture and experiments.
- Never describe a planned experiment as a completed result.
- Do not claim novelty until the literature review and citation-chain analysis are complete.
- Do not claim geological detection accuracy without independent reference labels.
- Do not treat interpolated values as measurements or grid spacing as true source resolution.

## Current status

This is a research plan, not a report of completed experiments. Dataset coverage, magnetic-data accessibility, reference labels, external validation and model performance remain to be verified.

## Core principle

The contribution should be a defensible study of the reliability of multimodal geophysical anomaly detection under heterogeneous spatial resolution, incomplete observations, measurement degradation and constrained adversarial perturbations—not merely the application of an autoencoder to seamount data.
