# coding=utf-8


class A(object):
    bar = 1

    @staticmethod
    def static_foo():
        print("A.bar = %d" % A.bar)


if __name__ == "__main__":
    # 1 可通过类直接调用静态方法
    A.static_foo()
    # 2 可通过实例调用静态方法
    a = A()
    a.static_foo()
