# coding=utf-8
# NumPy 为 ndarray 对象引入了一个简单的文件格式：npy
# npy 文件用于存储重建 ndarray 所需的数据、图形、dtype 和其他信息。
# load() 和 save() 函数是读写文件数组数据的两个主要函数，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为 .npy 的文件中。
import os
import numpy as np

a = np.random.randint(0, 10, (5, 6))
"""
def numpy.save(file, arr, allow_pickle=True, fix_imports=True):
    :param file: 要保存的文件，扩展名为 .npy，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上。
    :param arr: 要保存的数组。
"""
np.save('ndarray_a', a)

# 加载数据
b = np.load('ndarray_a.npy')
print(b)

# 删除文件
os.remove('ndarray_a.npy')
