program add_arrays
    implicit none
    
    integer :: i, n
    real :: a(n), b(n), c(n)
    
    ! Read in the size of the arrays
    print *, "Enter the size of the arrays:"
    read *, n
    
    ! Read in the values of A and B
    print *, "Enter the values of A:"
    do i = 1, n
        read *, a(i)
    end do
    
    print *, "Enter the values of B:"
    do i = 1, n
        read *, b(i)
    end do
    
    ! Add A and B to get C
    do i = 1, n
        c(i) = a(i) + b(i)
    end do
    
    ! Print the result
    print *, "The sum of A and B is:"
    do i = 1, n
        print *, c(i)
    end do
    
end program add_arrays