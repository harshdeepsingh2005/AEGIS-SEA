---
tags:
  - moc
  - technical-architecture
created: 2026-11-26
---

# MOC — Technical Architecture

## Set 2 Documents (`SET_2_TECHNICAL_ARCHITECTURE/`)
- [[Dataset Acquisition & Feasibility]] — Candidate sources (GEBCO, NOAA NCEI/MGDS, USGS), 17-field inventory schema, 5 feasibility tests (A–E), go/no-go thresholds, and 7 deliverables.
- [[Geospatial Data Pipeline]] — 8-stage pipeline, missing-data representation (value + mask + uncertainty), seismicity features, spatial block splits, and data-leakage controls.
- [[Model Architecture]] — Baselines A–D, proposed multimodal encoder/fusion design, fusion strategies, weighted score $S(x)$, modality dropout, uncertainty estimation, and ablations.
- [[Adversarial Threat Model & Defenses]] — Family A (measurement degradation) vs. Family B (adversarial attacks), 9-field threat-model spec, experiments A1–A8, defenses A–D, and $L_{\text{total}}$.

## Cross-Links
- [[Experimental Protocol & Metrics]] — How Set 2 models and threat models map to experiments E1–E14.
- [[Manuscript & Starter Scaffold]] — Current root starter requirements (`requirements.txt`, `DATA.md`, `README.md`).

