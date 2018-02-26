cmd.set('bg_rgb','1,1,1') #Set background color to white


cmd.load('Octa-Acid.pdb', 'acid')

#Set colors
#cmd.color('gray', 'elem C')
#Default colors OK for rest, I think.

#Show valences
cmd.set('valence', 'on')


cmd.turn('z', '135')
cmd.turn('y', '-7')
cmd.turn('x', '-17')
cmd.turn('z', '-8')
#Note x controls tip towards me

cmd.show('sticks')

#Now do some movie making stuff
#cmd.mset('1 x360') #Create a 360 frame movie with all frames copies of first
cmd.mset('1 x1200') #Create a 272 frame movie with all frames copies of first
#Store our initial view to frame 1
cmd.mview('store', '1')
#Rotate 360 degrees over 144 steps
rotation_per_step = 360./288
for i in range(1, 289):
  cmd.turn('y', '-1')
  cmd.mview('store', i)

#Show spheres
cmd.mdo(288, 'set sphere_transparency = 1.0')
cmd.mdo(289, 'show spheres')
for i in range(288, 388):
    if (i-288)%5==0:
        transparency = 1. - (i-288.)/100.
        cmd.mdo(i, 'set sphere_transparency = %.2f' % transparency )
cmd.mdo( 393, 'set sphere_transparency = 0.0')


#Do another lap
for i in range(288, 578):
    cmd.turn('y', '-1')
    cmd.mview('store', i)

#Turn in x direction to look at bottom
cmd.turn('x', '-90')
cmd.zoom('acid', 2)
cmd.mview('store', '720')
#Now pause
cmd.mview('store', '800')
#Now flip back
cmd.turn('x', '90')
cmd.mview('store', '942')

#Turn in x direction to look at top
cmd.turn('x', '90')
cmd.zoom('acid', 2)
cmd.mview('store', '1088')

cmd.move('z', 30)
cmd.mview('store', '1200')
