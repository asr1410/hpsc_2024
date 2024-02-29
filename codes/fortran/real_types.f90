program real_types

implicit none

real :: p, q, resr

integer :: i, j, resi

p = 2.0
q = 3.0
i = 2
j = 3

resr = p/q
resi = i/j

print *, resr
print *, resi

end program real_types