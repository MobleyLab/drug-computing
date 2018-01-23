# Completed code for MD sandbox 1D oscillator example

    energy, Forces = calcenergyforces( Pos, M, L, Cut, Forces )
    Pos, Vel, Accel, KEnergy, PEnergy = vvintegrate( Pos, Vel, Forces, M, L, Cut, dt )
    Pos_t[:,:,i] = Pos
