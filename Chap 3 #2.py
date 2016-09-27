# Gives array of 100 elements all equal to e
r = ones(100)
b = array(r)
b*exp(1)

# Gives array in 1-degree increments of all angles in degrees from 0 to 360 degrees 
s = arange(0, 361, 1)
c = array(s)

# Gives array in 1-degree increments of all angles in radians from 0 to 360 degrees
t = array(s)
radians(t)

# Gives array from 12 to 17 exclusive in 0.2 increments
u = arange(12, 17, 0.2)
d = array(u)
u

# Gives array from 12 to 17 inclusive in 0.2 increments
v = linspace(12, 17, 11)