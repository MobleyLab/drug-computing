#!/bin/env python
import os
from openeye.oechem import *
from openeye.oeiupac import *
from openeye.oeomega import *
from openeye.oequacpac import *
import pickle

OEThrow.SetLevel(OEErrorLevel_Info);

#First, load known compounds
compounds = {}
file = open('../llinas_knowns.txt', 'r')
text = file.readlines()
file.close()
molnames = []
#Loop over lines and parse
for line in text:
    #Skip comments
    if not line[0]=='#':
        #Split into columns
        tmp = line.split(';')
        name = tmp[0].strip() #Compound name
        mw = float( tmp[1].strip() )#Molecular weight
        pKa = float( tmp[2].strip() )#pKa as deposited
        sol = tmp[3].strip()
        if len(tmp) > 4 and len(tmp[4].strip())>2:
            print("Storing smiles for %s..." % line)
            smiles = tmp[4].strip()
        else:
            smiles = None

        #Store if the solubility is actually a number (skipping n/a values)
        try:
            sol = float(sol)
            compounds[name] = { 'name':name, 'mw':mw, 'pKa': pKa, 'solubility': sol }
            molnames.append(name)
            if not smiles==None:
                compounds[name]['smiles'] = smiles
        except:
            print("Error storing line: %s" % line)

trainingnames = [ name for name in molnames ]



#Add in the molecules we're going to 'predict'
file = open('../hopfinger_unknowns.txt', 'r')
text = file.readlines()
predictnames = []
file.close()
for line in text:
    tmp = line.split(';')
    if not 'ts' in tmp[1].strip(): #Store if not too soluble
        name = tmp[0].strip()
        compounds[name]={'solubility': float( tmp[1].strip() ), 'predict':True }
        predictnames.append(name)
        if len(tmp)>2:
            compounds[name]['smiles'] = tmp[2].strip()

#Make list of all molecules
molnames = molnames + predictnames

#Now loop over names and attempt to generate molecules
for molname in molnames:
    print("\nGenerating %s..." % molname)
    if not 'smiles' in compounds[molname]:
        mol = OEMol()
        status = OEParseIUPACName( mol, molname)
        #createMoleculeFromIUPAC( molname, strictTyping = False )
        #print OECreateCanSmiString(mol)
    else:
        mol = OEMol()
        print("Generating from smiles")
        OEParseSmiles( mol, compounds[molname]['smiles'] )
        #print type(mol)
        #mol = normalizeMolecule( mol )
        #mol = expandConformations( mol, maxconfs = 1)

    name = OECreateIUPACName( mol)
    mol.SetTitle(name)
    OEThrow.Info("Title: %s" % mol.GetTitle() )
    omega = OEOmega()
    omega.SetStrictStereo(False)
    omega.SetStrictAtomTypes( False )
    omega.SetIncludeInput(False)
    omega.SetMaxConfs(1)
    omega(mol)

    #Assign partial charges
    chargeEngine = OEAM1BCCCharges()
    OEAssignCharges( mol, chargeEngine)

    compounds[molname]['oemol'] = mol

    #Compute molecular weight
    mw = OECalculateMolecularWeight( mol )
    #Check against tabulated molecular weight if available
    if 'mw' in compounds[molname]:
        if not (compounds[molname]['mw']-mw) < 0.5:
            print("WARNING: Molecular weight discrepancy: %.2f tabulated vs %.2f computed, for %s..." % (compounds[molname]['mw'], mw, molname ))
    else:
        #Store mw
        compounds[molname]['mw'] = mw

    #Write out molecule
    filename = molname.replace(',','').replace(' ','')+'.sdf'

    if molname not in predictnames:
        fullfilename = os.path.join('../llinas_set', filename )
    else:
        fullfilename = os.path.join('../llinas_predict', filename )
    #print "Filename: %s..." % fullfilename
    ostr = oemolostream(fullfilename)
    OEWriteMolecule(ostr, mol)
    ostr.close()

solubilities = {}
for mol in molnames:
    solubilities[mol] = compounds[mol]['solubility']
file = open('solubilities.pickle', 'wb')
pickle.dump(solubilities, file)
file.close()

