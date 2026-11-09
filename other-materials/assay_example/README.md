# drug-computing-examples

Worked examples of **dose-response analysis** on public PXR reporter-assay data from
[OpenADMET/octant-pxr-htchem-blogpost](https://github.com/OpenADMET/octant-pxr-htchem-blogpost):
raw luciferase plate wells → TSV → four-parameter logistic (4PL) fit → potency (EC₅₀ / pEC₅₀) plotted
beside each compound's 2D structure, on identical axes.

## Notebooks

| Notebook | Source data | Compounds | Error bars | pEC₅₀ range | vs. authors' pEC₅₀ |
|---|---|---|---|---|---|
| [dose_response_curve.ipynb](dose_response_curve.ipynb) | OPA_PXR-046, crude library | 20 | none (one well per concentration) | 3.98 – 5.79 | Spearman 0.92 |
| [dose_response_pure_compounds.ipynb](dose_response_pure_compounds.ipynb) | OPA_PXR-032 + 036, pure reference hits (batch AA-004) | 10 | mean ± SD of two runs (n = 2) | 5.91 – 6.88 | Spearman 0.87 |

Both notebooks follow the same steps, each documented in a markdown cell: download raw wells → select
compounds by a fixed rule (evenly spaced across potency) → save raw wells as TSV and read them back →
fit 4PL → plot → cross-check against the authors' published values.

**Pure-compound notebook specifics.** Each compound was run twice, giving real replicates. Pure hits are
potent and often *roll over* (signal falls at high concentration), so only the rising limb is fitted;
excluded points are drawn as hollow markers.

## Method notes

- **Response** is `luci_norm`: luminescence normalised per plate (≈ 0 at negative-control level, 1 = positive
  control; dimensionless). Raw RLU (`luci`) is kept in the TSVs. **Concentration** is in µM.
- **4PL fit** in log₁₀(µM) space, bounded least squares with several starts. pEC₅₀ = −log₁₀(EC₅₀ / M),
  with a 95 % CI from the fit covariance. Each fit gets a quality label (`full curve`, `partial curve`,
  `EC50 above top conc.`, `EC50 poorly constrained`).
- **Every panel in a figure shares the same x- and y-limits.**
- The authors' pEC₅₀ is used only to choose compounds and to cross-check fits, never in the fitting.

## Caveats

- The 046 compounds are **crude, yield-uncorrected** samples, so potencies are apparent values.
- One well per concentration in the 046 data, so its CIs reflect scatter around the curve only.
- An SD from n = 2 is a rough estimate of spread.
- The 80 %-of-peak rollover rule is a pragmatic choice; EC₅₀ then describes activation before signal loss.
- Partial curves (top concentration still on the rising part) have EC₅₀ values that depend on an
  extrapolated plateau.

## Run

```shell
conda activate conda_env          # needs rdkit, scipy, pandas, matplotlib, pillow, nbconvert
cd drug-computing-examples        # notebooks use relative paths: run them from this directory
jupyter nbconvert --to notebook --execute --inplace dose_response_curve.ipynb
jupyter nbconvert --to notebook --execute --inplace dose_response_pure_compounds.ipynb
```

The first run needs network access to download the source files into `data/source_*` (later runs reuse
them). Data belong to OpenADMET/Octant; see the source repository for terms of use.

## File manifest

### Notebooks (executed, outputs included)

| File | Description |
|---|---|
| `dose_response_curve.ipynb` | 20 crude library compounds (OPA_PXR-046): 4PL fits, structures, cross-check |
| `dose_response_pure_compounds.ipynb` | 10 pure compounds, two runs: replicate error bars, rollover handling, 4PL fits |

### Results (`data/`)

| File | Rows | Description |
|---|---|---|
| `pxr_046_raw_20cpds.tsv` | 180 | Raw wells of the 20 selected 046 compounds: `plate, row, col, molecule_name, batch_name, chem_m, conc_uM, luci, luci_norm` |
| `pxr_046_structures_20cpds.tsv` | 20 | `molecule_name, smiles` |
| `pxr_046_fit_results_20cpds.tsv` | 20 | Per compound: `n_points, bottom, top, hill, log_ec50, ec50_uM, pEC50, pEC50_se, pEC50_ci95, rmse, fit_quality, smiles, author_pEC50, delta_pEC50` |
| `pxr_pure_raw_10cpds.tsv` | 180 | Raw wells of the 10 pure compounds, both runs: as above plus `run` (OPA_PXR-032 / OPA_PXR-036) |
| `pxr_pure_structures_10cpds.tsv` | 10 | `molecule_name, smiles` |
| `pxr_pure_fit_results_10cpds.tsv` | 10 | As the 046 fit table, with `n_wells_fit, n_wells_excluded, rollover_from_uM` in place of `n_points` |

### Downloaded source files (`data/source_*`, re-created on first run; safe to delete)

| File | Origin in the source repo (`data/raw/…`) | Content |
|---|---|---|
| `source_046_stats/stats.tsv` | `drc/htchem-libraries/OPA_PXR-046_…/stats.tsv` | Raw per-well data, 228 crude compounds |
| `source_046_cdd/cdd.csv` | `drc/htchem-libraries/CDD CSV Export … OCNT-0002416 …csv` | Processed: SMILES and the authors' fits (no per-well data) |
| `source_OPA_PXR-032/stats.tsv` | `drc/reference-hits/OPA_PXR-032_…/stats.tsv` | Raw per-well data, pure reference hits, run 032 |
| `source_OPA_PXR-036/stats.tsv` | `drc/reference-hits/OPA_PXR-036_…/stats.tsv` | Raw per-well data, pure reference hits, run 036 |
| `source_pure_correlation/correlation.csv` | `master/pxr-challenge_crude-sp-to-pure-correlation.csv` | Processed: SMILES and the authors' pEC₅₀ for the pure compounds |

### Figures (`figures/`)

| File | Description |
|---|---|
| `pxr_046_dose_response_20cpds.png` / `.pdf` | 20 panels (4 × 5): structure above 4PL curve, shared axes |
| `pxr_pure_dose_response_10cpds.png` / `.pdf` | 10 panels (5 × 2): structure above 4PL curve with SD error bars, shared axes |
