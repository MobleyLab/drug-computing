# Getting your computer ready for PharmSci 175/275

This document, which is a work in progress (contributions welcome), provides information on what you need to install and how in order for your computer to be ready for PharmSci 175/275.

## Prerequisites

Before getting started, note that the below assumes at least some modest familiarity with the BASH shell and the idea of paths, file names, and basic Linux commands.
If you do not have this familiarity, you may need to consult the [BASH cheat sheet](docs/bash_cheatsheet.jpg) and other sources of information (such as the [Linux/bash crash course](docs/linux_crashcourse.md) here) before proceeding. (MIT's [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/) provides a more complete and diverse introduction in the form of a full course.)

## Setup and Installation - WINDOWS ONLY:

### SPECIAL CONSIDERATIONS FOR WINDOWS:

If you are on Windows, you basically have three options:
1. Dual boot into Linux (best option, but requires some expertise and/or care to set up, and not something this course will help you do)
2. Use Windows Subsystem for Linux (may work for much but likely not all of the software used in this course)
3. Boot into Linux from a USB drive, e.g. a thumb drive with a persistent Linux distribution

We discuss each of those in turn here:

#### Dual boot (WINDOWS ONLY)

This is your best option on Windows, but not one we can help you set up. It requires some level of technical expertise/proficiency, not because it is difficult, but because missteps can result in your computer becoming unbootable, e.g. "a brick". This is the best route if you can manage it, but this class cannot support you in going this route.

### Windows Subsystem for Linux (WSL)

**Install BASH on Windows**: Follow the official guide linked [here](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)

If the BASH terminal guide works and you can successfully use BASH commands (i.e `cd`, `ls`). Now, try performing the installation steps to see if we can get Anaconda/OpenEye installed on your local machine too.

There may be some software we use in this course which does not work well on Windows (specifically, the Windows Subsystem for Linux (WSL) as discussed here) as Windows is not broadly used in scientific computing/our open source stack.

### Boot to Linux from an USB drive (e.g. thumb drive)

In the past, we have on occasion explored an alternative approach involving bootable USB drives (e.g. thumb drives) with a persistent Linux distribution available pre-installed.
If needed, we can explore this with Dr. Mobley, though it has not been attempted in several years.
Because of hardware differences, it is unlikely that the same installation (below) will work both on a personal laptop and on the computers in the classroom, so you would need to pick one or the other and coordinate with Dr. Mobley.
**If using the USB drive approach**, see [`docs/persistent-usb.md`](docs/persistent-usb.md) for additional information and instructions *before following the below instructions*.

## Setup and Installation: For everyone

### Anaconda Python
Download the Anaconda Python 3 installation file or download it from the [website](https://www.anaconda.com/distribution/) or use (from the command prompt):

(Linux/OSX)
> wget https://repo.anaconda.com/archive/Anaconda3-2021.05-MacOSX-x86_64.sh

(You can get a related link for Windows or Linux and use a similar command.)

Install Anaconda (this may take 15-30mins), filling in the "fill in the rest here" part with the appropriate name of the file you downloaded above (or run the interactive installer if you downloaded that):
> bash Anaconda_fillintheresthere.sh -b

Make sure the anaconda3 path is added to your `~/.bash_profile` (often this is automatically added by the installer, but make sure it ends up there), e.g. via:
>echo 'PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.bash_profile

When it asks you to add Anaconda to your bash shell PATH, select **YES**.
(If you are using a different shell, you need to make a similar change to your shell's configuration.)

Check that Anaconda installed properly by first running `which python`, which should show your newly installed python, e.g.:
```
#: which python
$HOME/anaconda3/bin/python
```
To ensure it works, run the command `python` in a new terminal. Its output should look something like:
```
Python 3.8.8 (default, April 13 2021, 12:59:45)
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Type `exit()` or ctrl-d ("control-d") to leave the python shell.

**Troubleshooting python**

If `which python` just gives a blank line, then it means it cannot find any python in your `$PATH`. Ensuring that `~/.bash_profile` was modified correctly, use `grep -c anaconda3/bin ~/.bash_profile` and check that it prints a number greater than 0 (0 means not found). If you do get 0, then go back and follow the above steps. Now, try to source it (`source ~/.bash_profile`) and repeat the checks above. If it works this time, it means your terminal is not sourcing `~/.bash_profile` automatically. Some OS e.g. certain linux distributions, will source `~/.bashrc` rather than `~/.bash_profile`, since `bash_profile` is only sourced for login shells (this is a technicality not important here). A common thing to do is put everything in bashrc, and have bash_profile source it, ensuring every terminal will work the same:
```
$: cat ~/.bash_profile
# /etc/skel/.bash_profile

# This file is sourced by bash for login shells.  The following line
# runs your .bashrc and is recommended by the bash info pages.
[[ -f ~/.bashrc ]] && . ~/.bashrc
```
where `cat` is a program that prints the file. The last line is bash code for "if ~/.bashrc is a file, then source it" where `. ~/.bashrc` is short for `source ~/.bashrc` and `~` is short for `$HOME`.

**Q: What if `which python` shows a python that is not from anaconda3?**
Then another python is installed on your system, and you likely did not follow the above steps regarding modifying `$PATH`. If you prefer to not have anaconda load its own python for every terminal, you can add the following to your `~/.bashrc`:

```
alias miniconda="source ~/miniconda3/etc/profile.d/conda.sh; conda           activate base"
```

where `alias` is essentially a macro. The conda.sh is what is normally sourced by automatic vanilla installation, and will modify `$PATH` to give its own python first choice. This will then activate a "base" environment, which you may or may not want to use (see below in the next section).

**Q: Anaconda versus miniconda?**
The only difference is the inclusion of GUI (graphical user interface) and a lot of prepackaged software in the full Anaconda installation given above. You may opt to install miniconda instead, which provides the exact same terminal functionality, and only installs the basics (python, conda, etc.). As a quick comparison, Anaconda is ~500MB where miniconda is ~50MB. See [this thread](https://stackoverflow.com/questions/45421163/anaconda-vs-miniconda) for more discussion).

Go to [https://conda.io/en/latest/miniconda.html] to download miniconda.

### Conda install requirements

Anaconda includes with it the `conda` environment/package manager, meaning that it can also install other software which you need.
Here we will use the `conda` package manager to install the software you need.

**First, you need to decide whether or not to use a conda environment (`env`) for the course**:
- If you have no idea what this means, only just installed anaconda, and do not have an existing set of conda packages you use extensively, you probably do not want to use an `env`
- If you already have an extensive set of packages managed with `conda` and you want to ensure you do not break or modify your existing installation, you probably DO want to create a custom environment (`env`) for this course.

If you are do not need an `env`, just proceed straight to installation.
If you do need an `env`, [use this info](https://conda.io/docs/user-guide/tasks/manage-environments.html) to create a new Python 3.8 conda environment called `drugcomp` (e.g. `conda create -n drugcomp python=3.8`) and activate this environment (`source activate drugcomp`) before doing the installs discussed below.
Whenever you do work for the class, you will need to activate this environment.

**Then proceed to installation**:

Once Anaconda is installed, run the following on the command-prompt
```bash
git clone git@github.com:MobleyLab/drug-computing.git
cd drug-computing
```
This checks out (obtains) a copy of this repository so you can work with it and the files in it, if you like (you'll be using this to access lecture content and other materials from this class.) (If you have trouble with this, you may want to try the https version of the command, `git clone https://github.com/MobleyLab/drug-computing.git`)

Then do the following additional installs (**except** if you are using a USB stick Ubuntu installation in 2018, in which case you should replace the first `conda install gcc libgfortran` command with the information [here](docs/persistent-usb.md/#troubleshooting), then follow the rest of the commands after it):
```bash
#Install the gcc and gfortran compilers
conda install gcc libgfortran

# Install OpenMM, openforcefield, yank, parmed, and openmoltools
conda install -c omnia openmm openforcefield parmed yank openmoltools pdbfixer solvationtoolkit

# Install plotting stuff and other prerequisites such as numerical libraries
conda install -c conda-forge nb_conda mpld3 scikit-learn seaborn numpy matplotlib bokeh
# Interactive visualization in jupyter notebooks
conda install -c bioconda nglview
```
The above installs quite a variety of software packages and may take a reasonable chunk of time to complete, even on a fairly fast connection.

Specific notebooks/assignments used in class may have additional requirements and in general these will be mentioned at the top of the notebook; you should set aside some extra time to install before using a particular notebook.


### Install OpenEye toolkits

Download a copy of the `oe_license.txt` OpenEye license file from the course website, as you will need it for what follows.
Put this somewhere safe, where you can find it again, and note the path (directory location) where you put it.
Then do the following:


```bash
#Add the OE_LICENSE to your ~/.bash_profile
# (Here, replace <PATHTOFILE> with the path of the place you have put this file)
echo export OE_LICENSE="<PATHTOFILE>/oe_license.txt" >> ~/.bash_profile

#Install the OpenEye package and toolkits and the oenotebook Jupyter helper
pip install -i https://pypi.anaconda.org/OpenEye/simple OpenEye-toolkits
pip install --extra-index-url https://pypi.org/simple --extra-index-url https://pypi.anaconda.org/openeye/simple/ -i https://pypi.anaconda.org/openeye/label/oenotebook/simple openeye-oenotebook
```
Verify the installation with:
> oecheminfo.py

The output should look something like:
```
Installed OEChem version: 2.1.1 platform: linux-g++4.x-x64 built: 20170210

Examples: /home/limn1/anaconda3/envs/drugcomp/lib/python3.5/site-packages/openeye/examples
Doc Examples: /home/limn1/anaconda3/envs/drugcomp/lib/python3.5/site-packages/openeye/docexamples

code| ext           | description                      |read? |write?
----+---------------+----------------------------------+------+------
  1 | smi           | Canonical stereo SMILES          | yes  | yes
  2 | mdl,mol,rxn   | MDL Mol                          | yes  | yes
  3 | pdb,ent       | PDB                              | yes  | yes
  4 | mol2,syb      | Tripos MOL2                      | yes  | yes
  5 | usm           | Non-Canonical non-stereo SMILES  | yes  | yes
  6 | ism,isosmi    | Canonical stereo SMILES          | yes  | yes
  7 | mol2h         | MOL2 with H                      | yes  | yes
  8 | sdf,sd        | MDL SDF                          | yes  | yes
  9 | can           | Canonical non-stereo SMILES      | yes  | yes
 10 | mf            | Molecular Formula                | no   | yes
 11 | xyz           | XYZ                              | yes  | yes
 12 | fasta,seq     | FASTA                            | yes  | yes
 13 | mopac,pac     | MOPAC                            | no   | yes
 14 | oeb           | OEBinary v2                      | yes  | yes
 15 | dat,mmd,mmod  | Macromodel                       | yes  | yes
 16 | sln           | Tripos SLN                       | no   | yes
 17 | rdf,rd        | MDL RDF                          | yes  | no
 18 | cdx           | ChemDraw CDX                     | yes  | yes
 19 | skc           | MDL ISIS Sketch File             | yes  | no
 20 | inchi         | IUPAC InChI                      | no   | yes
 21 | inchikey      | IUPAC InChI Key                  | no   | yes
 22 | csv           | Comma Separated Values           | yes  | yes
 23 | json          | JavaScript Object Notation       | yes  | yes
----+---------------+----------------------------------+------+------
```

You should doublecheck that the OpenEye installation is working corectly by opening python (on the command prompt) or a [Jupyter notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html) and typing:
```python
from openeye.oechem import *
mol = OEMol()
```
and you should get no errors.

If you have errors with your OpenEye installation and have verified that you have an OpenEye license file, it is in the correct place, and properly listed in your `~/.bash_profile` file, you may need to edit your `~/.bashrc` file to point to your `~/.bash_profile` file. Particularly, I have noticed that on USB installations of Ubuntu in some cases this step may be necessary. You would just add a line to the end of your `~/.bashrc` file that says `source ~/.bash_profile`

### Additions for Macintosh (OS X)
For some of our assignments (energy minimization, MD, MC) we will use `f2py` to compile some fortran code for use in Python (to make some numerical operations fast).
To use this on OS X, you will need to install XCode (developer tools) from the Mac App Store, and then on the terminal, execute `xcode-select --install` to install the XCode command-line tools.
Without this you will get an error message relating to `limits.h` when attempting to execute f2py.

A subtle problem arises if you install a compiler with conda (e.g. `gcc`) and have XCode installed as well. This can be a source of headache/confusion, so just be aware that multiple compilers will exist on your machine, and care must be taken to ensure only one is used at a time.

### One additional step

After the above, please also use `jupyter-nbextension enable nglview --py --sys-prefix` on the command-line to enable the `nglview` extension for interactive visualization in Jupyter notebooks.
