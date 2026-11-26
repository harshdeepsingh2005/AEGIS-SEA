---
tags:
  - execution
  - roadmap
  - timeline
source: Aegis-Sea_Research_Documentation/SET_3_EXECUTION_AND_EXPERIMENTS/11_twelve_week_roadmap.md
created: 2026-11-26
---

# Twelve-Week Research Roadmap

> [!NOTE] Source
> Distilled from `11_twelve_week_roadmap.md`. Parent: [[MOC - Execution & Paper]]. See also the compressed 3-week schedule in [[Manuscript & Starter Scaffold]].

## 1. Six Phases (12 Weeks to Complete Manuscript Draft)
1. **Weeks 1–2 — Research & Data Feasibility:**
   - *Team A:* Study-area polygon, GEBCO + survey bathymetry, NOAA/MGDS gravity & magnetics, seismicity sources, initial data inventory.
   - *Team B:* Literature review, degradation categories, threat-model template, validation metrics, reference geological features.
   - *Gate:* Do not continue with a modality lacking usable evidence or coverage.
2. **Weeks 3–4 — Data Engineering:**
   - *Team A:* Download approved data, inspect units/CRS/res/uncertainty, coverage maps, QC & spatial alignment, first master dataset.
   - *Team B:* Spatial blocks, evaluation pipeline, finalize degradation bounds, catalogue reference features.
3. **Weeks 5–6 — Baselines:**
   - *Team A:* Justified features, Isolation Forest, PCA reconstruction, dense autoencoder, early-fusion baseline.
   - *Team B:* Validate split integrity, test metric code, preliminary missingness & resolution experiments, output interpretation.
4. **Weeks 7–8 — Multimodal Model & Stress Testing:**
   - *Team A:* Modality-specific encoders, fusion comparisons, modality ablations, anomaly maps.
   - *Team B:* Measurement degradation, missing-modality experiments, constrained adversarial attacks, score/ranking changes.
5. **Weeks 9–10 — Defenses & Analysis:**
   - *Team A:* Refine model only if justified, review geological interpretation, investigate failure cases.
   - *Team B:* Modality dropout, uncertainty-aware fusion, adversarial training, defense trade-offs, statistical analysis.
6. **Weeks 11–12 — Manuscript & Reproducibility:**
   - *All:* Methods & results, complete literature/novelty review, verify references, document limitations, package code/configs, review claims vs. evidence, submission plan.

## 2. Scope Control Fallbacks
If data feasibility fails: remove unavailable modalities; prioritize bathymetry + 1 verified complementary modality; reframe as a data-reliability benchmark if geological labels are inadequate; do not add a second study area until the primary pipeline works.

