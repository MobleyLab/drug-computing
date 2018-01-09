# Getting your computer ready for PharmSci 175/275

This document, which is a work in progress (contributions welcome), provides information on what you need to install and how in order for your computer to be ready for PharmSci 175/275.

## Prerequisites

Before getting started, note that the below assumes at least some modest familiarity with the BASH shell and the idea of paths, file names, and basic Linux commands.
If you do not have this familiarity, you may need to consult the [BASH cheat sheet](docs/bash_cheatsheet.jpg) and other sources of information (such as the [Linux/bash crash course](docs/linux_crashcourse.md) here) before proceeding.

## Setup and Installation

### **(WINDOWS ONLY -- Skip to the "Anaconda Python" section if you're not on Windows)** Install BASH on Windows
Follow the official guide linked [here](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)

If the BASH terminal guide works and you can successfully use BASH commands (i.e `cd`, `ls`). Now, try performing the installation steps to see if we can get Anaconda/OpenEye installed on your local machine too.

This feature is still in BETA and we have not tested extensively; we hope it will work on your machine.
This is meant to replace command terminals like PuTTY so that your terminal can more closely mimic the command terminal found on Linux/MacOS machines or when you login to remote clusters.

**ALTERNATIVE**:

An alternative approach we are exploring is to distribute USB drives (e.g. thumb drives) with a persistent Linux distribution available pre-installed and you can boot from these/do your work from these for the purposes of this class.
If needed, these should be available from Dr. Mobley for booting your own computer or for use on the computers in our classroom.
Because of hardware differences, it is unlikely that the same installation (below) will work both on a personal laptop and on the computers in the classroom, so you would need to pick one or the other and coordinate with Dr. Mobley.
If using this approach, see [`docs/persistent-usb.md`](docs/persistent-usb.md) for additional information.


### Anaconda Python
Download the Anaconda installation file or Download it from the [website](https://www.continuum.io/downloads) or use (from the command prompt)
> wget https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh

Install Anaconda (this may take 15-30mins)
> bash Anaconda3-4.4.0-Linux-x86_64.sh -b

Make sure the anaconda3 path is added to your `~/.bash_profile` (often this is automatically added by the installer, but make sure it ends up there), e.g. via:
>echo export PATH="$HOME/anaconda3/bin:$PATH" >> ~/.bash_profile

When it asks you to add Anaconda to your bash shell PATH, select **YES**.

Check that Anaconda installed properly by running the command `python`. Its output should look something like:
```
Python 3.6.0 |Anaconda 4.3.0 (64-bit)| (default, Dec 23 2016, 12:22:00)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Conda install requirements

Anaconda includes with it the `conda` environment/package manager, meaning that it can also install other software which you need.
Here we will use the `conda` package manager to install the software you need.

**First, you need to decide whether or not to use a conda environment (`env`) for the course**:
- If you have no idea what this means, only just installed anaconda, and do not have an existing set of conda packages you use extensively, you probably do not want to use an `env`
- If you already have an extensive set of packages managed with `conda` and you want to ensure you do not break or modify your existing installation, you probably DO want to create a custom environment (`env`) for this course.

If you are do not need an `env`, just proceed straight to installation.
If you do need an `env`, [use this info](https://conda.io/docs/user-guide/tasks/manage-environments.html) to create a new Python 3.6 conda environment called `drugcomp` (e.g. `conda create -n drugcomp python=3.6`) and activate this environment (`source activate drugcomp`) before doing the installs discussed below.
Whenever you do work for the class, you will need to activate this environment.

**Then proceed to installation**:

Once Anaconda is installed, run the following on the command-prompt
```bash
git clone git@github.com:MobleyLab/drug-computing.git
cd drug-computing
```
This checks out (obtains) a copy of this repository so you can work with it and the files in it, if you like (you'll be using this to access lecture content and other materials from this class.) (If you have trouble with this, you may want to try the https version of the command, `git clone https://github.com/MobleyLab/drug-computing.git`)

Then do the following additional installs:
```bash
#Install the gcc and gfortran compilers
conda install gcc libgfortran

# Install OpenMM, openforcefield, yank, parmed, and openmoltools
conda install -c omnia openmm openforcefield parmed yank openmoltools pdbfixer solvationtoolkit
# Install oeommtools for interfacing OpenEye and OpenMM
conda install -c OpenEye/label/Orion -c omnia oeommtools
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
pip install --pre --extra-index-url https://pypi.anaconda.org/OpenEye/channel/beta/simple OpenEye-oenotebook
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

After the above, please also use `jupyter-nbextension enable nglview --py --sys-prefix` on the command-line to enable the `nglview` extension for interactive visualization in Jupyter notebooks.
