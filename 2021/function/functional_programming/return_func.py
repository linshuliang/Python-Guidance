# coding=utf-8


def createCounter():
    m = 0

    def counter():
        nonlocal m
        m += 1
        return m

    return counter


if __name__ == "__main__":
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(),
          counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
