---
tags:
  - index
  - moc
  - aegis-sea
aliases:
  - AEGIS-SEA Home
  - Vault Index
created: 2026-11-26
status: active
---

# AEGIS-SEA — Knowledge & Memory Vault

> [!IMPORTANT] Core Principle
> **Aegis-Sea 2.0** is an original methodological study on the **reliability of multimodal geophysical anomaly detection** under heterogeneous spatial resolution, incomplete observations, measurement degradation, and constrained adversarial perturbations—using **Indian Ocean** volcanic structures as case studies: **Afanasy Nikitin Seamount** (primary, Central Indian Basin) and **Ninety East Ridge** (external cross-region validation). It is **not** merely applying an autoencoder to seamount data, and **not** an eruption-prediction system.

## Current Repository State (2026-11-26)
- **Stage:** Gate 1 data acquisition in progress (`ans_srtm15.nc` & `ner_srtm15.nc` downloaded; `grav_34.1.nc` downloading).
- **Pipeline (`src/`):** Implemented and verified via `tests/test_pipeline_smoke.py` on synthetic `EPSG:32605` GeoTIFFs.
- **Verified scientific results:** None yet — awaiting real-data pipeline execution.
- **Hardware target:** MacBook Air M4, 16 GB RAM (CPU-friendly NumPy/SciPy/scikit-learn; no GPU required).

## Maps of Content (MOCs)
- [[Complete Walkthrough (Easy & Technical)]] — **Start here** for a plain-English + mathematical walkthrough of everything we built and measured.
- [[MOC - Research Foundation]] — Charter, scope, RQs/hypotheses, literature review, publication strategy.
- [[MOC - Technical Architecture]] — Data feasibility, 8-stage geospatial pipeline, model architectures, adversarial threat model & defenses.
- [[MOC - Execution & Paper]] — E1–E14 protocol, metrics, team roles, 12-week roadmap, reproducibility checklists, and manuscript/starter status.

## Agent Memory
- [[Memory Index & Invariants]] — Persistent invariants, verified vs. unverified boundaries, and sync state with `everything-antigravity_memory`.

## Four Decision Gates (Must Pass in Order)
1. **Gate 1 — Data Feasibility:** Geographic overlap, temporal compatibility, native resolution, usable coverage ([[Dataset Acquisition & Feasibility]]).
2. **Gate 2 — Validation Feasibility:** Independent geological reference evidence & operational anomaly definition ([[Research Questions & Hypotheses]]).
3. **Gate 3 — Baseline Feasibility:** Reproducible spatial pipeline + at least 2 working baselines ([[Model Architecture]]).
4. **Gate 4 — Robustness Feasibility:** Realistic degradation ranges & physically/instrumentally constrained threat model ([[Adversarial Threat Model & Defenses]]).

