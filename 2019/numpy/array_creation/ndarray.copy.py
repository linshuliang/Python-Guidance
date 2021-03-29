# coding=utf-8
#
# numpy.copy(a, order='K')
#     Return an array copy of the given object.
#
import numpy as np

arr_0 = np.arange(0, 10).reshape((2, 5))
print('arr_0:\n{}\n'.format(arr_0))

# 浅拷贝，arr_1 就是 arr_0, 改变 arr_0 会改变 arr_1，反之亦然。
arr_1 = arr_0
print('arr_1:\n{}\n'.format(arr_1))

# 深拷贝，arr_2 是新的内存地址上的数据，改变 arr_1 不会改变 arr_2，反之亦然。
arr_2 = arr_0.copy()
print('arr_2:\n{}\n'.format(arr_2))

print('\n------- Change ------\n')
arr_0[0][0] = 20
print('arr_0:\n{}\n'.format(arr_0))
print('arr_1:\n{}\n'.format(arr_1))
print('arr_2:\n{}\n'.format(arr_2))
