
subroutine CalcEnergy(Pos, L, rc, PEnergy, Dim, NAtom)
    implicit none
    integer, intent(in) :: Dim, NAtom
    real(8), intent(in), dimension(0:NAtom-1, 0:Dim-1) :: Pos
    real(8), intent(in) :: L, rc
    real(8), intent(out) :: PEnergy
    real(8), parameter :: k = 3000., r0 = 1.
    integer:: i, j
    real(8) :: d2, sep, disp, shiftval, rc2, id6, id2, id12
    real(8), dimension(Dim) :: rij, Posi
    

    !Assign initially zeros to the force array and potential energy
    PEnergy = 0.
    rc2 = rc**2

    !Precompute constants such as LJ shift value up here
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

        enddo
    enddo
end subroutine


