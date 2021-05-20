# coding=utf-8


def fn(i: int):
    return i * 2


if __name__ == "__main__":
    l = [1, 3, 5]
    result = map(fn, l)
    print(list(result))
