# Setup and Installation

## **(WINDOWS ONLY)** Install BASH on Windows
Follow the official guide linked [here](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)

If the BASH terminal guide works and you can successfully use BASH commands (i.e `cd`, `ls`). Now, try performing the installation steps to see if we can get Anaconda/OpenEye installed on your local machine too.

This feature is still in BETA and I have not tried it out myself. So I'm really hoping it works out on your machine. This is meant to replace command terminals like PuTTY so that your terminal can more closely mimic the command terminal found on Linux/MacOS machines or when you login to remote clusters.

## Anaconda Python
Download the Anaconda installation file or Download it from the [website](https://www.continuum.io/downloads)
> wget https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh

Install Anaconda (this may take 15-30mins)
> bash Anaconda3-4.4.0-Linux-x86_64.sh -b

Make sure the anaconda3 path is added to your `~/.bash_profile`
>echo export PATH="$HOME/anaconda3/bin:$PATH" >> ~/.bash_profile

When it asks you to add Anaconda to your bash shell PATH, select **YES**.

Check that Anaconda installed properly by running the command `python`. It's output should look something like:
```
Python 3.6.0 |Anaconda 4.3.0 (64-bit)| (default, Dec 23 2016, 12:22:00)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Conda install Requirements

```bash
git clone git@github.com:MobleyLab/drug-computing.git
cd drug-computing

#Create a new local conda environment
conda create -n drugcomp python=3.5
source activate drugcomp
conda install -c omnia openmm==7.1.0rc1 parmed numpy matplotlib
conda install -c conda-forge nb_conda mpld3 scikit-learn seaborn
```

## Install OpenEye toolkits
*While still in your drugcomp virtualenv*

```bash
#Add the OE_LICENSE to your ~/.bash_profile
echo export OE_LICENSE="<PATHTOFILE>/oe_license.txt" >> ~/.bash_profile

#Install the OpenEye-floe package and toolkits
pip install -i https://pypi.anaconda.org/OpenEye/simple OpenEye-toolkits
pip install --pre --extra-index-url https://pypi.anaconda.org/OpenEye/channel/beta/simple OpenEye-oenotebook
```
Verify the installation with:
> python oecheminfo.py

The output should look something like:
```
Installed OEChem version: 2.1.1 platform: linux-g++4.x-x64 built: 20170210

Examples: /home/limn1/anaconda3/envs/dev/lib/python3.5/site-packages/openeye/examples
Doc Examples: /home/limn1/anaconda3/envs/dev/lib/python3.5/site-packages/openeye/docexamples

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
