# Completed code for MC sandbox LJ particle example; not meant for independent use



#Define a counter to count how many moves are accepted
ct=0

#Run a 'for' loop over steps (starting with step 2, since we did step 1 above, and running up to max_steps)
for i in range(2, max_steps):
    #Generate a random move proposal
    move = max_displacement * (np.random.random( 3)*2.-1.)

    #Pick a random particle to move
    num = np.random.randint(N) #Random integer from 0 up to but not including N

    #Store the old positions before updating
    OldPos = Pos.copy()
    #Update the positions with the proposed move
    Pos[num,:] += move
    #Calculate the new energy
    Unew = mc_sandbox.calcenergy( Pos, L, Cut)
    #Evaluate the change in energy
    DeltaU = Unew - U

    #Calculate the acceptance probability
    Pacc = np.exp(-DeltaU/T)

    #Decide whether to accept or reject the move with if/else statements,
    #reverting the position array if it's rejected
    #Also update your counter to track whether or not the move was accepted
    if np.random.rand() < Pacc:
        U = Unew
        ct+=1
    else:
        Pos = OldPos.copy()
    #Store the positions for the current step (whether or not they changed)
    Pos_t[:,:,i] = Pos

#Print out the fraction of moves which were accepted, and the final energy if you like.

print(float(ct)/float(max_steps))

##GET READY TO PLOT
#Find x axis (MC steps rather than time, as it was in the MD sandbox)
t = np.arange(0,max_steps)
#Find y axis (r values)
r_vs_t = []
for i in range(max_steps):
    r=get_r(Pos_t[:,:,i], L)
    r_vs_t.append(r)

r_vs_t = np.array(r_vs_t)

#Plot
figure()
plot(t, r_vs_t)
