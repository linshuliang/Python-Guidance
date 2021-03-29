# coding=utf-8
import math


def justify_num(x):
    """
    数据类型检查可以用内置函数 isinstance() 实现
    """
    if (not isinstance(x, (int, float))):
        raise TypeError("Type Error")


def move(x, y, step, angle):
    """
    坐标移动
    """
    justify_num(x)
    justify_num(y)
    justify_num(step)
    justify_num(angle)

    nx = x + step * math.cos(angle)
    ny = x + step * math.sin(angle)
    return nx, ny


ret = move(100, 100, 60, math.pi / 6)
print(type(ret))  # <class 'tuple'>
print(ret)
