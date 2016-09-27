import numpy as np

h0 = 10
y = arange(10, 0, -0.5)
g = 9.8

t = np.sqrt((2*(h0-y))/g)

print y, t

t[1:20]
t[0:19]
z = t[1:20] - t[0:19]

v = 0.5/z

print z