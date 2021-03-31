# coding=utf-8
# 将数字字符串转换为浮点数
from functools import reduce

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}


def str2float(s: str) -> float:
    point = 0

    def to_float(f: float, n: int) -> float:
        nonlocal point
        if n == -1:
            point = 1
            return f

        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point

    return reduce(to_float, map(lambda ch: CHAR_TO_FLOAT[ch], s), 0.0)


if __name__ == "__main__":
    print(str2float('0'))
    print(str2float('123.456'))
    print(str2float('123.45600'))
    print(str2float('0.1234'))
    print(str2float('.1234'))
    print(str2float('120.0034'))
