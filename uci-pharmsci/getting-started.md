# Getting your computer ready for PharmSci 175/275

This document, which is a work in progress (contributions welcome), provides information on preparing your computing environment for PharmSci 175/275.

This class involves using a considerable amount of Python and computational chemistry software. There are two main ways you can use this software, requiring rather different setup and requirements:
1) Install and run in the cloud via Google Colab (minimal hardware requirements; may even work on tablets and/or phones)
2) Install and run locally on your computer

Here, we recommend and support the first approach, especially for novice users. The second approach is also documented, but historically poses major challenges for many Windows users (most scientific computing is done in a Linux-like environment, e.g. Mac or Linux) and/or those without significant computing/command-line experience.

Thus, here, we first describe the **Google Colab approach** as recommended for all users, then discuss the local installation approach further down.

The one major **downside of the Google Colab approach is that doing calculations requires your computer to be on, awake, and have internet access**. Some of the assignments in this course can run a few hours or more, so these will require planning (or running overnight) if you are using Google Colab.

## Working on Google Colab

For Google Colab, you will be running everything in the cloud ON Google Colab, which is free. If you plan to go this route (which we recommend unless you have a strong reason to run locally, though see caveat above about internet access) [this getting started notebook](https://github.com/MobleyLab/drug-computing/blob/master/uci-pharmsci/Getting_Started.ipynb) can be opened in Colab and used to install/test out the requisite software.

Typical notebooks here contain an "Open in Google Colab" button you can use, so e.g. click on the notebook on GitHub, open a preview of it, then click "Open in Google Colab". Occasionally, on some browser configurations, however, the GitHub preview will not load, so you need another mechanism to access the notebook. For this, use [NBViewer](https://nbviewer.org/). It allows you to enter a URL of any Jupyter notebook (such as one on GitHub as in this course) and it will display it to you in the browser, then you can click through to Colab. Alternatively, you can download the Jupyter notebook from GitHub and upload it Colab yourself. 

### Subsequent use of Google Colab

Each time you begin using Google Colab, it's like beginning on a new computer. This means that **before every lecture or assignment, you will need to install the required software on Google Colab**, which takes just a few minutes. In other words, you will need to insert the commands from the [getting started notebook](https://github.com/MobleyLab/drug-computing/blob/master/uci-pharmsci/Getting_Started.ipynb) at the beginning of the notebook you will be using on Colab, and run them.

Notebooks we use in class will have pointers to this "getting started" content to remind you of this.

**If you are using Colab, you do not need to read the remainder of this document.**

## Local installation (not for the inexperienced and often problematic for Windows users)

As noted, we can support Google Colab across platforms and even for novices. Local installation requires more expertise, and is often problematic for Windows users.

### Prerequisites

Before getting started, note that the below assumes at least some modest familiarity with the BASH/zsh shell and the idea of paths, file names, and basic Linux commands.
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
1) Install the mamba package manager via mambaforge (a lot like conda, but faster)
2) Configure a virtual environment
3) Install gfortran
4) Use f2py to compile libraries for lectures/assignments  (sometimes breaks if step (5) is done first)
5) Use mamba to finish installing prerequisites
6) Install the OpenEye license

#### 1. Install the mamba package manager

(This, and much of the following, generally follows the [OpenFF install guide](https://docs.openforcefield.org/en/latest/install.html) which is well maintained and has a lot of the same prerequisites).

Download the appropriate MambaForge/MiniForge installer [from the repository](https://github.com/conda-forge/miniforge?tab=readme-ov-file#user-content-mambaforge). If you are on OS X, use an installer ending with "MacOSX-x86_64". 

Then, from the command line (terminal), run 
> bash Mambaforge-(rest of name).sh 
or 
> bash Miniforge-(rest of name).sh
where you fill in the rest of the name as appropriate for what you downloaded.

As per the OpenFF instructions:
- When asked for an install destination, choose a directory owned by your user account (such as the default).
- When asked if you’d like to initialize MambaForge, answer “yes”.
- Once the installer is finished, close the terminal window, open a new one, and run:
> conda config --set auto_activate_base false

#### Get the repository locally

Anytime after mamba is installed (and before step 4 involving pre-compiling the libraries), run the following on the command-prompt
```bash
git clone git@github.com:MobleyLab/drug-computing.git
cd drug-computing
```
This checks out (obtains) a copy of this repository so you can work with it and the files in it, if you like (you'll be using this to access lecture content and other materials from this class.) (If you have trouble with this, you may want to try the https version of the command, `git clone https://github.com/MobleyLab/drug-computing.git`)

#### 2. Configure a virtual environment

Install the desired packages into a new virtual environment named `drugcomp` using:
> mamba create -c conda-forge -n drugcomp openff-toolkit-examples

This uses a recipe provided by OpenFF to create a new virtual environment containing most of what we will need for the course. (For those who want to peek inside the recipe, it's roughly [here](https://github.com/conda-forge/openff-toolkit-feedstock/blob/main/recipe/meta.yaml#L79-L95) and installs python, nglview, notebook, several qc packages, openmmforcefields, pdbfixer and a couple of others, along with their dependencies.) 

This step may take a while, depending on the speed of your connection, as quite a bit needs to be downloaded.
 
Whenever you do work for the class, you will need to activate this environment via `mamba activate drugcomp`

#### 3) Install gfortran

For some of our assignments/lectures (energy minimization, MD, MC) we will use `f2py` to compile some fortran code for use in Python (to make some numerical operations fast), which requires a fortran compiler.

**If on Mac OS, you also need XCode's command-line tools**:

To use this on OS X, you will need to install the XCode command-line tools via something like `xcode-select --install` from the command-line.
Without this you will get an error message relating to libraries or includes (perhaps `limits.h`) when attempting to execute f2py.

After installing xcode's tools, do
``mamba install gfortran``
and accept in order to install.

In 2025, also ``mamba install meson``; apparently gfortran recently switched platforms so this is required.

A subtle problem arises if you install a compiler with mamba/conda (e.g. `gcc`) and have XCode installed as well. This can be a source of headache/confusion, so just be aware that multiple compilers will exist on your machine, and care must be taken to ensure only one is used at a time.

#### 4) Use f2py to compile the fortran libraries for the course

f2py (packed with numpy) can turn prepared Fortran code into Python libraries; here, we use this for a few computationally intensive portions of the course.

**You should pre-compile the course libraries before finishing installation** as we find that sometimes, subsequent installations in the same mamba environment break gfortran.

Using the command-line, pre-compile the relevant libraries listed here:
- assignments:
  - MC/mclib.f90
  - MD/mdlib.f90
  - energy_minimization/emlib.f90
- lectures:
  - MC/mc_sandbox.f90
  - MD/md_sandbox.f90

To compile each, navigate to the relevant directory (which you will have checked out to your local computer from GitHub) and use the command `f2py -c -m mclib mclib.f90`, for example (for the MC library); the first argument is the final name of the module and the second argument is the name of the .f90 file. You would execute the above in the `MC` directory, then do a similar thing for the MD assignment/library, energy_minimization assignment/library, and the MC and MD lectures. You should end up with a total of five files, each in the appropriate directory.

(If you fail to pre-compile these libraries, usually this causes no problem and you can compile them later. However, in some cases later installations cause library problems that make this fail. If you encounter problems later, you can fix this issue by creating a clean mamba environment later, installing only gfortran, then compiling the libraries. Then you can use them back in your original mamba environment.)

#### 5) Use mamba to finish installing prerequisites

**Proceed to finish installation**:
```bash
mamba install -c openeye openeye-toolkits --yes
mamba install -c conda-forge requests
```

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
oecheminfo.py
Installed OEChem version: 3.4.0.1 debug platform: osx-clang++-universal built: 20230910 release name: 2023.1.1

Examples: /Users/dmobley/mambaforge/envs/openff/lib/python3.11/site-packages/openeye/examples
Doc Examples: /Users/dmobley/mambaforge/envs/openff/lib/python3.11/site-packages/openeye/docexamples

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
 24 | cif           | Crystallographic Information File (CIF)  | yes  | yes
 25 | oez           | Zstd Compressed OEBinary                 | yes  | yes
 26 | cif           | Macromolecular CIF                       | yes  | yes
 27 | cxsmiles      | Chemaxon Extended SMILES                 | yes  | yes
----+---------------+------------------------------------------+------+------
```

You should doublecheck that the OpenEye installation is working corectly by opening python (on the command prompt) or a [Jupyter notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html) and typing:
```python
from openeye.oechem import *
mol = OEMol()
```
and you should get no errors.

If you have errors with your OpenEye installation and have verified that you have an OpenEye license file, it is in the correct place, and properly listed in your appropriate profile file (e.g. `~/.bash_profile` or ~/.zshrc or similar).


# Instructor notes

Many of the notebooks are formatted as RISE notebooks which can be presented as slides using the RISE plugin. To get this to work, I have needed to:
- Install as normal (above)
- `mamba install jupyter_contrib_nbextensions`
- `mamba install rise`
- `mamba install git-lfs` for large files
- `python -m ipykernel install --user --name=drugcomp` (or whatever environment is being used above) to make sure this environment is activated in the notebook
- Once installed, if a notebook with RISE slides is active, use option-R to enter the slideshow.

Note that Google Colab and environments without RISE will strip out the RISE formatting from notebooks and make it necessary to re-add it.
