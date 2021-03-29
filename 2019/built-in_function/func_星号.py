# coding=utf-8
"""
星号 * 在函数传参中有以下作用：

    (1) 一个星号* 可把 序列/集合 转为位置参数。
    (2) 两个星号** 可把字典转为关键字参数。
"""
import os
import numpy as np


def handle(im_path=None, im_arr=None, im_info=None):
    if im_path is not None:
        print(im_path)

    if im_arr is not None:
        print(im_arr)

    if im_info is not None:
        print(im_info)


if __name__ == '__main__':
    path = os.getcwd()
    arr = np.linspace(1, 6, 3)

    print("一个星号`*`可把`序列/集合`转为位置参数:")
    series = [path, arr]
    handle(*series)

    print("两个星号`**`可把`字典`转为关键字参数:")
    dict_demo = {'im_arr': arr, 'im_path': path}
    handle(**dict_demo)

    print('* 号和关键字字段混用')
    handle(im_info='third', **dict_demo)
