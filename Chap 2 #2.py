# Evaluates V in an expression containing V0, a, and z when these 3 variables are defined
V0 = 10
a = 2.5
z = 13./3
import numpy as np

V = V0*(1-z/(np.sqrt(a**2+z**2)))

print V

z=26./3

V = V0*(1-z/(np.sqrt(a**2+z**2)))

print V

z= 13.

V = V0*(1-z/(np.sqrt(a**2+z**2)))

print V