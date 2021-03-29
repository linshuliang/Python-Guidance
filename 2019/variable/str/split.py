# coding=utf-8
# help(str.split)
# Syntax:
#     S.split(sep=None, maxsplit=-1)
str_demo = '123,456,789,0'

print(str_demo)
# 123,456,789,0

print(str_demo.split())
# ['123,456,789,0']

print(str_demo.split(','))
# ['123', '456', '789', '0']

print(str_demo.split(',', maxsplit=2))
# ['123', '456', '789,0']
