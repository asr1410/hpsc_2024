program variable_testing

implicit none

integer :: total
real :: average
complex :: cx
logical :: done
character(len = 80) :: message

total = 1000
average = 1.2934
done = .true.
message = "first fortran string type"
cx = (2.0, 4.0)

print *, total
print *, average
print *, cx
print *, done
print *, message

end program variable_testing