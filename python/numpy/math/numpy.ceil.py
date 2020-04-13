# coding=utf-8
"""
def numpy.ceil(x)
    Return the floor of the input, element-wise.

    The floor of scalar `x` is the smallest integer i, such that `i >= x`
"""
import numpy as np
a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 3.8, 2.0])
print('Original arr: \n{}'.format(a))

floor_a = np.ceil(a)
print('After ceil: \n{}'.format(floor_a))
# [-1. -1. -0.  1.  2.  4.  2.]
