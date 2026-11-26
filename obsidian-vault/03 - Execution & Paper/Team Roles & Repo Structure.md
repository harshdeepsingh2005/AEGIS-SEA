---
tags:
  - execution
  - team
  - repo-structure
source: Aegis-Sea_Research_Documentation/SET_3_EXECUTION_AND_EXPERIMENTS/10_team_roles_and_repository_structure.md
created: 2026-11-26
---

# Team Roles and Repository Structure

> [!NOTE] Source
> Distilled from `10_team_roles_and_repository_structure.md`. Parent: [[MOC - Execution & Paper]].

## 1. Team Organization (4 Members, 2 Workstreams)
### Team A — Geophysics and Baseline Modelling
- **Member 1 (Geospatial Data Engineer):** Study-area boundary, dataset inventory/acquisition, data inspection, CRS standardization, QC & coverage mapping, native-res/provenance docs, master spatial dataset.
- **Member 2 (Geophysical ML Engineer):** Terrain/geophysical feature engineering, baseline models, multimodal fusion, anomaly-score design, modality ablation, initial geological interpretation.

### Team B — Robustness and Evaluation
- **Member 3 (Robustness / Adversarial ML Engineer):** Measurement-degradation design, threat-model definitions, single/multi-modality perturbations, attack implementation, adversarial training, robustness tracking.
- **Member 4 (Evaluation / Uncertainty Engineer):** Spatial split design, reference-feature catalogue, evaluation metrics, environmental strata, uncertainty/calibration evaluation, statistical analysis, figures & manuscript integration.

## 2. Workstream Interfaces
- **Team A $\rightarrow$ Team B:** Versioned data schema, feature definitions/units, per-modality masks, spatial split IDs, model training/inference interfaces, baseline checkpoints/configs.
- **Team B $\rightarrow$ Team A:** Attack/degradation specs, evaluation code & metrics, validation feedback, reproducibility requirements, robustness/uncertainty findings.

## 3. Target Repository Layout & Git Workflow
- **Target layout:** `docs/`, `data/{raw,interim,processed,metadata}/`, `configs/`, `src/{ingestion,preprocessing,features,models,attacks,defenses,evaluation,visualization}/`, `notebooks/`, `tests/`, `experiments/`, `reports/`, `paper/`, `environment/`.
- **Branches:** `main` (stable), `dev` (integration), `feature/*` branches; require review for preprocessing, labels, splits, and metrics; keep large/restricted data out of Git (use manifests, scripts, checksums).
- **Weekly meeting format:** (1) Completed, (2) Evidence/links, (3) What failed & why, (4) Changes in data/assumptions, (5) Blockers, (6) Next measurable deliverable.

