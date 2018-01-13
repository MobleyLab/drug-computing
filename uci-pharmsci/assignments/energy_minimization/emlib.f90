

subroutine CalcEnergy(Pos, PEnergy, Dim, NAtom)
    implicit none
    integer, intent(in) :: Dim, NAtom
    real(8), intent(in), dimension(0:NAtom-1, 0:Dim-1) :: Pos
    real(8), intent(out) :: PEnergy
    real(8), dimension(Dim) :: rij, Posi
    real(8) :: d2, id2, id6, id12
    real(8) :: alpha
    integer :: i, j
    !alpha varies with system size
    alpha = 0.0001 * dble(NAtom)**(-2./3.)
    PEnergy = 0.
    do i = 0, NAtom - 1
        !store Pos(i,:) in a temporary array for faster access in j loop
        Posi = Pos(i,:)
        do j = i + 1, NAtom - 1
            rij = Pos(j,:) - Posi
            d2 = sum(rij * rij)
            id2 = 1. / d2            !inverse squared distance
            id6 = id2 * id2 * id2    !inverse sixth distance
            id12 = id6 * id6         !inverse twelvth distance
            PEnergy = PEnergy + 4. * (id12 - id6)
        enddo
        !compute the single-body term
        PEnergy = PEnergy + alpha * sum(Posi * Posi)
    enddo
end subroutine


subroutine CalcForces(Pos, Forces, Dim, NAtom)
    implicit none
    integer, intent(in) :: Dim, NAtom
    real(8), intent(in), dimension(0:NAtom-1, 0:Dim-1) :: Pos
    real(8), intent(out), dimension(0:NAtom-1, 0:Dim-1) :: Forces
    real(8), dimension(Dim) :: rij, Fij, Posi
    real(8) :: d2, id2, id6, id12
    real(8) :: alpha 
    integer :: i, j
    !alpha varies with system size
    alpha = 0.0001 * dble(NAtom)**(-2./3.)
    Forces = 0.
    do i = 0, NAtom - 1
        !store Pos(i,:) in a temporary array for faster access in j loop
        Posi = Pos(i,:)
        do j = i + 1, NAtom - 1
            rij = Pos(j,:) - Posi
            d2 = sum(rij * rij)
            id2 = 1. / d2            !inverse squared distance
            id6 = id2 * id2 * id2    !inverse sixth distance
            id12 = id6 * id6         !inverse twelvth distance
            Fij = rij * ((-48. * id12 + 24. * id6) * id2)
            Forces(i,:) = Forces(i,:) + Fij
            Forces(j,:) = Forces(j,:) - Fij
        enddo
        !compute the single-body term
        Forces(i,:) = Forces(i,:) - 2. * alpha *Posi 
    enddo
end subroutine


subroutine CalcEnergyForces(Pos, PEnergy, Forces, Dim, NAtom)
    implicit none
    integer, intent(in) :: Dim, NAtom
    real(8), intent(in), dimension(0:NAtom-1, 0:Dim-1) :: Pos
    real(8), intent(out) :: PEnergy
    real(8), intent(out), dimension(0:NAtom-1, 0:Dim-1) :: Forces
    real(8), dimension(Dim) :: rij, Fij, Posi
    real(8) :: d2, id2, id6, id12
    real(8) :: alpha
    integer :: i, j
    !alpha varies with system size
    alpha = 0.0001 * dble(NAtom)**(-2./3.)
    PEnergy = 0.
    Forces = 0.
    do i = 0, NAtom - 1
        !store Pos(i,:) in a temporary array for faster access in j loop
        Posi = Pos(i,:)
        do j = i + 1, NAtom - 1
            rij = Pos(j,:) - Posi
            d2 = sum(rij * rij)
            id2 = 1. / d2            !inverse squared distance
            id6 = id2 * id2 * id2    !inverse sixth distance
            id12 = id6 * id6         !inverse twelvth distance
            PEnergy = PEnergy + 4. * (id12 - id6)
            Fij = rij * ((-48. * id12 + 24. * id6) * id2)
            Forces(i,:) = Forces(i,:) + Fij
            Forces(j,:) = Forces(j,:) - Fij
        enddo
        !compute the single-body term
        PEnergy = PEnergy + alpha * sum(Posi * Posi)
        Forces(i,:) = Forces(i,:) - 2. * alpha *Posi
    enddo
end subroutine

