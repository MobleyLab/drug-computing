
subroutine CalcEnergy(Pos, M, L, rc, PEnergy, Dim, NAtom)
    implicit none
    integer, intent(in) :: M, Dim, NAtom
    real(8), intent(in), dimension(0:NAtom-1, 0:Dim-1) :: Pos
    real(8), intent(in) :: L, rc
    real(8), intent(out) :: PEnergy
    real(8), parameter :: k = 3000., r0 = 1.
    integer:: i, j
    real(8) :: kfac, d2, sep, disp, shiftval, rc2, id6, id2, id12
    real(8), dimension(Dim) :: rij, Posi
    

    !Assign initially zeros to the force array and potential energy
    PEnergy = 0.
    rc2 = rc**2

    !Precompute constants such as LJ shift value up here
    kfac = k/2.
    id6 = 1./rc**6
    shiftval = 4*(id6**2 - id6)


    do i=0, NAtom - 1
        !store Pos(i,:) in a temporary array for faster access in j looop
        Posi = Pos(i,:)
        do j = i+1, NAtom - 1
            !compute initial rij
            rij = Pos(j,:) - Posi
            !Apply minimum image convention
            rij = rij - L*dnint(rij / L)

            !Do bonded calculation
            if ( j == i+1 .and. mod(j, M)> 0) then
                !Compute scalar separation
                sep = sqrt( sum( rij * rij ) )
                !Compute displacement relative to preferred separation
                disp = sep - r0
                !Calculate energy
                PEnergy = PEnergy + kfac * disp*disp
            else   !Do nonbonded calculation
                !compute scalar distance
                d2 = sum(rij*rij)
                !Check against cutoff
                if ( d2 > rc2) then 
                    cycle
                end if
                id2 = 1./d2                 !inverse squared distance
                id6 = id2 * id2 * id2       !inverse sixth distance
                id12 = id6 * id6            !inverse twelfth distance
                PEnergy = Penergy + 4. * (id12 - id6) + shiftval

                !end nonbonded calculation
            endif
        enddo
    enddo
end subroutine



subroutine CalcEnergyForces(Pos, M, L, rc, PEnergy, Forces, Dim, NAtom)
    implicit none
    integer, intent(in) :: M, Dim, NAtom
    real(8), intent(in), dimension(0:NAtom-1, 0:Dim-1) :: Pos
    real(8), intent(in) :: L, rc
    real(8), intent(out) :: PEnergy
    real(8), intent(inout), dimension(0:NAtom-1, 0:Dim-1) :: Forces
!f2py intent(in, out, inplace) :: Forces
    real(8), parameter :: k = 3000., r0 = 1.
    integer :: i, j
    real(8) :: kfac, d2, sep, disp, shiftval, rc2, id6, id2, id12
    real(8), dimension(Dim) :: rij, Fij, Posi
    

    !Assign initially zeros to the force array and potential energy
    Forces = 0.
    PEnergy = 0.
    rc2 = rc**2

    !Precompute constants such as LJ shift value up here
    kfac = k/2.
    id6 = 1./rc**6
    shiftval = 4.*(id6**2 - id6)


    do i=0, NAtom - 1
        !store Pos(i,:) in a temporary array for faster access in j looop
        Posi = Pos(i,:)
        do j = i+1, NAtom - 1
            !compute initial rij
            rij = Pos(j,:) - Posi
            !Apply minimum image convention
            rij = rij - L*dnint(rij / L)

            !Do bonded calculation
            if ( j == i+1 .and. mod(j, M)> 0) then
                !Compute scalar separation
                sep = sqrt( sum( rij * rij ) )
                !Compute displacement relative to preferred separation
                disp = sep - r0
                !Calculate energy
                PEnergy = PEnergy + kfac * disp*disp
                !Calculate force: - k*displacement in direction of rij
                Fij = k * ( disp ) * rij/sep
                Forces(i,:) = Forces(i,:) + Fij
                Forces(j,:) = Forces(j,:) - Fij
            else   !Do nonbonded calculation
                !compute scalar distance
                d2 = sum(rij*rij)
                !Check against cutoff
                if ( d2 > rc2) then 
                    cycle
                end if
                id2 = 1./d2                 !inverse squared distance
                id6 = id2 * id2 * id2       !inverse sixth distance
                id12 = id6 * id6            !inverse twelfth distance
                PEnergy = Penergy + 4. * (id12 - id6) + shiftval
                Fij = rij * (-48. * id12 + 24. * id6) * id2
                Forces(i,:) = Forces(i,:) + Fij
                Forces(j,:) = Forces(j,:) - Fij

                !end nonbonded calculation
            endif
        enddo
    enddo
end subroutine


subroutine VVIntegrate(Pos, Vel, Accel, M, L, rc, dt, KEnergy, PEnergy, Dim, NAtom)
    implicit none
    integer, intent(in) :: M, Dim, NAtom
    real(8), intent(in) :: L, rc, dt
    real(8), intent(inout), dimension(0:NAtom-1, 0:Dim-1) :: Pos, Vel, Accel
!f2py intent(in,out,inplace) :: Pos, Vel, Accel
    real(8), intent(out) :: KEnergy, PEnergy
    external :: CalcEnergyForces
    Pos = Pos + dt * Vel + 0.5 * dt*dt * Accel
    Vel = Vel + 0.5 * dt * Accel
    call CalcEnergyForces(Pos, M, L, rc, PEnergy, Accel, Dim, NAtom)
    Vel = Vel + 0.5 * dt * Accel
    KEnergy = 0.5 * sum(Vel*Vel)
end subroutine
