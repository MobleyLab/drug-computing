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

## TO DO: ADD OPTION PARSING

input_molecule = 'mobley_9979854.mol2' #temporary example from FreeSolv

# Key settings to fill in in the template
timestep = 2 #femtoseconds
nsteps_per_iteration = 500 #Number of timesteps per iteration
# Will use 5000, but use 100 now for testing purposes...
#number_of_iterations = 5000 #How many iterations
number_of_iterations = 100 #How many iterations
temperature = 298.15 # kelvin
pressure = 1 #atmosphere
output_dir = 'data'
verbose = 'yes' # yes or no
solvent = 'gbsa' # gbsa or tip3p

# Copy input molecule to output directory
if not os.path.isdir(output_dir): os.mkdir(output_dir)
shutil.copy(input_molecule, os.path.join(output_dir, 'input.mol2'))
# TO DO: DECIDE IF WE SHOULD BE CHARGING THIS molecule
#(Check for charges first and charge if uncharged? Prompt user to provide charges?)


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
    filepath: %(output_dir)s/input.mol2
    antechamber:
      charge_method: null

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
  hydration-tip3p:
    solute: input_molecule
    solvent1: tip3p
    solvent2: vacuum
    leap:
      parameters: [leaprc.gaff, leaprc.protein.ff14SB, leaprc.water.tip3p]
  hydration-gbsa:
    solute: input_molecule
    solvent1: gbsa
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
  system: hydration-%(solvent)s
  protocol: protocol-%(solvent)s
""" % options


# Run YANK on the specified molecule.
yaml_builder = ExperimentBuilder(hydration_yaml)
yaml_builder.run_experiments()
