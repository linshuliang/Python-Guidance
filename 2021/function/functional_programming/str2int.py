# coding=utf-8
# 将数字字符串转换为整数
from functools import reduce

DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def str2int(s: str) -> int:
    num = reduce(lambda x, y: x * 10 + y, map(lambda c: DIGITS[c], s), 0)
    return num


s = "1238956"
i = str2int(s)
print(type(i))  # <class 'int'>
print(i)
