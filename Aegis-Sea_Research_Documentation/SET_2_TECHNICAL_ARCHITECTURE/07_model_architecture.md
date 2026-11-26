# 07 — Model Architecture

## 1. Design objective

Build a model comparison framework that tests whether multimodal fusion improves geophysical anomaly ranking and whether modality-aware design improves reliability under missing or degraded inputs.

The model should be no more complex than required by the data volume and research questions.

## 2. Baseline models

### Baseline A — Single-modality Isolation Forest
Train separate detectors on bathymetry-derived features, gravity, magnetics and other usable modalities. This establishes the contribution of each source.

### Baseline B — PCA reconstruction
Fit PCA on training features and calculate reconstruction error. This is a simple, interpretable reconstruction baseline.

### Baseline C — Dense Autoencoder
Train a conventional autoencoder on normalized feature vectors. Use reconstruction error as an anomaly score.

### Baseline D — Feature-concatenation model
Concatenate aligned feature vectors and train the same class of detector. This tests whether simple fusion is already sufficient.

## 3. Proposed multimodal model

Use modality-specific encoders where data volume and modality coverage justify them.

Conceptual flow:

1. Bathymetry/terrain encoder.
2. Gravity encoder.
3. Magnetic encoder, if verified data exist.
4. Seismicity encoder, if temporal and spatial support are defensible.
5. Coverage/uncertainty representation.
6. Fusion layer.
7. Shared latent representation.
8. Modality-aware decoder or reconstruction heads.
9. Anomaly-score calculation.

Do not force all modalities into identical neural-network branches if their data structures differ. Raster patches, trackline measurements and event sequences may require different encoders or feature representations.

## 4. Fusion strategies to compare

- Early fusion: concatenate standardized features before the model.
- Feature-level fusion: encode each modality, then combine latent vectors.
- Reliability-aware fusion: use coverage/uncertainty information to weight available representations.

Compare strategies under the same spatial split and training budget.

## 5. Anomaly scoring

Possible score components:
- Total reconstruction error.
- Per-modality reconstruction error.
- Latent-space distance.
- Ensemble or detector disagreement.
- Uncertainty estimate.

A weighted score may be written:

`S(x) = sum_m w_m * E_m(x)`

where `E_m` is the error for modality `m` and `w_m` is a pre-defined or learned weight. The weights must be estimated without test-set leakage and should be examined through ablation.

Do not call `S(x)` a probability unless it has been calibrated and validated as one.

## 6. Modality dropout

During training, randomly mask selected modalities according to a documented missingness design. This may improve tolerance to missing inputs.

Test whether dropout helps under:
- One missing modality.
- Multiple missing modalities.
- Spatially clustered missingness.
- Missingness patterns matching actual survey coverage.

Avoid dropout rates that create unrealistic training conditions.

## 7. Uncertainty estimation

Potential approaches:
- Deep ensembles.
- Monte Carlo dropout.
- Heteroscedastic output heads where justified.
- Modality-specific uncertainty estimates.
- Agreement/disagreement across independently trained detectors.

Evaluate whether uncertainty is associated with errors or unstable anomaly rankings. Do not assume an uncertainty estimate is meaningful without calibration or validation.

## 8. Training protocol

- Use training spatial blocks only for fitting.
- Use validation blocks for hyperparameter selection.
- Keep test blocks untouched until final evaluation.
- Fix and report random seeds.
- Repeat experiments across multiple seeds.
- Record optimizer, learning rate, batch size, epochs, early stopping and normalization.
- Save model checkpoints and configurations.
- Track all failed as well as successful runs.

## 9. Ablation plan

Remove one component at a time:
- Each modality.
- Coverage masks.
- Uncertainty features.
- Modality dropout.
- Fusion mechanism.
- Robustness loss.
- Reconstruction head.

Ablations are necessary to show which components contribute value.

## 10. Recommended implementation stack

- Python.
- PyTorch.
- scikit-learn.
- NumPy, SciPy, pandas.
- Xarray, Rasterio, GeoPandas, GDAL.
- QGIS for independent spatial inspection.
- MLflow or Weights & Biases for experiment tracking.
- Git and DVC where appropriate.

## 11. Model selection rule

Choose the model based on pre-defined validation criteria, not the most attractive final map. A more complex model should only be retained if it provides a meaningful, repeatable improvement or answers a research question that simpler models cannot.
