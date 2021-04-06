# coding=utf-8
from math import pow


def make_pow(n: int):
    def inner_func(x):
        return pow(x, n)

    return inner_func


if __name__ == "__main__":
    pow2 = make_pow(2)
    print(pow2)
    # <function make_pow.<locals>.inner_func at 0x7f9b6d89b670>
    print(pow2(9))
    # 81

    # del make_pow
    # pow3 = make_pow(3)
    # NameError: name 'make_pow' is not defined
    print(pow2(10))
    # pow2 仍可正常调用，自由变量 2 仍保存在 pow2 中

    pow2_1 = make_pow(2)
    print(pow2 == pow2_1)  # False
