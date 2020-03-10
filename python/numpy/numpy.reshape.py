# coding=utf-8
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html
# 语法: numpy.reshape(a, newshape, order='C')[source]
#   Parameters:
#       * a        : Array to be reshaped.
#       * newshape : int or tuple of ints
#   Returns  : reshaped array.
import numpy as np

a = np.zeros((3, 10))
b = np.reshape(a, (5, 6))
print(b)
c = np.reshape(a, (10, -1))
print(c)
