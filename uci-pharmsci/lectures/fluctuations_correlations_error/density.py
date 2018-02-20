
#--------------------------------------
# OpenMM Minimization, NVT, NPT, PROD
#
# Author: Dr Gaetano Calabro'
# University of California, Irvine
# ver 0.0 06/23/2016
# Adapted Nov. 2017 by David Mobley
#--------------------------------------


import numpy as np
import os, sys
import math
import simtk.openmm as mm
from simtk.openmm import app
from simtk.openmm.app import *
from simtk.openmm import Platform
from simtk.unit import *
from simtk.openmm import XmlSerializer

from pymbar import timeseries as ts
import pandas as pd



#----------------USER INFO-----------------
#------------------------------------------

#Skip equilibration? Use if we previously equilibrated, to load stored
#trajectory file and jump straight into production
skip_equilibration = False

identifier = "phenol_toluene_cyclohexane_1_10_100"

DATA_PATH = "mixtures/amber/"
RESULT_PATH = "density_simulation/"


#md_platform = 'Reference' # e.g. Reference or CUDA or OpenCL
md_platform = 'OpenCL'

# Some file names
prmtop_filename = DATA_PATH + identifier + '.prmtop'
inpcrd_filename = DATA_PATH + identifier + '.inpcrd'
xml_filename = RESULT_PATH + identifier + '.xml' # For serialized system

#--------------MINIMIZATION----------------
MIN_TIME_STEP = 0.5 * femtoseconds
MIN_STEPS =  0 # 0=Until convergence is reached
MIN_TOLERANCE  = 10.0 * kilojoule_per_mole
MIN_PLATFORM = Platform.getPlatformByName('Reference')
MIN_FRICTION = 1.0 / picoseconds

#-------------------NVT--------------------
NVT_TIME_STEP = 1.0 * femtoseconds
NVT_STEPS = 50000
NVT_FRICTION = 1.0 / picoseconds
NVT_PLATFORM = Platform.getPlatformByName(md_platform)
NVT_PROPERTIES = {'DeviceIndex':1} # TEST
if md_platform == 'CUDA':
    NVT_PROPERTIES = {'CudaPrecision': 'mixed'}
else: NVT_PROPERTIES={}
NVT_OUTPUT_FREQ = 10000
NVT_DATA_FREQ = 10000

#------------------NPT--------------------
NPT_TIME_STEP = 2.0 * femtoseconds
NPT_STEPS = 5000000
NPT_FRICTION = 1.0 / picoseconds
BAROSTAT_FREQUENCY = 25
NPT_PLATFORM = Platform.getPlatformByName(md_platform)
if md_platform == 'CUDA':
    NPT_PROPERTIES = {'CudaPrecision': 'mixed'}
else: NPT_PROPERTIES={}
NPT_OUTPUT_FREQ = 500000
NPT_DATA_FREQ = 500000

#--------------PRODUCTION------------------
PROD_TIME_STEP = 2.0 * femtoseconds
PROD_STEPS = 50000
PROD_FRICTION = 1.0 / picoseconds
PROD_PLATFORM = Platform.getPlatformByName(md_platform)
if md_platform == 'CUDA':
    PROD_PROPERTIES = {'CudaPrecision': 'mixed'}
else: PROD_PROPERTIES={}
PROD_OUTPUT_FREQ = 500
PROD_DATA_FREQ = 500

#------------GEN PARAMETERS--------------
CUTOFF = 0.95 * nanometers
TEMPERATURE = 300 * kelvin
PRESSURE = 1.0 * atmospheres
#Density STD tolerance
STD_ERROR_TOLERANCE = 0.0005 # g/mL


#---------------END USER INFO---------------
#-------------------------------------------




nvt_dcd_filename = RESULT_PATH + "nvt/" + identifier + "_nvt.dcd"
nvt_data_filename = RESULT_PATH + "nvt/" + identifier + "_nvt.csv"

npt_dcd_filename = RESULT_PATH + "npt/" + identifier + "_npt.dcd"
npt_data_filename = RESULT_PATH + "npt/" + identifier + "_npt.csv"

prod_data_filename = RESULT_PATH + "prod/" + identifier + "_prod.csv"
prod_dcd_filename = RESULT_PATH + "prod/" + identifier + "_prod.dcd"

# Load prmtop, crd
prmtop = AmberPrmtopFile( prmtop_filename )
inpcrd = AmberInpcrdFile( inpcrd_filename )

def make_path(filename):
    try:
        path = os.path.split(filename)[0]
        os.makedirs(path)
    except OSError:
        pass

# Create System and store to OpenMM XML for easier reuse later
system = prmtop.createSystem(nonbondedMethod = PME, nonbondedCutoff = 1*nanometer, constraints = HBonds)
make_path(xml_filename)
serialized_system = XmlSerializer.serialize(system)
file = open(xml_filename, 'w')
file.write(serialized_system)
file.close()




def minimization():
    # Load OpenMM System
    file = open(xml_filename, 'r')
    serialized_system = file.read()
    system = XmlSerializer.deserialize(serialized_system)

    # Select Integrator
    integrator = mm.LangevinIntegrator(TEMPERATURE, MIN_FRICTION, MIN_TIME_STEP)

    # Set Simulation
    simulation = app.Simulation(prmtop.topology, system, integrator, MIN_PLATFORM)

    # Set Position
    simulation.context.setPositions(inpcrd.positions)

    state = simulation.context.getState(getEnergy=True)

    if np.isnan(state.getPotentialEnergy() / kilojoule_per_mole):
        raise ValueError("The Potential Energy before minimization is NaN")

    # Minimization
    print('Minimizing...\n')
    simulation.minimizeEnergy(tolerance=MIN_TOLERANCE, maxIterations=MIN_STEPS)

    state = simulation.context.getState(getPositions=True, getEnergy=True)

    if np.isnan(state.getPotentialEnergy() / kilojoule_per_mole):
        raise ValueError("The Potential Energy after minimization is NaN")

    coords = state.getPositions()

    return coords


def nvt(coords):
    # Load OpenMM System
    file = open(xml_filename, 'r')
    serialized_system = file.read()
    system = XmlSerializer.deserialize(serialized_system)

    # Select Integrator
    integrator = mm.LangevinIntegrator(TEMPERATURE, NVT_FRICTION, NVT_TIME_STEP)

    # Set Simulation
    simulation = app.Simulation(prmtop.topology, system, integrator, NVT_PLATFORM, NVT_PROPERTIES)


    # Set Position and velocities
    simulation.context.setPositions(coords)
    simulation.context.setVelocitiesToTemperature(TEMPERATURE)

    # Set Reporter
    simulation.reporters.append(app.DCDReporter(nvt_dcd_filename, NVT_OUTPUT_FREQ))
    simulation.reporters.append(app.StateDataReporter(nvt_data_filename, NVT_DATA_FREQ, step=True, potentialEnergy=True, temperature=True, density=True))

    state = simulation.context.getState(getEnergy=True)

    if np.isnan(state.getPotentialEnergy() / kilojoule_per_mole):
        raise ValueError("The Potential Energy before NVT is NaN")

    print('NVT...\n')
    simulation.step(NVT_STEPS)

    state = simulation.context.getState(getPositions=True, getVelocities=True, getEnergy=True)

    if np.isnan(state.getPotentialEnergy() / kilojoule_per_mole):
        raise ValueError("The Potential Energy after NVT is NaN")


    coords = state.getPositions()
    velocities = state.getVelocities()

    return coords, velocities



def npt(coords, velocities):
    # Create OpenMM System
    file = open(xml_filename, 'r')
    serialized_system = file.read()
    system = XmlSerializer.deserialize(serialized_system)

    # Select Integrator
    integrator = mm.LangevinIntegrator(TEMPERATURE, NPT_FRICTION, NPT_TIME_STEP)

    # Set Barostat
    system.addForce(mm.MonteCarloBarostat(PRESSURE, TEMPERATURE, BAROSTAT_FREQUENCY))

    # Set Simulation
    simulation = app.Simulation(prmtop.topology, system, integrator, NPT_PLATFORM, NPT_PROPERTIES)

    # Set Position and velocities
    simulation.context.setPositions(coords)
    simulation.context.setVelocities(velocities)

    # Set Reporter
    simulation.reporters.append(app.DCDReporter(npt_dcd_filename, NPT_OUTPUT_FREQ))
    simulation.reporters.append(app.StateDataReporter(npt_data_filename, NPT_DATA_FREQ, step=True, potentialEnergy=True, temperature=True, density=True))

    state = simulation.context.getState(getEnergy=True)

    if np.isnan(state.getPotentialEnergy() / kilojoule_per_mole):
        raise ValueError("The Potential Energy before NPT is NaN")

    print('NPT...\n')
    simulation.step(NPT_STEPS)

    state = simulation.context.getState(getPositions=True, getVelocities=True, getEnergy=True)

    if np.isnan(state.getPotentialEnergy() / kilojoule_per_mole):
        raise ValueError("The Potential Energy after NPT is NaN")


    coords = state.getPositions()
    velocities = state.getVelocities()
    box = state.getPeriodicBoxVectors()

    return coords, velocities, box



def production(coords, velocities, box):

    # Create OpenMM System
    file = open(xml_filename, 'r')
    serialized_system = file.read()
    system = XmlSerializer.deserialize(serialized_system)

    # Select Integrator
    integrator = mm.LangevinIntegrator(TEMPERATURE, PROD_FRICTION, PROD_TIME_STEP)

    # Set Barostat
    system.addForce(mm.MonteCarloBarostat(PRESSURE, TEMPERATURE, BAROSTAT_FREQUENCY))

    # Set Simulation
    simulation = app.Simulation(prmtop.topology, system, integrator, PROD_PLATFORM, PROD_PROPERTIES)

    # Set Position and velocities
    simulation.context.setPositions(coords)
    if velocities is not None:
        simulation.context.setVelocities(velocities)
    else: #reset
        simulation.context.setVelocitiesToTemperature(TEMPERATURE)

    # Set Box
    #box = box.in_units_of(nanometer)
    simulation.context.setPeriodicBoxVectors(box[0], box[1], box[2])


    # Set Reporter
    simulation.reporters.append(app.DCDReporter(prod_dcd_filename, PROD_OUTPUT_FREQ))
    simulation.reporters.append(app.StateDataReporter(prod_data_filename, PROD_DATA_FREQ, step=True, potentialEnergy=True, temperature=True, density=True))


    state = simulation.context.getState(getEnergy=True)

    if np.isnan(state.getPotentialEnergy() / kilojoule_per_mole):
        raise ValueError("The Potential Energy before Production is NaN")

    print('PRODUCTION...\n')

    converged = False

    while not converged:

        simulation.step(PROD_STEPS)

        d = pd.read_csv(prod_data_filename, names=["step", "U", "Temperature", "Density"], skiprows=1)
        density_ts = np.array(d.Density)
        [t0, g, Neff] = ts.detectEquilibration(density_ts, nskip=1000)
        density_ts = density_ts[t0:]
        density_mean_stderr = density_ts.std() / np.sqrt(Neff)

        print("Current density mean std error = %f g/mL" % density_mean_stderr)

        if density_mean_stderr < STD_ERROR_TOLERANCE:
            converged = True
            print("...Convergence is OK\n")

    state = simulation.context.getState(getPositions=True, getVelocities=True, getEnergy=True)


    if np.isnan(state.getPotentialEnergy() / kilojoule_per_mole):
        raise ValueError("The Potential Energy after Production is NaN")


    coords = state.getPositions()
    velocities = state.getVelocities()
    box = state.getPeriodicBoxVectors()

    return coords, velocities, box


if __name__=='__main__':

    make_path(RESULT_PATH + 'nvt/')
    make_path(RESULT_PATH + 'npt/')
    make_path(RESULT_PATH + 'prod/')


    if not skip_equilibration:
        coords = minimization()
        coords, velocities = nvt(coords)
        coords, velocities, box = npt(coords, velocities)
    else:
        import mdtraj as md
        # Load dcd file with relevant INFO
        traj = md.load_dcd( npt_dcd_filename, prmtop_filename )
        coords = traj.xyz[-1]
        #velocities = traj.velocities[-1]
        box = traj.unitcell_vectors[-1]
        #DCD file seems not to have velocities; set to None to trigger a reset to temperature
        velocities = None

    production(coords, velocities, box)
