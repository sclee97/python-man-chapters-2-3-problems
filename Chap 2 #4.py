# Calculates numerical values of solutions of a quadratic equation given inputs a, b, and c

a = 1
b = 2
c = 3

import numpy as np

a = a + 0j

x1 = (-b+np.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-np.sqrt(b**2-4*a*c))/(2*a)

print x1, x2

a = 1
b = 0
c = -16

import numpy as np

x1 = (-b+np.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b-np.sqrt(b**2-4*a*c))/(2*a)

print x1, x2