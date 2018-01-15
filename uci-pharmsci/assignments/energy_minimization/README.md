# Materials/assignment for energy minimization

## Manifest
- [energy_minimization_assignment.ipynb](energy_minimization_assignment.ipynb): Jupyter notebook for energy minimzation assignment; also provided in HTML format
- `emlib.f90`: Fortran (90) library to be compiled with f2py for use in energy minimization assignment
- Miscellaneous graphics files: Files which support the assignment.

## Troubleshooting

One of the main places to go wrong early in this assignment is if you cannot compile the fortran library via `f2py -c -m emlib emlib.f90`.
On my Ubuntu (dual boot) computer with an intel processor, this fails because I don't have a fortran compiler; apparently `conda` failed to correctly install gcc/gfortran when following the [getting started info](../getting-started.md) due to issues with missing libraries (specifically `sys/cdefs.h`).
After some Googling, [this thread](https://askubuntu.com/questions/470796/fatal-error-sys-cdefs-h-no-such-file-or-directory) suggests installing g++-multilib first, so I did so (via `sudo apt-get install g++-multilib`).
This takes some time, but after that, `conda install gcc libgfortran` proceeds correctly and I'm able to compile `emlib.f90`.
