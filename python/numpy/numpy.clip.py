# coding=utf-8
# def clip(a, a_min, a_max, out=None):
#   limit each value of matrix `a` between [a_min, a_max].
import numpy as np

a = np.arange(10)
b = np.clip(a, 2, 6)
print('a:\n', a)
print('b:\n', b)
