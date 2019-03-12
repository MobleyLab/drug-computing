# Visualization with PyMol and VMD

This directory contains content relating to visualization with both PyMol and VMD.
VMD is more commonly used for visualization of molecular simulations; however, PyMol is perhaps a better general-purpose viewer for biomolecules if you are not visualizing simulations.
As of the 2017-2018 school year we are shifting to primarily instructing on use of VMD; however, legacy material on PyMol is also provided here, and students may choose either piece of software for use in the class and for (if selected) the visualization assignment.

## Manifest
(Keynote note: The large Keynote files in this directory present only as small placeholders if you cloned the repository with normal `git`; to obtain them you would need to install `git-lfs` and then use `git-lfs pull` to obtain the files. Otherwise only placeholder files will be present.)

- `PyMol`: Keynote and PDF; old lecture content relating to PyMol usage, by David Mobley.
- `VMD`: Keynote and PDF; 2018 lecture content relating to VMD usage, by Nathan Lim.
- `pymol_files`: Supplemental files relating to the PyMol lecture (e.g. sample movie files referenced therein)
- `pymol_tutorial.md`: Tutorial content relating to PyMol, useful if you choose to use PyMol rather than VMD for the visualization assignment.
- `BACE1.pdb`: PDB file from Lea El Khoury and Sukanya Sasmal (Mobley lab) of a BACE1 inhibitor bound to BACE, from the D3R 2018 grand challenge. Can be used with OpenEye's example code https://docs.eyesopen.com/toolkits/cookbook/python/visualization/activesitemaps.html to generate a 2D interaction map, as shown in the file `interaction_map.svg` here.
- `interaction_map.svg`: Sample interaction map, as noted in previous point.
