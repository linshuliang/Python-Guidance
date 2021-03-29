# coding=utf-8
"""
Python 字典 pop() 方法删除字典给定键(key)及对应的值(value)，返回值为被删除的值。

Syntax:
    pop(key[, default])
        * key: 要删除的键；
        * default: 如果dict 中不存在这个 key，则返回 default 值。

Returns:
    如果 key 存在，返回相应的 value.
    如果 key 不存在：
        * 如果设置了 default，则返回 default；
        * 如果没有设置 default，则报错 KeyError: 'key'
"""
dict_demo = {'a': 1, 'b': 2, 'c': 3}
pop_return = dict_demo.pop('b')
print(pop_return)  # 2

pop_default = dict_demo.pop('d', 5)
print(pop_default)  # 5
