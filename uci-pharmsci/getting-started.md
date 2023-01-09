# Getting your computer ready for PharmSci 175/275

This document, which is a work in progress (contributions welcome), provides information on preparing your computing environment for PharmSci 175/275.

This class involves using a considerable amount of Python and computational chemistry software. There are two main ways you can use this software, requiring rather different setup and requirements:
1) Install and run in the cloud via Google Colab (minimal hardware requirements; may even work on tablets and/or phones)
2) Install and run locally on your computer

Here, we recommend and support the first approach, especially for novice users. The second approach is also documented, but historically poses major challenges for many Windows users (most scientific computing is done in a Linux-like environment, e.g. Mac or Linux) and/or those without significant computing/command-line experience.

Thus, here, we first describe the **Google Colab approach** as recommended for all users, then discuss the local installation approach further down.

The one major **downside of the Google Colab approach is that doing calculations requires your computer to be on, awake, and have internet access**. Some of the assignments in this course can run a few hours or more, so these will require planning (or running overnight) if you are using Google Colab.

## Working on Google Colab

For Google Colab, you will be running everything in the cloud ON Google Colab, which is free. If you plan to go this route (which we recommend unless you have a strong reason to run locally, though see caveat above about internet access) [this getting started notebook](https://github.com/MobleyLab/drug-computing/blob/master/uci-pharmsci/Getting_Started_condacolab.ipynb) can be opened in Colab and used to install/test out the requisite software. (Two getting started notebooks for Colab are provided; the `condacolab` one is probably superior, but the other is a fallback option.)

### Subsequent use of Google Colab

Each time you begin using Google Colab, it's like beginning on a new computer. This means that **before every lecture or assignment, you will need to install the required software on Google Colab**, which takes just a few minutes. In other words, you will need to insert the commands from the [getting started notebook](https://github.com/MobleyLab/drug-computing/blob/master/uci-pharmsci/Getting_Started_condacolab.ipynb) at the beginning of the notebook you will be using on Colab, and run them.

Notebooks we use in class will have pointers to this "getting started" content to remind you of this.

**If you are using Colab, you do not need to read the remainder of this document.**

## Local installation (not for the inexperienced and often problematic for Windows users)

As noted, we can support Google Colab across platforms and even for novices. Local installation requires more expertise, and is often problematic for Windows users.

### Prerequisites

Before getting started, note that the below assumes at least some modest familiarity with the BASH shell and the idea of paths, file names, and basic Linux commands.
If you do not have this familiarity, you may need to consult the [BASH cheat sheet](docs/bash_cheatsheet.jpg) and other sources of information (such as the [Linux/bash crash course](docs/linux_crashcourse.md) here) before proceeding. (MIT's [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/) provides a more complete and diverse introduction in the form of a full course.)

### Setup and Installation - WINDOWS ONLY:

#### SPECIAL CONSIDERATIONS FOR WINDOWS:

If you are on Windows, you basically have three options:
1. Dual boot into Linux (best option, but requires some expertise and/or care to set up, and not something this course will help you do)
2. Use Windows Subsystem for Linux (may work for much but likely not all of the software used in this course)
3. Boot into Linux from a USB drive, e.g. a thumb drive with a persistent Linux distribution

We discuss each of those in turn here:

**Dual boot (WINDOWS ONLY)**:

This is your best option on Windows, but not one we can help you set up. It requires some level of technical expertise/proficiency, not because it is difficult, but because missteps can result in your computer becoming unbootable, e.g. "a brick". This is the best route if you can manage it, but this class cannot support you in going this route, and if you decide to go this route, we are not responsible for any damage you might cause to your computer.

**Windows Subsystem for Linux (WSL)**:

**Install BASH on Windows**: Follow the official guide linked [here](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)

If the BASH terminal guide works and you can successfully use BASH commands (i.e `cd`, `ls`). Now, try performing the installation steps to see if we can get Anaconda/OpenEye installed on your local machine too.

There may be some software we use in this course which does not work well on Windows (specifically, the Windows Subsystem for Linux (WSL) as discussed here) as Windows is not broadly used in scientific computing/our open source stack.

#### Boot to Linux from an USB drive (e.g. thumb drive)

In the past, we have on occasion explored an alternative approach involving bootable USB drives (e.g. thumb drives) with a persistent Linux distribution available pre-installed.
If needed, we can explore this with Dr. Mobley, though it has not been attempted in several years.
Because of hardware differences, it is unlikely that the same installation (below) will work both on a personal laptop and on the computers in the classroom, so you would need to pick one or the other and coordinate with Dr. Mobley.
**If using the USB drive approach**, see [`docs/persistent-usb.md`](docs/persistent-usb.md) for additional information and instructions *before following the below instructions*.

### Setup and Installation: For everyone (except Google Colab)

Here, you will need to complete several main steps in the install, each of which has its own section:
1) Install Anaconda Python and get the repository (inserting a step before this if you're on a Mac with an M1/M2 chip)
2) (Optionally) Configure a conda environment if desired
3) Install gfortran
4) Use f2py3 to compile libraries for lectures/assignments  (sometimes breaks if step (5) is done first)
5) Use conda to finish installing prerequisites
6) Install the OpenEye license

#### 0. For M1/M2 (Apple Silicon) Macs in 2023

If you are on a Mac with an M1/M2 chip in 2023, you need to add an additional step before beginning. Essentailly, since Apple's migration to their own chips, not all software has been packaged for these chips yet, so we need to set up our Macs to install using Intel emulation instead. This involves two parts:
a) Install Rosetta. Open a Terminal (e.g. "Terminal" or, I prefer, iTerm) and run `softwareupdate --install-rosetta. Rosetta is used for running x86 code on an M1/M2 Mac. 
b) Use an Intel/x86 Terminal: Open your Applications folder, make a copy of your preferred terminal application, right click it, choose "get info", and check the "open with Rosetta" box. I suggest renaming this application to have `x86` in its name so you can easily recognize it.

**In everything to follow, you will use the x86 version of the terminal application**, which will ensure you get x86/Intel code which will work consistently.

#### 1. Install Anaconda Python

Download the Anaconda Python 3 installation file or download it from the [website](https://www.anaconda.com/distribution/) or use (from the command prompt); if you are experienced, you can also substitute a Miniconda installation or similar:

(Linux/OSX)
> wget https://repo.anaconda.com/archive/Anaconda3-2022.10-MacOSX-x86_64.sh

(You can get a [related link for Windows or Linux](https://repo.anaconda.com/archive/) and use a similar command.) Note if you are on a Mac, you want the x86_64 one as of 2023 even if you're on an ARM-based Mac..

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
(yours may list a different, more recent Python version, though you will likely need to end up using python 3.8 or 3.9.)

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

#### Get the repository locally

Anytime after Anaconda is installed (and before step 4 involving pre-compiling the libraries), run the following on the command-prompt
```bash
git clone git@github.com:MobleyLab/drug-computing.git
cd drug-computing
```
This checks out (obtains) a copy of this repository so you can work with it and the files in it, if you like (you'll be using this to access lecture content and other materials from this class.) (If you have trouble with this, you may want to try the https version of the command, `git clone https://github.com/MobleyLab/drug-computing.git`)

#### 2. Configure a conda environment if desired; do this if on OS X

Short version: Run `conda create -n drugcomp python=3.8` on the command-line to create a new environment called `drugcomp` then activate this (using `conda activate drugcomp`) whenever you are working on the course.

Long version: Anaconda includes with it the `conda` environment/package manager, meaning that it can also install other software which you need.
Here we will use the `conda` package manager to install the software you need.

**First, you need to decide whether or not to use a conda environment (`env`) for the course**:
- If you have no idea what this means, only just installed anaconda, and do not have an existing set of conda packages you use extensively, you probably do not want to use an `env`
- If you already have an extensive set of packages managed with `conda` and you want to ensure you do not break or modify your existing installation, you probably DO want to create a custom environment (`env`) for this course.

If you are do not need an `env`, just proceed straight to installation.
If you do need an `env`, [use this info](https://conda.io/docs/user-guide/tasks/manage-environments.html) to create a new Python 3.8 conda environment called `drugcomp` (e.g. `conda create -n drugcomp python=3.8`) and activate this environment (`source activate drugcomp`) before doing the installs discussed below.
Whenever you do work for the class, you will need to activate this environment.

#### 3) Install gfortran

For some of our assignments/lectures (energy minimization, MD, MC) we will use `f2py3` to compile some fortran code for use in Python (to make some numerical operations fast), which requires a fortran compiler.

(**2023 Apple M1/M2 Silicon ONLY:** With Mac's M1/M2 processors (Apple silicon) in 2023 we are having issues with gfortran/gcc which necessitate separate install. As of this writing, most packages are available for Apple Silicon, but a couple important packages still are not. This means that we can't get a uniform conda installation to work nicely. The work-around is to conda install everything but gfortran *with the x86 terminal introduced above* then use SourceForge to install an Intel-based gfortran. Specifically, instal the generic (non-M1) gcc and gfortran from SourceForge, [http://hpc.sourceforge.net/](http://hpc.sourceforge.net/). So if you're on an M1/M2 Mac in 2023, visit Sourceforge, download the non-M1 binaries linked at the top of the page (something like `gfortran-11.2-bin.tar.gz`, and follow the instructions there to install).

**If on Mac OS, you also need XCode's command-line tools**:

To use this on OS X, you will need to install the XCode command-line tools via something like `xcode-select --install` from the command-line.
Without this you will get an error message relating to `limits.h` when attempting to execute f2py3.

A subtle problem arises if you install a compiler with conda (e.g. `gcc`) and have XCode installed as well. This can be a source of headache/confusion, so just be aware that multiple compilers will exist on your machine, and care must be taken to ensure only one is used at a time.

#### 4) Use f2py3 to compile the fortran libraries for the course

f2py3 can turn prepared Fortran code into Python libraries; here, we use this for a few computationally intensive portions of the course.

**You should pre-compile the course libraries before finishing installation** as we find that sometimes, subsequent installations in the same conda environment break gfortran.

Using the command-line, pre-compile the relevant libraries listed here:
- assignments:
  - MC/mclib.f90
  - MD/mdlib.f90
  - energy_minimization/emlib.f90
- lectures:
  - MC/mc_sandbox.f90
  - MD/md_sandbox.f90

To compile each, navigate to the relevant directory (which you will have checked out to your local computer from GitHub) and use the command `f2py3 -c -m mclib mclib.f90`, for example (for the MC library); the first argument is the final name of the module and the second argument is the name of the .f90 file. You would execute the above in the `MC` directory, then do a similar thing for the MD assignment/library, energy_minimization assignment/library, and the MC and MD lectures. You should end up with a total of five files, each in the appropriate directory.

(If you fail to pre-compile these libraries, usually this causes no problem and you can compile them later. However, in some cases later installations cause library problems that make this fail. If you encounter problems later, you can fix this issue by creating a clean conda environment later, installing only gfortran, then compiling the libraries. Then you can use them back in your original conda environment.)

#### 5) Use conda to finish installing prerequisites

**Proceed to finish installation**:
```bash
conda config --add channels conda-forge 
conda install parmed --yes
conda install openff-toolkit pdbfixer nb_conda mpld3 scikit-learn seaborn bokeh py3dmol --yes
conda install -c openeye openeye-toolkits --yes
conda install -c anaconda requests
conda install pyemma --yes
# Optional (enables 3D movies in Jupyter notebooks, but can be finicky)
conda install -c conda-forge nglview --yes
```

The above installs quite a variety of software packages and may take a reasonable chunk of time to complete, even on a fairly fast connection.

Specific notebooks/assignments used in class may have additional requirements and in general these will be mentioned at the top of the notebook; you should set aside some extra time to install before using a particular notebook.

Finally, make sure your environment is activated as a kernel for Jupyter notebooks:
`python -m ipykernel install --user --name=drugcomp` (or whatever environment name is being used above) to make sure this environment is activated in the notebook


#### 6) Install the OpenEye license

Download a copy of the `oe_license.txt` OpenEye license file from the course Canvas site, as you will need it for what follows.

Put the license file somewhere safe, where you can find it again, and note the path (directory location) where you put it.
Then do the following, replacing PATHTOFILE with where you put it:


```bash
#Add the OE_LICENSE to your ~/.bash_profile
# (Here, replace <PATHTOFILE> with the path of the place you have put this file)
echo export OE_LICENSE="<PATHTOFILE>/oe_license.txt" >> ~/.bash_profile

```
Verify the installation with:
> oecheminfo.py

The output should look something like:
```
oechem
info.py
Installed OEChem version: 3.1.1.1 platform: osx-clang++-x64 built: 20210708 release name: 2021.1.1

Examples: /Users/dmobley/opt/anaconda3/envs/drugcomp/lib/python3.8/site-packages/openeye/examples
Doc Examples: /Users/dmobley/opt/anaconda3/envs/drugcomp/lib/python3.8/site-packages/openeye/docexamples

code| ext           | description                              |read? |write?
----+---------------+------------------------------------------+------+------
  1 | smi           | Canonical stereo SMILES                  | yes  | yes
  2 | mdl,mol,rxn   | MDL Mol                                  | yes  | yes
  3 | pdb,ent       | PDB                                      | yes  | yes
  4 | mol2,syb      | Tripos MOL2                              | yes  | yes
  5 | usm           | Non-Canonical non-stereo SMILES          | yes  | yes
  6 | ism,isosmi    | Canonical stereo SMILES                  | yes  | yes
  7 | mol2h         | MOL2 with H                              | yes  | yes
  8 | sdf,sd        | MDL SDF                                  | yes  | yes
  9 | can           | Canonical non-stereo SMILES              | yes  | yes
 10 | mf            | Molecular Formula                        | no   | yes
 11 | xyz           | XYZ                                      | yes  | yes
 12 | fasta,seq     | FASTA                                    | yes  | yes
 13 | mopac,pac     | MOPAC                                    | no   | yes
 14 | oeb           | OEBinary v2                              | yes  | yes
 15 | dat,mmd,mmod  | Macromodel                               | yes  | yes
 16 | sln           | Tripos SLN                               | no   | yes
 17 | rdf,rd        | MDL RDF                                  | yes  | no
 18 | cdx           | ChemDraw CDX                             | yes  | yes
 19 | skc           | MDL ISIS Sketch File                     | yes  | no
 20 | inchi         | IUPAC InChI                              | yes  | yes
 21 | inchikey      | IUPAC InChI Key                          | no   | yes
 22 | csv           | Comma Separated Values                   | yes  | yes
 23 | json          | JavaScript Object Notation               | yes  | yes
 24 | cif           | Crystallographic Information File (CIF)  | yes  | no
 25 | oez           | Zstd Compressed OEBinary                 | yes  | yes
 26 | cif           | Macromolecular CIF                       | yes  | no
----+---------------+------------------------------------------+------+------
```

You should doublecheck that the OpenEye installation is working corectly by opening python (on the command prompt) or a [Jupyter notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html) and typing:
```python
from openeye.oechem import *
mol = OEMol()
```
and you should get no errors.

If you have errors with your OpenEye installation and have verified that you have an OpenEye license file, it is in the correct place, and properly listed in your `~/.bash_profile` file, you may need to edit your `~/.bashrc` file to point to your `~/.bash_profile` file. Particularly, I have noticed that on some dual boot installations of Ubuntu in some cases this step may be necessary. You would just add a line to the end of your `~/.bashrc` file that says `source ~/.bash_profile`


#### One additional step

After the above, please also use `jupyter-nbextension enable nglview --py --sys-prefix` on the command-line to enable the `nglview` extension for interactive visualization in Jupyter notebooks.


# Instructor notes

Many of the notebooks are formatted as RISE notebooks which can be presented as slides using the RISE plugin. To get this to work, I have needed to:
- Install as normal (above)
- `conda install -c conda-forge rise` (2023 I had to pip install RISE)
- `conda install git-lfs` for large files
- `python -m ipykernel install --user --name=drugcomp` (or whatever environment is being used above) to make sure this environment is activated in the notebook
- Once installed, if a notebook with RISE slides is active, use option-R to enter the slideshow.

Note that Google Colab and environments without RISE will strip out the RISE formatting from notebooks and make it necessary to re-add it.
