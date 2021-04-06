# coding=utf-8


def count():
    funcs = list()
    for i in [1, 2, 3]:

        def f():
            print(i)

        funcs.append(f)

    return funcs


def count_right():
    funcs = list()
    for i in range(1, 4):

        def g(param: int):
            def f():
                print(param)

            return f

        funcs.append(g(i))
    return funcs


if __name__ == "__main__":
    f1, f2, f3 = count()
    f1()
    f2()
    f3()

    g1, g2, g3 = count_right()
    g1()
    g2()
    g3()
