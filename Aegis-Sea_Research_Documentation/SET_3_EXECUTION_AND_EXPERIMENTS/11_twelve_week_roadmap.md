# 11 — Twelve-Week Research Roadmap

## Overview

The 12-week schedule targets a complete experimental manuscript draft. It does not guarantee journal acceptance or even guarantee that every planned modality will pass feasibility checks.

## Weeks 1–2: Research and data feasibility

**Team A**
- Define study-area polygon.
- Identify GEBCO and high-resolution survey products.
- Search NOAA and MGDS for gravity and magnetic observations.
- Inspect seismicity sources.
- Build initial data inventory.

**Team B**
- Review close seamount-detection literature.
- Define measurement-degradation categories.
- Draft threat-model template.
- Define candidate validation metrics.
- Investigate reference geological features.

**Deliverable:** Data-feasibility report, literature matrix and revised scope decision.

**Gate:** Do not continue with a modality that lacks usable evidence or coverage.

## Weeks 3–4: Data engineering

**Team A**
- Download approved data.
- Inspect units, CRS, native resolution and uncertainty.
- Generate coverage maps.
- Implement QC and spatial alignment.
- Produce first master dataset.

**Team B**
- Define spatial blocks.
- Build evaluation pipeline.
- Finalize degradation bounds from source documentation.
- Catalogue reference features.

**Deliverable:** Versioned dataset, masks, metadata, spatial split and evaluation specification.

## Weeks 5–6: Baselines

**Team A**
- Engineer justified features.
- Implement Isolation Forest.
- Implement PCA reconstruction.
- Implement dense autoencoder.
- Implement early-fusion baseline.

**Team B**
- Validate split integrity.
- Test metric code on controlled examples.
- Run preliminary missingness and resolution experiments.
- Review model-output interpretation.

**Deliverable:** Reproducible baseline results and first figures.

## Weeks 7–8: Multimodal model and stress testing

**Team A**
- Implement modality-specific encoders where justified.
- Compare fusion strategies.
- Run modality ablations.
- Produce anomaly maps.

**Team B**
- Run measurement-degradation experiments.
- Run missing-modality experiments.
- Implement constrained adversarial attacks.
- Record score and ranking changes.

**Deliverable:** Multimodal comparison and robustness benchmark.

## Weeks 9–10: Defenses and analysis

**Team A**
- Refine model only where experiments justify it.
- Review geological interpretation.
- Investigate failure cases.

**Team B**
- Test modality dropout.
- Test uncertainty-aware fusion.
- Test adversarial training.
- Compare defense trade-offs.
- Run statistical analysis.

**Deliverable:** Defense comparison, uncertainty analysis and near-final figures.

## Weeks 11–12: Manuscript and reproducibility

**All members**
- Write methods and results.
- Complete literature and novelty review.
- Verify references.
- Document limitations.
- Package code and configurations.
- Review claims against evidence.
- Prepare conference/journal submission plan.

**Deliverable:** Complete manuscript draft, code release candidate and supplementary material.

## Scope control

If the data-feasibility stage fails:
- Remove unavailable modalities.
- Prioritize bathymetry plus one verified complementary modality.
- Reframe the work as a data-reliability benchmark if geological labels are inadequate.
- Do not add another study area until the primary pipeline works.

## Weekly status template

```text
Week:
Member:
Objective:
Completed:
Evidence / links:
Experiments:
Results:
Problems:
Decisions required:
Next week's deliverables:
```
