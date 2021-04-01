from collections import Iterator


class Fib(object):
    def __init__(self, maxLimit=100):
        self.a, self.b = 0, 1
        self.maxLimit = maxLimit

    # __iter__ 方法返回迭代器对象本身
    def __iter__(self):
        return self

    # __next__ 方法返回容器的下一个元素
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a < self.maxLimit:
            return self.a
        else:
            raise StopIteration


if __name__ == "__main__":
    fib = Fib()
    print("ininstance(fib, Iterator): ", isinstance(fib, Iterator))

    for element in fib:
        print(element)
