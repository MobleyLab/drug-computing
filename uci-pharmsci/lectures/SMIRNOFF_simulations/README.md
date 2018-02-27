# PharmSci 175/275: The SMIRNOFF force field format and simulations of mixtures and host-guest systems with OpenMM

## Manifest

### Core content
- `mixture_simulations.ipynb`: A Jupyter notebook for conducting simple mixture simulations, where setup is done with SolvationToolkit and simulations with OpenMM. Builds on/has some similarity to previous examples seen relating to density in the `fluctuations_correlations_error` lecture.
- `smirnoff_host_guest.ipynb`: Sets up a simulation of a guest in a host (a miniature version of ligand-receptor binding) using the SMIRNOFF force field and minimizes/runs some dynamics in OpenMM. Adapted from an example I prepared in the `openforcefield` repo at https://github.com/openforcefield/openforcefield/tree/master/examples/host_guest_simulation .
- `OpenFF_effort`: PDF and Keynote of slides that I'll show part of to introduce the format and force field.

### Supporting files
- `hbonds.ffxml`, `OA.mol2` -- files used by the `smirnoff_host_guest.ipynb` notebook
