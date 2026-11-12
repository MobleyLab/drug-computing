# drug-computing-examples

Worked examples of **dose-response analysis** on public PXR reporter-assay data from
[OpenADMET/octant-pxr-htchem-blogpost](https://github.com/OpenADMET/octant-pxr-htchem-blogpost):
raw luciferase plate wells → TSV → four-parameter logistic (4PL) fit → potency (EC₅₀ / pEC₅₀) plotted
beside each compound's 2D structure, on identical axes.

## Assay and data source

PXR agonism in a GAL4-PXR reporter cell line: 1536-well plates, 18–24 h compound incubation, Nano-Glo
luciferase readout, 9-point dose-response curves from 5 nM to 50 µM
([assay protocol](https://github.com/OpenADMET/octant-pxr-htchem-blogpost/blob/main/data/raw/protocols/PXR%20Activation%20Assay%20Protocol.md)).
The data come from the OpenADMET/Octant blog post
[Navigating PXR Chemical Space with High-Throughput Chemistry and Standard-Free Quantification](https://openadmet.github.io/octant-pxr-htchem-blogpost/)
and its [repository](https://github.com/OpenADMET/octant-pxr-htchem-blogpost). The post is about the
CAD-based yield correction of crude-sample potencies (not applied in these notebooks); it does not describe
the curve fitting, so the fits here are independent of the authors'. The repository's
[data dictionary](https://github.com/OpenADMET/octant-pxr-htchem-blogpost/blob/main/data/raw/master/PXR_CAD_Blog_Post_Master_Raw_Data_README.md)
documents the authors' potency and uncertainty conventions.

## Notebooks

| Notebook | Source data | Compounds | Error bars | pEC₅₀ range | vs. authors' pEC₅₀ |
|---|---|---|---|---|---|
| [dose_response_curve.ipynb](dose_response_curve.ipynb) | OPA_PXR-046, crude library | 20 | none (one well per concentration) | 4.32 – 5.79 | Spearman 0.97 |
| [dose_response_pure_compounds.ipynb](dose_response_pure_compounds.ipynb) | OPA_PXR-032 + 036, pure reference hits (batch AA-004) | 10 | mean ± SD of two runs (n = 2) | 5.91 – 6.88 | Spearman 0.87 |

Both notebooks follow the same steps, each documented in a markdown cell: download raw wells → select
compounds by a fixed rule (evenly spaced across potency) → save raw wells as TSV and read them back →
fit 4PL → plot → cross-check against the authors' published values.

**Pure-compound notebook specifics.** Each compound was run twice, giving real replicates. Pure hits are
potent and often *roll over* (signal falls at high concentration), so only the rising limb is fitted;
excluded points are drawn as hollow markers.

## Method notes

- **Response** is `luci_norm`: (`luci` − plate negative-control mean) / (positive-control window), so the
  negative-control level is 0 and the positive-control level is 1 (dimensionless). It is exactly
  linear in `luci` on every plate of all three source files (verified). The positive-control wells themselves
  are not in the files. Raw RLU (`luci`) is kept in the TSVs. **Concentration** is in µM.
- **4PL fit** in log₁₀(µM) space, bounded least squares with several starts, identical code in both notebooks;
  pEC₅₀ = −log₁₀(EC₅₀ / M). Only the settings differ:

  | | 046 (crude, one well per concentration) | pure (two runs pooled, 14–18 wells per curve) |
  |---|---|---|
  | baseline (`bottom`) | fixed at 0, the negative-control level (the authors also anchor it at the per-plate negative-control mean) | free, −0.2…0.2 |
  | plateau (`top`) | 0…2 | 0…3 |
  | Hill slope | 0.3…5 | 0.3…5 |
  | log₁₀ EC₅₀ | within one decade of the tested range | within one decade of the fitted range |

  The cap of 2 on the 046 plateau comes from the authors' fits to the whole library (largest Emax 1.77, none
  above 2; checked in the notebook). It only matters for partial curves. With the earlier settings (baseline
  free, top ≤ 3) two 046 fits ran to `top` = 3 and disagreed with the authors by 0.82 and 0.53 log units; with
  the fixed baseline and cap the agreement over the 20 compounds improved from Spearman 0.92 to 0.97 and from
  RMSE 0.28 to 0.14 log units. The pure notebook keeps the baseline free: fixing it did not improve its
  agreement with the authors.
- **Uncertainty.** Two intervals are stored. `pEC50_se` / `pEC50_ci95` come from the fit covariance
  (95 % CI = SE × t(0.975, n − p); the authors use 1.96 × SE, slightly narrower). `pEC50_lo` / `pEC50_hi` are the
  95 % **profile-likelihood** interval (EC₅₀ fixed on a grid, other parameters refitted, F-test threshold on
  the sum of squares), which is asymmetric and stays meaningful when a parameter sits on a bound. The profile
  interval is the one shown in the notebooks' tables and plots (`pEC50_report`).
- **Bound-only reporting.** An end of the profile interval is not reported when the data do not close it: the
  threshold is not crossed within the EC₅₀ search range, or the crossing is set by the plateau cap rather than
  by the data. If the weak-potency end is open, only an upper limit on pEC₅₀ is reported (`pEC50 ≤ x`, i.e.
  EC₅₀ ≥ y µM), the panel states the bound instead of a point value and no EC₅₀ line is drawn. This applies to
  5 of the 20 046 fits (`OCNT-2433726`, `-2433530`, `-2433692`, `-2433615`, `-2433543`) and 2 of the 10 pure
  fits (`OCNT-2317134`, `-2318311`). In the cross-check scatter they are hollow points.
- **Quality label** (`full curve`, `partial curve`, `EC50 above top conc.`, `EC50 below lowest conc.`, and in
  the pure notebook `EC50 poorly constrained`) describes the fitted curve; the interval describes what the data
  support, and the two can disagree (e.g. `OCNT-2318311` is a `full curve` whose weak-potency end is open).
- **`top_at_bound`** is `True` when the fitted `top` sits on its bound (0 or the cap: 2 in the 046 notebook,
  3 in the pure one), i.e. the data did not determine the plateau and `top` and EC₅₀ depend on the bound
  chosen. In the 046 table it flags `OCNT-2433726` and `OCNT-2433543` (`top` = 2, Δ pEC₅₀ vs. the authors of
  −0.22 and −0.19); treat their pEC₅₀ as unreliable whatever the quality label says. It is stored in the fit
  TSVs and shown in the fit tables, not marked on the figures.
- **Every panel in a figure shares the same x- and y-limits.**
- The authors' pEC₅₀ is used only to choose compounds and to cross-check fits, never in the fitting.

## Caveats

- The 046 compounds are **crude, yield-uncorrected** samples, so potencies are apparent values.
- One well per concentration in the 046 data, so its intervals reflect scatter around the curve only.
- An SD from n = 2 is a rough estimate of spread.
- The 80 %-of-peak rollover rule is a pragmatic choice; EC₅₀ then describes activation before signal loss.
- Partial curves (top concentration still on the rising part) have EC₅₀ values that depend on an
  extrapolated plateau. The fixed baseline and the plateau cap are modelling choices: a different cap
  changes the EC₅₀ of capped fits, which is why only a bound is reported for them.
- The authors' fits are not ground truth: they report EC₅₀ values far above the top concentration (no
  censoring) and pass confidence intervals up to about 2.6 log units wide.

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
| `pxr_046_fit_results_20cpds.tsv` | 20 | Per compound: `n_points, bottom, top, hill, log_ec50, ec50_uM, pEC50, pEC50_se, pEC50_ci95, rmse, top_at_bound, pEC50_lo, pEC50_hi, pEC50_report, fit_quality, smiles, author_pEC50, delta_pEC50` (`bottom` is the fixed baseline, 0; `pEC50_lo` / `pEC50_hi` are empty where the data do not close that end) |
| `pxr_pure_raw_10cpds.tsv` | 180 | Raw wells of the 10 pure compounds, both runs: as above plus `run` (OPA_PXR-032 / OPA_PXR-036) |
| `pxr_pure_structures_10cpds.tsv` | 10 | `molecule_name, smiles` |
| `pxr_pure_fit_results_10cpds.tsv` | 10 | As the 046 fit table, with `n_wells_fit, n_wells_excluded, rollover_from_uM` in place of `n_points` (`bottom` is fitted here) |

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
| `pxr_046_dose_response_20cpds.png` / `.pdf` | 20 panels (4 × 5): structure above 4PL curve, shared axes; potency box with the 95 % profile range or a bound |
| `pxr_pure_dose_response_10cpds.png` / `.pdf` | 10 panels (5 × 2): structure above 4PL curve with SD error bars, shared axes; potency box with the 95 % profile range or a bound |
