# coding=utf-8
"""
def numpy.floor(x)
    Return the floor of the input, element-wise.

    The floor of scalar `x` is the largest integer i, such that `i <= x`
"""
import numpy as np
a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 3.8, 2.0])
print('Original arr: \n{}'.format(a))

floor_a = np.floor(a)
print('After floor: \n{}'.format(floor_a))
# [-2. -2. -1.  0.  1.  3.  2.]
