# coding=utf-8
from functools import partial


def multiply(x, y):
    return x * y


def subtract(x, y):
    return x - y


if __name__ == "__main__":
    double = partial(multiply, y=2)
    print(double(3))  # 等价于 multiply(3, 2)
    print(double(100))  # 等价于 multiply(100, 2)

    subtractByTen = partial(subtract, 10)
    print(subtractByTen(3))  # 等价于 subtract(10, 3)
    print(subtractByTen(30))  # 等价于 subtract(10, 30)
