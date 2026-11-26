# Reliability of Multimodal Geophysical Anomaly Detection Under Spatial Resolution Mismatch and Sensor Degradation: A Case Study of Lō‘ihi Seamount

**Authors:** [Author 1], [Author 2], [Author 3], [Author 4]  
**Affiliations:** [Department, Institution]  
**Corresponding author:** [Email]

> **Manuscript status:** Working draft. All bracketed fields must be completed from verified data and experiments. No numerical results or conclusions should be inserted until measured.

## Abstract

[Background: 1–2 sentences describing geophysical anomaly mapping and heterogeneous observations.]

[Objective: state the reliability question and the Lō‘ihi case study.]

[Methods: name the verified datasets, preprocessing, models, spatial holdout and degradation tests. Only list methods actually executed.]

[Results: insert measured results with units, sample counts, uncertainty and comparisons. Do not write this paragraph until experiments are complete.]

[Conclusion: state only conclusions directly supported by results.]

**Index Terms—** Geophysical anomaly detection, multimodal learning, bathymetry, gravity, spatial validation, sensor degradation, robustness.

## I. Introduction

Geophysical interpretation of submarine volcanic systems increasingly relies on observations acquired by different instruments and at different spatial and temporal scales. Bathymetric and gravity observations provide complementary information, but their coverage, resolution, uncertainty and acquisition history may differ substantially.

Machine-learning anomaly detection offers a way to identify statistically unusual spatial patterns in these data. However, an anomaly score is not itself evidence of a geological feature. The reliability of the score may depend on how observations are aligned, which modalities are available, and how the model responds to measurement degradation.

This study examines these issues using Lō‘ihi Seamount, Hawai‘i, as a case study. The central research question is:

**How reliably can multimodal geophysical anomaly detection identify unusual patterns when the input observations have heterogeneous spatial resolution, incomplete coverage and controlled measurement degradation?**

The study addresses four questions:

1. Does combining bathymetry and gravity produce more stable anomaly rankings than either modality alone?
2. How does missing modality information affect anomaly scores?
3. How sensitive are the models to controlled noise, smoothing and resolution loss?
4. Can a bounded, model-directed perturbation materially alter anomaly scores?

The contributions will be stated only after the experiments establish them. The intended contribution is a reproducible evaluation protocol for multimodal geophysical anomaly detection under spatial and sensor uncertainty, rather than a claim that unsupervised scores independently identify new geological structures.

## II. Related Work

### A. Seafloor and Seamount Mapping

[Discuss established bathymetric, gravity-derived and machine-learning approaches to seamount detection. Compare input data, labels, spatial scale and validation strategy.]

### B. Multimodal Geophysical Learning

[Review approaches combining bathymetry, gravity, magnetics and other geophysical measurements. Explain what is genuinely different in this study.]

### C. Robustness and Spatial Generalization

[Review spatially blocked validation, missing-modality learning, measurement degradation and adversarial robustness in geoscience or related remote-sensing tasks.]

### D. Research Gap

[Precisely identify the gap after verifying the closest prior work. Do not claim that multimodal seamount detection itself is novel.]

## III. Study Area and Data

### A. Study Area

[Describe the geographic boundary, coordinate reference system, bathymetric setting and rationale for selecting Lō‘ihi. Include a location map.]

### B. Data Sources

| Modality | Provider / product | Native resolution | Coverage | Units | Licence / citation |
|---|---|---:|---|---|---|
| Bathymetry | [Verified source] | [Measured/documented] | [Measured] | [Units] | [Citation] |
| Gravity | [Verified source] | [Measured/documented] | [Measured] | [Units] | [Citation] |
| Magnetics (optional) | [Verified source] | [Measured/documented] | [Measured] | [Units] | [Citation] |

### C. Quality Control and Spatial Alignment

[Describe source checks, nodata handling, coordinate transformation, target grid, resampling, overlap mask, and the limitations of the chosen target resolution. Preserve native resolution information.]

No missing observation is interpreted as a physical zero. Coverage and validity masks are retained. Resampling is not described as increasing the information content of the original measurement.

## IV. Methodology

### A. Feature Construction

[Document bathymetry, slope, roughness, gravity and gravity-gradient features. State units, window sizes and edge handling.]

### B. Spatial Validation

[Describe geographic training and held-out blocks. Explain why random cell-level splitting would risk spatial leakage. Include a split map.]

### C. Baseline Models

1. Isolation Forest: [configuration, seed, contamination handling].
2. PCA reconstruction: [number of components and fitting procedure].
3. Autoencoder, if executed: [architecture, regularization, training details].

### D. Multimodal Fusion

[Describe the actual fusion approach and normalization. Compare it with single-modality baselines. Do not imply a fusion model was implemented if only concatenated features were used.]

### E. Degradation and Perturbation Protocol

[Define each degradation in physical or standardized units, spatial support, strength levels and random seeds. Distinguish ordinary measurement degradation from model-directed perturbation.]

[For model-directed tests, define the objective, perturbation norm, feature-wise bounds and physical plausibility limitations.]

### F. Evaluation

[Use independent reference labels only if they exist and are documented. Otherwise focus on score stability, rank correlation, top-k overlap and spatial generalization. Keep synthetic validation separate from real geological validation.]

## V. Experimental Results

**This section must remain incomplete until the pipeline has been run.**

### A. Data Coverage and Quality

[Insert actual valid-cell counts, overlap percentage, native resolutions, coverage map and quality observations.]

### B. Baseline and Modality Ablation

[Insert measured results for bathymetry-only, gravity-only and combined input. State the evaluation basis.]

### C. Missingness and Measurement Degradation

[Insert measured score-stability results and plots.]

### D. Model-Directed Perturbation

[Insert actual perturbation bounds, score changes and limitations.]

### E. Spatial Holdout

[Report held-out geography, sample counts and observed generalization behaviour.]

## VI. Discussion

[Interpret the actual findings. Explain whether fusion helped, where it failed, which data-quality conditions mattered, and whether patterns are consistent with known geological context. Do not equate high anomaly scores with confirmed geological discoveries.]

## VII. Limitations

[Discuss data coverage, resolution mismatch, uncertainty, reference-label scarcity, spatial sampling, model assumptions, synthetic degradation, and limitations of the case study.]

## VIII. Conclusion

[Summarize only the demonstrated findings and practical implications. Identify follow-up work without presenting it as completed.]

## Data and Code Availability

[Provide dataset access conditions, repository URL, code version/commit, processing scripts and any restrictions.]

## Acknowledgment

[Funding, data providers, institutional support and contributors.]

## References

[Complete and verify every reference. Include DOI or stable source URL where available.]
