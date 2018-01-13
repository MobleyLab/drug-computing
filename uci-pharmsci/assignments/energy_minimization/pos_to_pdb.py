import numpy as np

def MinImage(Pos, L):
    """Returns a new Pos array with minimum-imaged positions and CM held fixed."""
    Pos = Pos / L - np.round(Pos / L)
    Pos = Pos - Pos.mean(axis=0)
    return Pos

def PosToPDB( Pos, L, file):
    """ Take a position array, a box length L, and a target PDB file, and write the atomic coordinates to the PDB file, followed by the 'TER' code."""

    #Handle periodicity using minimum image convention
    Pos = MinImage(Pos, L)*L

    ofile = open(file, 'a') #Open target file to append
    for atomnum in range(len(Pos)):
        line = '%-6s%5s%5s %3s A   1    %8.3f%8.3f%8.3f\n' % ( 'ATOM', str(atomnum), 'C', 'MOL', Pos[atomnum][0], Pos[atomnum][1], Pos[atomnum][2] )
        ofile.write(line)
    ofile.write('TER\nENDMDL\n')
    ofile.close() 
    
