# Reliability of Multimodal Geophysical Anomaly Detection Under Spatial Resolution Mismatch and Sensor Degradation: Case Studies in the Indian Ocean (Afanasy Nikitin Seamount and Ninety East Ridge)

**Authors:** [Author 1], [Author 2], [Author 3], [Author 4]  
**Affiliations:** [Department, Institution]  
**Corresponding author:** [Email]

> **Manuscript status:** Experimental draft populated with verified outputs from `src.run_pipeline`, `src.spatial_cv`, `src.cross_region`, `src.defenses`, and `src.figures` (2026-11-26). All numerical claims trace directly to `data/processed/` and `DATA.md`.

## Abstract

Multimodal machine-learning anomaly detection on marine geophysical grids is vulnerable to spatial-resolution mismatch, missing observations, and distribution shift across geological regimes. Using two contrasting Indian Ocean volcanic structures—**Afanasy Nikitin Seamount (ANS)** in the Central Indian Basin (`EPSG:32744`) and a segment of the **Ninety East Ridge (NER)** (`EPSG:32745`)—we evaluate Isolation Forest and Principal Component Analysis (PCA) reconstruction detectors trained on `SRTM15+` bathymetry (`~459–462 m` projected) and Scripps 1-arc-minute free-air marine gravity (`~1822–1847 m` projected; ~4× coarser). Across 5-block longitudinal spatial cross-validation ($N = 150{,}000$ sampled cells per region), early feature concatenation (`Combined PCA`) suffers severe ranking collapse under missing modalities (ANS gravity missing: Spearman $\rho = -0.085 \pm 0.570$; NER bathymetry missing: $\rho = -0.023 \pm 0.300$) and asymmetric cross-region transfer failure (`ANS → NER`: $\rho = -0.134$, top-5% overlap $0.470$). Replacing early concatenation with **Late-Fusion Per-Modality Score Aggregation** eliminates the `ANS → NER` transfer collapse ($\rho = 0.936$, top-5% overlap $0.957$) and stabilizes missing-modality rankings (`ANS_bathymetry_missing`: $\rho = 0.904 \pm 0.046$; `NER_bathymetry_missing`: $\rho = 0.938 \pm 0.082$), while revealing an accuracy–noise trade-off under isotropic feature noise ($\sigma = 0.20$). Out-of-fold anomaly peaks align with documented summit/guyot scarps on ANS and ridge-crest scarps on NER, but without pixel-level ground-truth labels, anomaly scores are interpreted strictly as statistical unusualness rather than confirmed geological discoveries.

**Index Terms—** Geophysical anomaly detection, multimodal learning, bathymetry, gravity, Indian Ocean, spatial cross-validation, sensor degradation, robustness.

## I. Introduction

Geophysical interpretation of submarine volcanic systems increasingly relies on observations acquired by different instruments at different spatial and temporal scales. Bathymetric and gravity observations provide complementary structural information, yet their native resolution, uncertainty, and spatial coverage differ substantially.

Machine-learning anomaly detection offers a quantitative way to rank statistically unusual spatial patterns. However, an anomaly score is not itself proof of a geological feature, and its reliability depends on how modalities are aligned, how spatial holdouts are constructed, and how detectors behave under missing or degraded inputs.

This study investigates these reliability questions across two contrasting Indian Ocean volcanic regions: **Afanasy Nikitin Seamount (ANS)** and the **Ninety East Ridge (NER)**. Specifically, we address:
1. How sensitive are multimodal anomaly rankings to raster-space resolution degradation (`2x`, `4x`) and missing modalities?
2. Do multimodal anomaly models transfer across distinct Indian Ocean tectonic regimes (`ANS ↔ NER`)?
3. Can late-fusion per-modality score aggregation stabilize rankings under modality dropout and cross-region shift?
4. How do out-of-fold anomaly peaks compare against published Indian Ocean geological references?

## II. Related Work

### A. Seafloor and Seamount Mapping
Global seamount inventories have been constructed from satellite-altimetry-derived gravity anomalies \cite{kim2011seamounts} and 30-arc-second bathymetry \cite{yesson2011seamounts}, alongside global 15-arc-second bathymetric synthesis (`SRTM15+`) \cite{tozer2019srtm15plus} and marine gravity models \cite{sandwell2014gravity}. For our Indian Ocean case studies, Krishna et al. \cite{krishna2014ans} and Paul et al. \cite{paul1990ans} document the plateau/guyot morphology and gravity–bathymetry transfer characteristics of ANS, while Sreejith and Krishna \cite{sreejith2013ner} analyze isostatic compensation and structural segmentation along NER.

### B. Multimodal Geophysical Learning & Robustness
Standard multimodal workflows often stack interpolated rasters into a single feature vector (early fusion). However, early fusion entangles cross-modality covariance, creating fragility when one modality is missing, smoothed, or shifted in a new geological domain. Moreover, random cell-level splitting leaks spatially autocorrelated neighbors across train/test sets; spatial block cross-validation is therefore required.

## III. Study Area and Data

### A. Study Areas
1. **Afanasy Nikitin Seamount (ANS, Primary):** `81.5°E–84.5°E, 4.5°S–1.5°S`, projected to `EPSG:32744` (WGS 84 / UTM Zone 44S). Depth spans `-5300.86 m` to `-1463.12 m`; free-air gravity spans `-69.28` to `+57.56 mGal`.
2. **Ninety East Ridge (NER, External Validation):** `87.5°E–90.5°E, 11.5°S–8.5°S`, projected to `EPSG:32745` (WGS 84 / UTM Zone 45S). Depth spans `-6361.55 m` to `-1468.70 m`; free-air gravity spans `-92.82` to `+58.94 mGal`.

### B. Data Sources
| Modality | Provider / Product | Native Resolution | Projected Grid | Valid Overlap | Units |
|---|---|---:|---:|---:|---|
| Bathymetry | NOAA CoastWatch ERDDAP `srtm15plus` (`z`) \cite{tozer2019srtm15plus} | `0.004167°` (15 arc-sec) | `462.09 m` (ANS) / `458.96 m` (NER) | `520,108` (ANS) / `519,598` (NER) | `m` |
| Gravity | Scripps TOPEX 1-min free-air gravity \cite{sandwell2014gravity} | `~0.0167°` (1 arc-min) | `1847.00 m` (ANS) / `1821.68 m` (NER) | `99.54%` (ANS) / `98.48%` (NER) | `mGal` |

### C. Quality Control and Spatial Alignment
Gravity is reprojected onto the bathymetry grid using bilinear interpolation (`src/geodata.py`). **Resampling does not increase the native information content of the ~4× coarser gravity source.** Missing/NoData cells are masked rather than zero-filled, and a 1-pixel `binary_erosion` border mask is applied around `NaN` boundaries so finite-difference derivatives never encounter artificial raster-edge cliffs. Each region is subsampled to $N = 150{,}000$ valid interior cells (`seed=42`).

## IV. Methodology

### A. Feature Construction
Five features are extracted in projected metric coordinates: (1) bathymetry ($z$), (2) bathymetric slope ($\|\nabla z\|_2$), (3) bathymetric roughness (3×3 local standard deviation), (4) free-air gravity ($g$), and (5) gravity gradient magnitude ($\|\nabla g\|_2$).

### B. Spatial Validation & Models
We evaluate both a single easternmost 20% holdout (`src/models.py`) and **5-block longitudinal spatial cross-validation** (`src/spatial_cv.py`), reporting block means and 95% t-confidence intervals ($\text{df}=4$). `StandardScaler`, `IsolationForest` (`n_estimators=300`), and `PCA` ($k = \min(3, d-1)$) are fitted strictly on training blocks.

### C. Degradation, Perturbation, and Defense Protocol
- **Gaussian Noise (`E10`):** Isotropic standardized noise ($\sigma = 0.20$).
- **Modality Dropout (`E9`):** Masking bathymetry (`[0, 1, 2]`) or gravity (`[3, 4]`) to training mean (`0.0` in standardized space) for Combined PCA, or omitting the missing branch in Late Fusion.
- **Raster-Space Resolution Degradation (`E8`):** NaN-aware Gaussian smoothing ($\sigma_{\text{px}} \in \{1.0, 2.0\}$ for `2x`, `4x` coarsening) applied to bathymetry *prior* to recomputing slope and roughness.
- **Model-Directed Perturbation (`E11`):** Bounded $L_\infty$ PCA residual step ($z_{\text{adv}} = z + \varepsilon \, r / (\|r\|_\infty + 10^{-12})$, $\varepsilon = 0.10$).
- **Defense D — Late-Fusion Score Aggregation (`E12`):** Independent per-modality PCA detectors normalized by training mean error:
  $$S_{\text{late}}(x) = \frac{1}{|M|} \sum_{m \in M} \frac{E_m(x)}{\bar{E}_{m,\text{train}}}$$

## V. Experimental Results

### A. 5-Block Spatial CV: Robustness & Defense Comparison (`E8`, `E9`, `E10`, `E11`, `E12`)
From `data/processed/spatial_cv_summary.csv` (mean $\pm$ 95% CI across 5 spatial blocks; Spearman $\rho$ and top-5% overlap vs. clean):

| Region | Condition | Combined PCA $\rho$ | Combined Top-5% | Late-Fusion $\rho$ | Late-Fusion Top-5% |
|---|---|---:|---:|---:|---:|
| ANS | `noise_0.20` | `0.729 ± 0.131` | `0.552 ± 0.125` | `0.108 ± 0.093` | `0.122 ± 0.077` |
| ANS | `bathy_missing` | `0.296 ± 0.584` | `0.336 ± 0.425` | **`0.904 ± 0.046`** | **`0.630 ± 0.161`** |
| ANS | `gravity_missing` | `-0.085 ± 0.570` | `0.117 ± 0.175` | **`0.317 ± 0.082`** | **`0.438 ± 0.125`** |
| ANS | `res_deg_4x` | `0.993 ± 0.009` | `0.958 ± 0.034` | `0.918 ± 0.040` | `0.642 ± 0.156` |
| ANS | `pca_linf_0.10` | `1.000 ± 0.000` | `0.999 ± 0.001` | — | — |
| NER | `noise_0.20` | `0.441 ± 0.110` | `0.394 ± 0.149` | `0.330 ± 0.180` | `0.361 ± 0.213` |
| NER | `bathy_missing` | `-0.023 ± 0.300` | `0.166 ± 0.137` | **`0.938 ± 0.082`** | **`0.714 ± 0.395`** |
| NER | `gravity_missing` | `0.164 ± 0.249` | `0.125 ± 0.086` | **`0.281 ± 0.238`** | **`0.464 ± 0.404`** |
| NER | `res_deg_4x` | `0.981 ± 0.025` | `0.887 ± 0.130` | `0.947 ± 0.068` | `0.720 ± 0.384` |
| NER | `pca_linf_0.10` | `0.997 ± 0.001` | `0.986 ± 0.018` | — | — |

See `reports/figures/fig1_ans_ner_maps.png` and `reports/figures/fig2_spatial_cv_robustness.png`.

### B. Cross-Region Spatial Transfer (`E13` & `E12`)
From `data/processed/cross_region_transfer.csv` and `data/processed/defense_comparison.csv` (see `reports/figures/fig3_cross_region_transfer.png`):
- **`ANS → NER`:** Single-modality PCA transfers cleanly (`0.445` bathymetry, `0.947` gravity), but **Combined PCA collapses to $\rho = -0.134$** (top-5% overlap `0.470`). **Late-Fusion Defense D restores transfer to $\rho = 0.936$** (top-5% overlap `0.957`).
- **`NER → ANS`:** Combined PCA transfers at $\rho = 0.907$ (top-5% `0.809`), and **Late-Fusion Defense D improves it to $\rho = 0.966$** (top-5% `0.892`).

### C. Gate 2 Geological Validation (Out-of-Fold Peaks)
Cross-referencing 5-block out-of-fold (OOF) top-1% anomaly coordinates against published Indian Ocean studies:
1. **ANS Summit Plateau / Guyot Scarp (`82.90°E–82.91°E, 3.10°S`, depth `-1826` to `-1889 m`, gravity `+20.3` to `+20.6 mGal`):** Identified by `OOF_CombinedPCA` top peaks; **Confirmed** against Krishna et al. \cite{krishna2014ans} and Paul et al. \cite{paul1990ans}.
2. **ANS Northern Flank / Secondary Highs (`82.65°E–82.94°E, 2.28°S–2.46°S`, depth `-3899` to `-4656 m`):** Identified by `OOF_LateFusion` top peaks; **Partially supported** by northern secondary elevated highs/margin descriptions in Krishna et al. \cite{krishna2014ans}, pending multibeam verification.
3. **NER Ridge Crest & Bounding Scarps (`88.56°E–88.94°E, 11.20°S–11.40°S`, depth `-1846` to `-2905 m`, gravity `+32.0` to `+36.8 mGal`):** Identified identically by both `OOF_LateFusion` and `OOF_CombinedPCA` top peaks; **Confirmed** as the Ninetyeast Ridge crest/scarp corridor \cite{sreejith2013ner}, with fine-scale fracture-zone attribution **Partially supported** without shipborne multibeam.

## VI. Discussion

Early concatenation (`Combined PCA`) learns rigid cross-modality covariance that breaks both under missing modalities (`ANS_gravity_missing`: $\rho = -0.085$) and asymmetric domain shift (`ANS → NER`: $\rho = -0.134$). **Late-Fusion Score Aggregation** decouples modality encoders, eliminating the `ANS → NER` collapse ($\rho = 0.936$) and stabilizing missing-modality rankings. However, 5-block CV also reveals an important **accuracy–noise trade-off**: under isotropic standardized noise ($\sigma = 0.20$), Late Fusion is more sensitive than Combined PCA (`0.108` vs. `0.729` on ANS) because each 2–3D sub-encoder has fewer redundant dimensions to average out noise.

## VII. Limitations

1. **No pixel-level geological ground-truth labels:** Precision, recall, and AUROC are intentionally omitted; validation relies on score stability and coordinate cross-referencing against published studies.
2. **Coarse gravity support:** Scripps 1-arc-min gravity (`~1.83 km`) is ~4× coarser than `SRTM15+` bathymetry (`~460 m`).
3. **Optional magnetics excluded:** Magnetic trackline coverage has not yet passed Gate 1 feasibility and was excluded rather than fabricated.
4. **Linear detectors:** Only Isolation Forest and PCA were evaluated in this CPU starter; neural autoencoders and adversarial training remain future work.

## VIII. Conclusion

Across two Indian Ocean volcanic regimes (ANS and NER), late-fusion per-modality score aggregation substantially improves resilience to missing modalities and cross-region transfer compared to early feature concatenation, while exhibiting higher sensitivity to isotropic feature noise.

## Data and Code Availability

All processing, modeling, 5-block CV, defense, and plotting scripts are in `src/` and `scripts/`, with checksums and access URLs in `DATA.md`.

## References

Verified BibTeX entries are provided in `paper/references.bib`.
