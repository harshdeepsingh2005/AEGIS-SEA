# 10 — Team Roles and Repository Structure

## 1. Team organization

Four members are divided into two workstreams.

### Team A — Geophysics and baseline modelling

**Member 1: Geospatial Data Engineer**
- Study-area boundary.
- Dataset inventory and acquisition.
- Bathymetry, gravity, magnetic and seismic data inspection.
- CRS standardization.
- Quality control and coverage mapping.
- Native-resolution and provenance documentation.
- Master spatial dataset.

**Member 2: Geophysical ML Engineer**
- Terrain and geophysical feature engineering.
- Baseline models.
- Multimodal fusion implementation.
- Anomaly-score design.
- Modality ablation.
- Initial geological interpretation with reference sources.

### Team B — Robustness and evaluation

**Member 3: Robustness / Adversarial ML Engineer**
- Measurement-degradation design.
- Threat-model definitions.
- Single- and multi-modality perturbations.
- Attack implementation.
- Adversarial training.
- Robustness experiment tracking.

**Member 4: Evaluation / Uncertainty Engineer**
- Spatial split design.
- Reference-feature catalogue.
- Evaluation metrics.
- Environmental strata.
- Uncertainty and calibration evaluation.
- Statistical analysis.
- Figures and manuscript integration.

## 2. Shared responsibilities

All members must:
- Read the project charter and research questions.
- Review the closest competing literature.
- Participate in weekly integration meetings.
- Review experiment design before execution.
- Keep code reproducible.
- Review manuscript claims and limitations.
- Understand the complete research pipeline sufficiently to defend it.

Authorship must reflect actual scholarly contributions and follow the target venue's policy. Role assignment alone does not determine authorship order.

## 3. Workstream interfaces

Team A must provide Team B:
- Versioned data schema.
- Feature definitions and units.
- Per-modality masks.
- Spatial split IDs.
- Model training and inference interfaces.
- Baseline checkpoints and configurations.

Team B must provide Team A:
- Attack/degradation specifications.
- Evaluation code and metric definitions.
- Validation feedback.
- Reproducibility requirements.
- Robustness and uncertainty findings.

## 4. Suggested repository structure

```text
AEGIS-SEA/
├── README.md
├── docs/
│   ├── project_charter.md
│   ├── data_dictionary.md
│   └── experiment_protocol.md
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── metadata/
├── configs/
├── src/
│   ├── ingestion/
│   ├── preprocessing/
│   ├── features/
│   ├── models/
│   ├── attacks/
│   ├── defenses/
│   ├── evaluation/
│   └── visualization/
├── notebooks/
├── tests/
├── experiments/
├── reports/
├── paper/
└── environment/
```

Do not commit large restricted datasets, credentials or private tokens. Use data manifests, retrieval scripts and checksums.

## 5. Git workflow

- `main`: stable, reviewed code.
- `dev`: integration branch.
- Feature branches: `feature/data-ingestion`, `feature/fusion-model`, etc.
- Require code review for changes to preprocessing, labels, splits and metrics.
- Tag major experiment versions.
- Use issues for tasks and pull requests for changes.
- Keep configuration files with experiment outputs.

## 6. Weekly meeting format

1. What was completed?
2. What evidence was produced?
3. What failed and why?
4. What changed in the data or assumptions?
5. What is blocked?
6. What is the next measurable deliverable?

A meeting update should include links to code, logs, maps or reports—not only verbal progress.
