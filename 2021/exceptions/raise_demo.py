# coding=utf-8

try:
    raise ValueError("Forbidden")
except ValueError as e:
    print(e)

raise NameError("Name Not Exist")
