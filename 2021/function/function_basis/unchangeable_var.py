# coding=utf-8
# 不变对象


def add_end(L=None):
    if L is None:
        L = []
    L.append("end")
    return L


_list = [1, 2]
print(add_end(_list))  # [1, 2, 'end']


def add_end_wrong(L=[]):
    L.append("end")
    return L


print(add_end_wrong())  # ['end']
print(add_end_wrong())  # ['end', 'end']
