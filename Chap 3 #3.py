# Finds sequence of times as an array when ball passes each half meter assuming ball is dropped at t=0

import numpy as np

h0 = 10
y = arange(10, 0, -0.5)
g = 9.8

t = np.sqrt((2*(h0-y))/g)

print y, t

