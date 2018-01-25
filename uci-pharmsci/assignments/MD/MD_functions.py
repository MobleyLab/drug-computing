#MD Exercise Template for PharmSci 275
#This is just MD.py with the prototypes for InitVelocities and RescaleVelocities removed so that these can be defined within the iPython notebook.

#import python modules
import numpy as np
import time

#import compiled fortran library
import mdlib
import sys
import os

#whether or not to use the 3d visualization
UseVisual = False
if UseVisual:
    #import custom visualization library
    import atomvis


#========== GLOBAL VARIABLES ==========
#set the random number seed; useful for debugging
np.random.seed(342324)

#NOTE:
#everything below assumes unit atomic masses,
#such that forces = accelerations.



def LineSearch(Pos, Dir, dx, EFracTol, M, L, Cut,
               Accel = 1.5, MaxInc = 10., MaxIter = 10000):
    """Performs a line search along direction Dir.
Input:
    Pos: starting positions, (N,3) array
    Dir: (N,3) array of gradient direction
    dx: initial step amount
    EFracTol: fractional energy tolerance
    M: Monomer number per polymer
    L: Box size
    Cut: Cutoff
    Accel: acceleration factor
    MaxInc: the maximum increase in energy for bracketing
    MaxIter: maximum number of iteration steps
Output:
    PEnergy: value of potential energy at minimum along Dir
    Pos: minimum energy (N,3) position array along Dir
"""
    #start the iteration counter
    Iter = 0

    #find the normalized direction
    NormDir = Dir / np.sqrt(np.sum(Dir * Dir))

    #take the first two steps and compute energies
    Dists = [0., dx]
    PEs = [mdlib.calcenergy(Pos + NormDir * x, M, L, Cut) for x in Dists]

    #if the second point is not downhill in energy, back
    #off and take a shorter step until we find one
    while PEs[1] > PEs[0]:
        Iter += 1
        dx = dx * 0.5
        Dists[1] = dx
        PEs[1] = mdlib.calcenergy(Pos + NormDir * dx, M, L, Cut)

    #find a third point
    Dists = Dists + [2. * dx]
    PEs = PEs + [mdlib.calcenergy(Pos + NormDir * 2. * dx, M, L, Cut)]

    #keep stepping forward until the third point is higher
    #in energy; then we have bracketed a minimum
    while PEs[2] < PEs[1]:
        Iter += 1

        #find a fourth point and evaluate energy
        Dists = Dists + [Dists[-1] + dx]
        PEs = PEs + [mdlib.calcenergy(Pos + NormDir * Dists[-1], M, L, Cut)]

        #check if we increased too much in energy; if so, back off
        if (PEs[3] - PEs[0]) > MaxInc * (PEs[0] - PEs[2]):
            PEs = PEs[:3]
            Dists = Dists[:3]
            dx = dx * 0.5
        else:
            #shift all of the points over
            PEs = PEs[-3:]
            Dists = Dists[-3:]
            dx = dx * Accel

    #we've bracketed a minimum; now we want to find it to high
    #accuracy
    OldPE3 = 1.e300
    while True:
        Iter += 1
        if Iter > MaxIter:
            print("Warning: maximum number of iterations reached in line search.")
            break

        #store distances for ease of code-reading
        d0, d1, d2 = Dists
        PE0, PE1, PE2 = PEs

        #use a parobolic approximation to estimate the location
        #of the minimum
        d10 = d0 - d1
        d12 = d2 - d1
        Num = d12*d12*(PE0-PE1) - d10*d10*(PE2-PE1)
        Dem = d12*(PE0-PE1) - d10*(PE2-PE1)
        if Dem == 0:
            #parabolic extrapolation won't work; set new dist = 0
            d3 = 0
        else:
            #location of parabolic minimum
            d3 = d1 + 0.5 * Num / Dem

        #compute the new potential energy
        PE3 = mdlib.calcenergy(Pos + NormDir * d3, M, L, Cut)

        #sometimes the parabolic approximation can fail;
        #check if d3 is out of range < d0 or > d2 or the new energy is higher
        if d3 < d0 or d3 > d2 or PE3 > PE0 or PE3 > PE1 or PE3 > PE2:
            #instead, just compute the new distance by bisecting two
            #of the existing points along the line search
            if abs(d2 - d1) > abs(d0 - d1):
                d3 = 0.5 * (d2 + d1)
            else:
                d3 = 0.5 * (d0 + d1)
            PE3 = mdlib.calcenergy(Pos + NormDir * d3, M, L, Cut)

        #decide which three points to keep; we want to keep
        #the three that are closest to the minimum
        if d3 < d1:
            if PE3 < PE1:
                #get rid of point 2
                Dists, PEs = [d0, d3, d1], [PE0, PE3, PE1]
            else:
                #get rid of point 0
                Dists, PEs = [d3, d1, d2], [PE3, PE1, PE2]
        else:
            if PE3 < PE1:
                #get rid of point 0
                Dists, PEs = [d1, d3, d2], [PE1, PE3, PE2]
            else:
                #get rid of point 2
                Dists, PEs = [d0, d1, d3], [PE0, PE1, PE3]

        #check how much we've changed
        if abs(OldPE3 - PE3) < EFracTol * abs(PE3):
            #the fractional change is less than the tolerance,
            #so we are done and can exit the loop
            break
        OldPE3 = PE3

    #return the position array at the minimum (point 1)
    PosMin = Pos + NormDir * Dists[1]
    PEMin = PEs[1]

    #if using visualization, update the display
    if UseVisual:
        if atomvis.Initialized:
            #update the positions
            atomvis.Update(PosMin)
        else:
            #initialize the visualization window
            atomvis.Init(PosMin)

    return PEMin, PosMin


def ConjugateGradient(Pos, dx, EFracTolLS, EFracTolCG, M, L, Cut):
    """Performs a conjugate gradient search.
Input:
    Pos: starting positions, (N,3) array
    dx: initial step amount
    EFracTolLS: fractional energy tolerance for line search
    EFracTolCG: fractional energy tolerance for conjugate gradient
    M: Monomers per polymer
    L: Box size
    Cut: Cutoff
Output:
    PEnergy: value of potential energy at minimum
    Pos: minimum energy (N,3) position array
"""
    PE, Forces = mdlib.calcenergyforces(Pos, M, L, Cut, np.zeros_like(Pos))
    Dir = Forces
    OldPE = 1.e300
    while abs(PE - OldPE) > EFracTolCG * abs(PE):
        OldPE = PE
        PE, Pos = LineSearch(Pos, Dir, dx, EFracTolLS, M, L, Cut)
        OldForces = Forces.copy()
        PE, Forces = mdlib.calcenergyforces(Pos, M, L, Cut, Forces)
        Gamma = np.sum((Forces - OldForces) * Forces) / np.sum(OldForces * OldForces)
        Dir = Forces + Gamma *  Dir
    return PE, Pos


def InitPositions(N, L):
    """Returns an array of initial positions of each atom,
placed on a cubic lattice for convenience.
Input:
    N: number of atoms
    L: box length
Output:
    Pos: (N,3) array of positions
"""
    #make the position array
    Pos = np.zeros((N,3), float)
    #compute integer grid # of locations for cubic lattice
    NLat = int(N**(1./3.) + 1.)
    LatSpac = float(L) / float(NLat)
    #make an array of lattice sites
    r = LatSpac * np.arange(NLat, dtype=float) - 0.5*L
    #loop through x, y, z positions in lattice until done
    #for every atom in the system
    i = 0
    for x in r:
        for y in r:
            for z in r:
                Pos[i] = np.array([x,y,z], float)
                #add a random offset to help initial minimization
                Offset = 0.1 * LatSpac * (np.random.rand(3) - 0.5)
                Pos[i] = Pos[i] + Offset
                i += 1
                #if done placing atoms, return
                if i >= N:
                    return Pos
    return Pos


def InstTemp(Vel):
    """Returns the instantaneous temperature.
Input:
    Vel: (N,3) array of atomic velocities
Output:
    Tinst: float
"""
    return np.sum(Vel * Vel) / (3. * len(Vel))


