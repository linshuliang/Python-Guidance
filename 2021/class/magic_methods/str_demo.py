# coding=utf-8


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        """
        调用 print 打印对象时，会调用对象的 __str__ 方法
        """
        return "Student object (name : %s)" % self.name

    """
    __repr__() 是为调试服务的
    """
    __repr__ = __str__


if __name__ == "__main__":
    s = Student("lqj")
    print(s)
