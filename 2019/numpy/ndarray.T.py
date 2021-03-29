# coding=utf-8
# if type(arr) is numpy.ndarray:
#     transposed_arr = arr.T  # arr 的转置
#
# 简而言之，a.T 会返回 a 的转置
import numpy as np

a = np.arange(0, 18).reshape((2, 3, 3))
print('a: \n{}'.format(a))

print('\na.T: \n{}'.format(a.T))
