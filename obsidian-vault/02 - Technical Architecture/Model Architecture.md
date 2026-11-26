---
tags:
  - technical-architecture
  - models
  - fusion
source: Aegis-Sea_Research_Documentation/SET_2_TECHNICAL_ARCHITECTURE/07_model_architecture.md
created: 2026-11-26
---

# Model Architecture

> [!NOTE] Source
> Distilled from `07_model_architecture.md`. Parent: [[MOC - Technical Architecture]].

## 1. Design Objective & Selection Rule
Test whether multimodal fusion improves anomaly ranking and whether modality-aware design improves reliability under missing/degraded inputs. Keep models no more complex than data volume and RQs justify; retain a complex model only if it gives a repeatable improvement or answers an RQ simpler models cannot.

## 2. Four Baseline Models (A–D)
- **Baseline A — Single-modality Isolation Forest:** Separate detectors on bathymetry, gravity, magnetics, etc.
- **Baseline B — PCA reconstruction:** Fit PCA on training features; use reconstruction error as anomaly score.
- **Baseline C — Dense Autoencoder:** Normalized feature vectors; reconstruction error as anomaly score.
- **Baseline D — Feature-concatenation model:** Concatenate aligned features and train the same detector class (tests if simple early fusion suffices).

## 3. Proposed Multimodal Model & Fusion Strategies
Modality-specific encoders (bathymetry/terrain, gravity, optional magnetics, optional seismicity) + coverage/uncertainty representation $\rightarrow$ fusion layer $\rightarrow$ shared latent $\rightarrow$ modality-aware decoder/heads $\rightarrow$ anomaly score. *(Do not force different data structures like rasters, tracklines, and event sequences into identical branches.)*

**Fusion strategies to compare** (under identical spatial split & training budget):
1. **Early fusion:** Concatenate standardized features.
2. **Feature-level fusion:** Encode each modality, then combine latent vectors.
3. **Reliability-aware fusion:** Weight representations using coverage/uncertainty metadata.

## 4. Anomaly Scoring
Weighted score formulation:
$$S(x) = \sum_{m} w_m \, E_m(x)$$
where $E_m(x)$ is per-modality error and $w_m$ is a pre-defined or learned weight (estimated without test-set leakage and examined via ablation). *Never call $S(x)$ a probability unless calibrated and validated.*

## 5. Modality Dropout & Uncertainty Estimation
- **Modality dropout:** Randomly mask modalities during training (aligned with realistic survey missingness) and test under 1-missing, multi-missing, spatially clustered, and survey-matched missingness.
- **Uncertainty:** Deep ensembles, MC dropout, heteroscedastic heads, modality-specific uncertainty, or cross-detector disagreement. Validate whether uncertainty correlates with errors or unstable rankings.

## 6. Training, Ablation & Stack
- **Training:** Fit on training spatial blocks only; tune on validation blocks; evaluate once on test blocks; multiple seeds; log failed and successful runs.
- **Ablations:** Remove one component at a time (each modality, coverage masks, uncertainty features, modality dropout, fusion mechanism, robustness loss, reconstruction head).
- **Stack:** Python, PyTorch, scikit-learn, NumPy/SciPy/pandas, Xarray/Rasterio/GeoPandas/GDAL, QGIS, MLflow/W&B, Git/DVC. *(Note: current root `requirements.txt` uses the lightweight CPU starter stack without PyTorch; see [[Manuscript & Starter Scaffold]].)*

