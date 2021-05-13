# coding=utf-8
import inspect
from .demo import func


def func2():
    print("Call %s" % inspect.stack()[0][3])
    func()
