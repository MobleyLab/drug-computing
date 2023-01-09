# Solvation free energy calculations with Yank

This provides example materials for solvation free energy calculations with implicit and explicit solvent in Yank. You would need to install Yank first.
Demonstrations are set up for hydration free energy calculations on FreeSolv and/or FreeSolvMini.

I validated this, in the implicit solvent case, for phenol from IUPAC name, SMILES, and FreeSolv (mobley_20524.mol2) and get consistent values -- basically -10.08+/-0.01 kT in all cases. 

## Manifest
- run_hydration.py: Sets up and runs a Yank hydration free energy calculation in implicit or explicit solvent, for a single molecule. Can use mol2/pdb/sdf input, or SMILES/name. Basically provides an interface to set up Yank YAML input. For usage info, see `python run_hydration.py -h`
- mobley_9979854.mol2: A selected molecule from the FreeSolv database for testing purposes

## Requirements
Ensure you have a working installation of anaconda python (or miniconda); see [getting started](../../uci-pharmsci/getting-started.md) if you do not.
Then use `conda install -c omnia yank` to ensure you have the `yank` package installed.

## Acknowledgments
Material here draws heavily on work of John Chodera's group and his Yank package (and utilizes the Yank package).
Some of the templates here come from the FreeSolv cube developed for OpenEye's Orion platform (https://github.com/oess/openmm_orion/commit/9bb2f55d416acae8b6f31647e918a520c624bc6e) and written by John Chodera.
