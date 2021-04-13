# coding=utf-8
from math import sqrt


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))


if __name__ == "__main__":
    p = Point(3, 4)
    print(p())
