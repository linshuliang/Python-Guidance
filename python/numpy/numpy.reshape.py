# coding=utf-8
# Syntax:
#     numpy.reshape(a, newshape, order='C')[source]
# Parameters:
#     a        : array to be reshaped.
#     newshape : int or tuple of ints
# Returns:
#     reshaped array.
import numpy as np

a = np.zeros((3, 10))

b = np.reshape(a, (5, 6))
print(b.shape)  #  (5, 6)

c = np.reshape(a, (10, -1))
print(c.shape)  # (10, 3)
