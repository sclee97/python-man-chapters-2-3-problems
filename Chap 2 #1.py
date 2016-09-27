# Calculates height h and velocity v at a time t after a ball is thrown
h0 = 1.2 # meters
v0 = 5.4 # meters/second
g = 9.8
t = 0.5

height = h0 + v0*t - 0.5*g*t**2
velocity = v0 - g*t

print height
print velocity

t = 2.0

height = h0 + v0*t - 0.5*g*t**2
velocity = v0 - g*t

print height
print velocity

