import numpy as np
from numpy.random import uniform, normal

## Linear regression

# given some 2d data with (x,y) values
x = np.sort(uniform(-10, 10, (100,1)), axis=0)
y = np.sort(normal(loc=0, scale=10, size=(100,1)), axis=0)

# we need to make a column of 1s in front of the X
X = np.hstack((np.ones((x.shape[0],1)), x))  # augmented with 1s

# calculate the hat matrix
# b = (X'X)-1X'Y