# coding=utf-8
"""
Python 字典 popitem() 方法返回并删除字典中的最后一对键和值。
如果字典已经为空，却调用了此方法，就报出 KeyError 异常。

Syntax:
    popitem()

Returns:
    返回字典中的最后一个 键值对(key,value)
"""
dict_demo = {'a': 1, 'b': 2, 'c': 3}
pop_return = dict_demo.popitem()
print(pop_return)  # ('c', 3)
print(dict_demo)  # {'a': 1, 'b':2}

pop_default = dict_demo.popitem()
print(pop_default)  # ('b', 2)
print(dict_demo)  # {'a': 1}
