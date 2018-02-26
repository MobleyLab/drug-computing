cmd.set('bg_rgb','1,1,1') #Set background color to white


for prot in ['1HVR', '1MUI', '1HXW']:
    cmd.load( prot+'.pdb', prot ) #Load each protein as a new object
    cmd.align( prot, '1HVR') #Align each protein

cmd.show('cartoon') #Show cartoons for protein
cmd.hide('lines') #Hide lines
cmd.center('1HVR') #Center on one protein (really all, since aligned)
cmd.remove('SOLVENT') #Remove solvent
cmd.show('sticks', 'HETATM') #Show sticks for ligands bound
