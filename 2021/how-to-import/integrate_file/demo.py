# coding=utf-8
import inspect


def func():
    # inspect.stack()[0][3] : 获取当前函数的名称
    print("call %s" % inspect.stack()[0][3])
