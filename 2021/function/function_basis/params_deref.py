# coding=utf-8

_list = [1, 3, 2, 5]
_tuple = (1, 2, 6, 8)
_dict = {'1': 'a', '2': 'b', '3': 'c'}

print(_list, " --- ", *_list)
print(_tuple, " --- ", *_tuple)
print(_dict, " --- ", *_dict)
"""
[1, 3, 2, 5]  ---  1 3 2 5
(1, 2, 6, 8)  ---  1 2 6 8
{'1': 'a', '2': 'b', '3': 'c'}  ---  1 2 3
"""
