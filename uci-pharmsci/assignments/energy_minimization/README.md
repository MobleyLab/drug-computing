# Materials/assignment for energy minimization

## Manifest
- [energy_minimization_assignment.ipynb](energy_minimization_assignment.ipynb): Jupyter notebook for energy minimzation assignment; also provided in HTML format
- `emlib.f90`: Fortran (90) library to be compiled with f2py/f2py3/numpy.f2py for use in energy minimization assignment
- Miscellaneous graphics files: Files which support the assignment.

## Troubleshooting

One of the main places to go wrong early in this assignment is if you cannot compile the fortran library via `f2py3 -c -m emlib emlib.f90` or similar (please consult the NumPy documentation).

