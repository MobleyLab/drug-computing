cmd.set('bg_rgb','1,1,1') #Set background color to white


for prot in ['1HVR', '1MUI', '1HXW']:
    cmd.load( prot+'.pdb', prot ) #Load each protein as a new object
    cmd.align( prot, '1HVR') #Align each protein

cmd.show('cartoon') #Show cartoons for protein
cmd.hide('lines') #Hide lines
cmd.center('1HVR') #Center on one protein (really all, since aligned)
cmd.remove('SOLVENT') #Remove solvent
cmd.show('sticks', 'HETATM') #Show sticks for ligands bound
preset.publication()

cmd.create('lig', 'resn RIT') #Create selection of a particular ligand
cmd.remove('1HXW and resn RIT')
cmd.show('sticks', 'lig')
cmd.zoom()

#Do some initial orientation stuff
cmd.turn('y', '45')
cmd.turn('z', '-17')
cmd.turn('x', '-20')

#Now do some movie making stuff
cmd.mset('1 x360') #Create a 360 frame movie with all frames copies of first
#Store our initial view to frame 1
cmd.mview('store', '1')
#Turn 180 degrees around y axis
cmd.turn('y', '180')
#Store this view in frame 36; intermediate frames will be interpolated
cmd.mview('store', '36')
#Turn another 180 degrees
cmd.turn('y', '180')
#Store this view to frame 72
cmd.mview('store', '72')

#We still have nothing after frame 72 and we created a 360 frame movie. 

#Hide everything from the other ligands and proteins
cmd.mdo('72', 'hide everything, 1HVR; hide everything, 1MUI')

#Zoom in on, and rotate around a bit, the ligand
cmd.zoom('lig') #Zoom in on the ligand
cmd.turn('y', '45') #Rotate a bit in y direction
cmd.mview('store', '150') #Now up to frame 150

#Turn on space filling representation for the ligand and lines for the protein
cmd.mdo('150', 'show spheres, lig; show lines, 1HXW')
#Do another 180 degree rotation
cmd.turn('y', '180')
cmd.mview('store', '260') #Store to frame 260


#Now go to a semi-transparent surface representation of the protein
cmd.mdo('260', 'show surf, 1HXW')
cmd.set('transparency', '0.4')

#Zoom back out and do another rotation
cmd.zoom()
cmd.turn('y', '180')
cmd.mview('store', '360')
