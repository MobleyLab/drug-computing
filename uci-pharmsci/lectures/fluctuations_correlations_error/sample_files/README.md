# Supporting/sample files for OpenMM session

## Manifest:

### Provided:
- [`toluene.pdb`](toluene.pdb): PDB file of small molecule tolene, oriented with respect to T4 lysozyme L99A protein. File from `openforcefield` package data folder.
- [`T4-protein.pdb`](T4-protein.pdb): A T4 lysozyme mutant (L99A) which binds toluene and other small molecules. File from `openforcefield` package data folder.
- [`mobley_20524.mol2`](mobley_20524.mol2): Phenol (from FreeSolv) as in the `solvation_free_energies` directory.
- `mobley_20524.prmtop`, `.inpcrd`, `.top`, and `.gro`: Phenol (from FreeSolv) parameterized systems in AMBER and GROMACS formats. In the AMBER case, phenol is in vacuum; in the GROMACS case, in TIP3P water.
- [`input.pdb`]: OpenMM example villin headpiece input pdb (openmm/examples/input.pdb)
- [`density_sample.csv`](desity_sample.csv): Sample density versus time trace for phenol/toluene/cyclohexane mixture (1 molecule, 10 molecules, 100 molecules) generated via `Session2.ipynb`.
- [`host-guest-data`](host-guest-data): Sample short host-guest binding free energy calculation
- `hbonds.ffxml`: FFXML file for constraining hydrogen bonds with SMIRNOFF; from `openforcefield/examples/host-guest-simulation`
- `OA.mol2`, Gibb octa acid host from `openforcefield/examples/host-guest-simulation`

### Potentially generated:
- `mixture_output.pdb`: Output of energy minimization of a mixture
- `guest_in_water`: Output of Session 3 notebook
- `guest.pdb`: Output of Session 3 notebook
- `guest_solvated.xml`: Output of Session 3 notebook
- `complex_solvated.xml`: Output of Session 3 notebook.
