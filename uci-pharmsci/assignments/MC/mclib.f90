
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


!I AM WRITING THIS PART
!added atomnum argument for atom for which to calculate interaction energy
subroutine CalcInteractionEnergy(Pos, atomnum, M, L, rc, PEnergy, Dim, NAtom)
    implicit none
    integer, intent(in) :: M, Dim, NAtom, atomnum
    real(8), intent(in), dimension(0:NAtom-1, 0:Dim-1) :: Pos
    real(8), intent(in) :: L, rc
    real(8), intent(out) :: PEnergy
    real(8), parameter :: k = 3000., r0 = 1.
    integer:: j
    real(8) :: kfac, d2, sep, disp, shiftval, rc2, id6, id2, id12
    real(8), dimension(Dim) :: rij, Posi
    

    !Assign initially zeros to the force array and potential energy
    PEnergy = 0.
    rc2 = rc**2

    !Precompute constants such as LJ shift value up here
    kfac = k/2.
    id6 = 1./rc**6
    shiftval = 4*(id6**2 - id6)
    
    !store Pos(i,:) in a temporary array for faster access in j looop
    Posi = Pos(atomnum,:)
    do j = 0, NAtom - 1
        if (j==atomnum) cycle 
        !compute initial rij
        rij = Pos(j,:) - Posi
        !Apply minimum image convention
        rij = rij - L*dnint(rij / L)
        !Do bonded calculation
        !Note that each trial movement may involves 2 bond length changes.
        if ( j == atomnum+1 .and. mod(j, M)> 0) then
            !Compute scalar separation
            sep = sqrt( sum( rij * rij ) )
            !Compute displacement relative to preferred separation
            disp = sep - r0
            !Calculate energy
            PEnergy = PEnergy + kfac * disp*disp
        else if (j == atomnum-1 .and. mod(j,M) < M-1) then
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
            if ( d2 > rc2)  cycle
            id2 = 1./d2                 !inverse squared distance
            id6 = id2 * id2 * id2       !inverse sixth distance
            id12 = id6 * id6            !inverse twelfth distance
            PEnergy = Penergy + 4. * (id12 - id6) + shiftval

            !end nonbonded calculation
        endif
    enddo
end subroutine

! a mutant version of CalcInteractionEnergy 
! the atom "atomnum" has an extra virtual displacement parameter.
subroutine CalcVirtualEnergy(Pos, atomnum, virtualDisp, M, L, rc, PEnergy, Dim, NAtom)
    implicit none
    integer, intent(in) :: M, Dim, NAtom, atomnum
    real(8), intent(in), dimension(0:NAtom-1, 0:Dim-1) :: Pos
    real(8), intent(in), dimension(0:Dim-1) :: virtualDisp
    real(8), intent(in) :: L, rc
    real(8), intent(out) :: PEnergy
    real(8), parameter :: k = 3000., r0 = 1.
    integer:: j
    real(8) :: kfac, d2, sep, disp, shiftval, rc2, id6, id2, id12
    real(8), dimension(Dim) :: rij, Posi
    

    !Assign initially zeros to the force array and potential energy
    PEnergy = 0.
    rc2 = rc**2

    !Precompute constants such as LJ shift value up here
    kfac = k/2.
    id6 = 1./rc**6
    shiftval = 4*(id6**2 - id6)
    
    !store Pos(i,:) in a temporary array for faster access in j looop
    Posi = Pos(atomnum,:) + virtualDisp
    do j = 0, NAtom - 1
        if (j==atomnum) cycle 
        !compute initial rij
        rij = Pos(j,:) - Posi
        !Apply minimum image convention
        rij = rij - L*dnint(rij / L)
        !Do bonded calculation
        if ( j == atomnum+1 .and. mod(j, M)> 0) then
            !Compute scalar separation
            sep = sqrt( sum( rij * rij ) )
            !Compute displacement relative to preferred separation
            disp = sep - r0
            !Calculate energy
            PEnergy = PEnergy + kfac * disp*disp
        else if (j == atomnum-1 .and. mod(j,M) < M-1) then
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
            if ( d2 > rc2)  cycle
            id2 = 1./d2                 !inverse squared distance
            id6 = id2 * id2 * id2       !inverse sixth distance
            id12 = id6 * id6            !inverse twelfth distance
            PEnergy = Penergy + 4. * (id12 - id6) + shiftval

            !end nonbonded calculation
        endif
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
