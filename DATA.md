# Data provenance log

Verified Gate 1 records for the two Indian Ocean study regions (2026-11-26).

| Field | Bathymetry (ANS & NER) | Gravity (ANS & NER) | Optional magnetics |
|---|---|---|---|
| Provider | NOAA CoastWatch ERDDAP / SIO | Scripps Institution of Oceanography (UCSD TOPEX) | Not included (pending Gate 1 coverage check) |
| Product / dataset name | SRTM15_PLUS (`srtm15plus`, var `z`) | Global Marine Gravity 1-min (`get_data.cgi`, `mag=0.1`) | |
| Download URL | `https://coastwatch.pfeg.noaa.gov/erddap/griddap/srtm15plus.nc` | `https://topex.ucsd.edu/cgi-bin/get_data.cgi` | |
| Access date | 2026-11-26 | 2026-11-26 | |
| Version / release | SRTM15+ v1 (ERDDAP) | 1-min global gravity grid | |
| Native CRS | `EPSG:4326` | `EPSG:4326` | |
| Native resolution | `0.004167°` (15 arc-sec; ~459–462 m) | `~0.0167°` (1 arc-min; ~1822–1847 m) | |
| Units | meters (`m`) | milliGal (`mGal`) | |
| NoData value | `NaN` | `NaN` | |
| Spatial bounds (ANS) | `81.5°E–84.5°E, 4.5°S–1.5°S` (`EPSG:32744`) | `81.5°E–84.5°E, 4.5°S–1.5°S` (`EPSG:32744`) | |
| Spatial bounds (NER) | `87.5°E–90.5°E, 11.5°S–8.5°S` (`EPSG:32745`) | `87.5°E–90.5°E, 11.5°S–8.5°S` (`EPSG:32745`) | |
| Licence / terms | Public domain / SIO-NOAA open access | SIO Satellite Geodesy open access | |
| File checksum (SHA-256, ANS) | `98941ea9725ba5fd731a7a0dcc0c124638f14aaf5990c897c17e32a1eb5473af` | `d51192618dea5c8d06e093f33154cbef06d39545ffce1c53e686822199c5a0af` | |
| File checksum (SHA-256, NER) | `d78a18c6926fd6771e2d29407ffa8a77302522690e7ce63f0bb1e3e3eb2e290e` | `a3c353390c4920021c314bfdfe874f9d794a76bfdc73d90b2d08eaab2a2687ed` | |

Processing: `scripts/prepare_rasters.py` reprojects raw `.nc` / `.xyz` subsets to local UTM (`EPSG:32744` for ANS, `EPSG:32745` for NER) using bilinear resampling; `src/geodata.py` aligns gravity onto the bathymetry grid without increasing gravity's native information content.
