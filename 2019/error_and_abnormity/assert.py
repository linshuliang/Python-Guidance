# coding=utf-8
# Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
#
# 语法格式如下:
#     assert expression
#
# 等价于：
#     if not expression:
#         raise AssertionError
assert True
# assert False

assert 1 == 1
# assert 1==2

assert 1 == 2, '1 is not equal to 2'
