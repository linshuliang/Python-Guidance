# coding=utf-8
# `for ... in` 循环的本质


def for_in(L, f):
    # 首先获得Iterator对象
    it = iter(L)
    # 循环
    while True:
        try:
            # 获得下一个值
            x = next(it)
            f(x)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]
    for_in(L, print)
