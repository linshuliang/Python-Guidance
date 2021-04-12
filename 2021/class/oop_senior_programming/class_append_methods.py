# coding=utf-8
from types import MethodType


class Student:
    pass


def set_score(self, s):
    self.score = s


# 给class添加方法
Student.set_score = set_score

if __name__ == "__main__":
    s1 = Student()
    s2 = Student()

    s1.set_score(75)
    s2.set_score(82)

    print(s1.score)
    print(s2.score)
