# coding=utf-8


class Fib(object):
    def __init__(self, maxLimit=100):
        self._a, self._b = 0, 1
        self._maxLimit = maxLimit

    def __iter__(self):
        """
        该方法返回一个迭代对象
        """
        return self  # 实例本身就是迭代对象

    def __next__(self):
        self._a, self._b = self._b, self._a + self._b
        if self._a > self._maxLimit:
            raise StopIteration()
        return self._a


if __name__ == "__main__":
    for n in Fib(10):
        print(n)
