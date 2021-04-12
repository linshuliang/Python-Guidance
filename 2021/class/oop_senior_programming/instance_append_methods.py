# coding=utf-8
from types import MethodType


class Student(object):
    pass


def set_age(self, age):
    self.age = age


if __name__ == "__main__":
    s = Student()
    # 给实例绑定属性
    s.name = "Michael"
    print(s.name)
    # 给实例绑定方法
    s.set_age = MethodType(set_age, s)
    s.set_age(25)
    print(s.age)
