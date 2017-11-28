#!/bin/env python

import io, os, time, traceback, base64, shutil
from openeye import oechem
import numpy as np
from simtk import unit, openmm
from simtk.openmm import app
import netCDF4 as netcdf
from tempfile import TemporaryDirectory
import yank
import mdtraj
from yank.experiment import *
import textwrap
import subprocess
import openforcefield.utils #Not really needed that much, but has nice utility function for checking charges and reading molecules

# Set up option parsing
from optparse import OptionParser
parser = OptionParser()
parser.add_option('-f', '--file', dest='input_molecule',
                    help = "Input mol2 file containing molecule", metavar="File", default = None)
parser.add_option('--smiles', dest = 'smiles',
                    help="SMILES string for desired molecule", metavar = "String", type="string", default = None)
parser.add_option('--name', dest = 'name', help='IUPAC name of desired molecule',
                    metavar = "String", type ="string", default = None)
parser.add_option('-s', '--solvent', dest="solvent", metavar='String', type="string",
                    help = "Solvent model: tip3p or gbsa; default=gbsa", default ='gbsa' )
parser.add_option('-i', '--iterations', dest="iterations", metavar = "integer", type="int",
                    help = "Number of iterations (each is 500 steps); default = 5000.", default=5000)
parser.add_option('-t', '--dt', dest="timestep", metavar = "integer", type="int",
                    help = "Timestep in femtoseconds; default = 2.", default = 2)
parser.add_option('-o', '--out', dest="output_dir", metavar = "String", type="string",
                    help = "Output directory; default 'data'.", default ='data')
parser.add_option('-T', '--temperature', dest='temperature', metavar = "float", type="float",
                    help = "Temperature in Kelvin; default = 298.15", default = 298.15)

(options, args) = parser.parse_args()


# Do some error checking on input options
input_molecule = options.input_molecule
if input_molecule is not None:
    if not os.path.isfile(input_molecule) or not input_molecule[-5:]=='.mol2' or not input_molecule[-5:]=='.pdb' or not input_molecule[-5:]=='.sdf':
        parser.error("Error: `input_molecule` must be an accessible mol2, sdf, or pdb file.")
    input_source = 'File'
else:
    input_source = 'Identifier'
if input_molecule is None and options.smiles is None and options.name is None:
        parser.error("Error: Must provide a solute molcule via the --file, --smiles, or --name options.")
if not options.solvent.lower()=='tip3p' and not options.solvent.lower()=='gbsa':
    parser.error("Error: Solvent must be tip3p or gbsa.")


# Key settings to fill in in the template
timestep = options.timestep #femtoseconds
nsteps_per_iteration = 500 #Number of timesteps per iteration
#How many iterations
number_of_iterations = options.iterations #How many iterations
temperature = options.temperature # kelvin
pressure = 1 #atmosphere
output_dir = options.output_dir
verbose = 'yes' # yes or no
solvent = options.solvent.lower() # gbsa or tip3p; needs to be lowercase

# If our input source is a file, do some bookkeeping -- copy file, charging if needed
if input_source =='File':
    # Read molecule
    mol = openforcefield.utils.read_molecules(input_molecule)[0]
    # Check if charged
    isCharged = openforcefield.utils.checkCharges(mol)

    if not isCharged:
        print("Warning: Your input molecule has no partial charges. Partial charges will be assigned via AM1-BCC unless you provide an input molecule with charges.")
        charge_method = 'bcc'
    else:
        charge_method = 'null'

    # Copy input molecule to output directory
    input_filename = 'input'+input_molecule[-5:]
    if not os.path.isdir(output_dir): os.mkdir(output_dir)
    shutil.copy(input_molecule, os.path.join(output_dir, input_filename))
else:
    charge_method = 'bcc'

#Compose string describing input for YAML -- if it's an input file, use it
# otherwise use SMILES or name and use BCC charges
if input_source =='File':
    molecule_string = 'filepath: %s/%s' % (output_dir, input_filename)
elif options.smiles is not None:
    molecule_string = 'smiles: %s' % options.smiles
    charge_method = 'bcc'
elif options.name is not None:
    molecule_string = 'name: %s' % options.name
    charge_method = 'bcc'


# Compose options
options = {
    'timestep' : timestep,
    'nsteps_per_iteration' : nsteps_per_iteration,
    'number_of_iterations' : number_of_iterations,
    'temperature' : temperature,
    'pressure' : pressure,
    'solvent' : solvent,
    'verbose' : 'yes' if verbose else 'no',
    'output_dir': output_dir,
    'charge_method': charge_method,
    'input_source': molecule_string,
}


## Define YAML template for use with implicit OR explicit solvent hydration
# free energy calculations, adapted from https://github.com/oess/openmm_orion/commit/9bb2f55d416acae8b6f31647e918a520c624bc6e
# with additions from https://github.com/choderalab/yank-examples/blob/master/examples/hydration/freesolv/yank.yaml
# and https://github.com/MobleyLab/SMIRNOFF_paper_code/blob/master/FreeSolv/scripts/yank_template.yaml

hydration_yaml = """\
---
options:
  minimize: yes
  resume_simulation: yes
  checkpoint_interval: 50
  timestep: %(timestep)f*femtoseconds
  nsteps_per_iteration: %(nsteps_per_iteration)d
  number_of_iterations: %(number_of_iterations)d
  temperature: %(temperature)f*kelvin
  pressure: %(pressure)f*atmosphere
  anisotropic_dispersion_cutoff: 9*angstroms
  output_dir: %(output_dir)s
  verbose: %(verbose)s

molecules:
  input_molecule:
    %(input_source)s
    antechamber:
      charge_method: %(charge_method)s

solvents:
  tip3p:
    solvent_model: tip3p
    nonbonded_method: PME
    nonbonded_cutoff: 9*angstroms
    clearance: 8*angstroms
    ewald_error_tolerance: 1.0e-4
  gbsa:
    nonbonded_method: NoCutoff
    implicit_solvent: OBC2
  vacuum:
    nonbonded_method: NoCutoff

systems:
  hydration:
    solute: input_molecule
    solvent1: %(solvent)s
    solvent2: vacuum
    leap:
      parameters: [leaprc.gaff, leaprc.protein.ff14SB, leaprc.water.tip3p]

protocols:
  protocol-tip3p:
    solvent1:
      alchemical_path:
        lambda_electrostatics: [1.00, 0.75, 0.50, 0.25, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
        lambda_sterics:        [1.00, 1.00, 1.00, 1.00, 1.00, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70, 0.65, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10, 0.00]
    solvent2:
      alchemical_path:
        lambda_electrostatics: [1.00, 0.75, 0.50, 0.25, 0.00]
        lambda_sterics:        [1.00, 1.00, 1.00, 1.00, 1.00]


  protocol-gbsa:
    solvent1:
      alchemical_path:
        lambda_electrostatics: [1.00, 0.00]
        lambda_sterics:        [1.00, 0.00]
    solvent2:
      alchemical_path:
        lambda_electrostatics: [1.00, 0.00]
        lambda_sterics:        [1.00, 0.00]

experiments:
  system: hydration
  protocol: protocol-%(solvent)s
""" % options


# Run YANK on the specified molecule.
yaml_builder = ExperimentBuilder(hydration_yaml)
yaml_builder.run_experiments()
