# coding=utf-8
"""
Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。

语法
    fromkeys()方法语法：
        dict.fromkeys(seq[, value])

参数
    seq -- 字典键值列表。
    value -- 可选参数, 设置键序列（seq）的值。

返回值
    该方法返回一个新字典。
"""
seq = ('Google', 'Tencent', 'Ali')
print(dict.fromkeys(seq))
# {'Google': None, 'Tencent': None, 'Ali': None}

print(dict.fromkeys(seq, 10))
# {'Google': 10, 'Tencent': 10, 'Ali': 10}
