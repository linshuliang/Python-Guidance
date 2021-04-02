# coding=utf-8
from math import sqrt, pow


class Point(object):
    """
    class Point 属于上下文管理器
    """

    def __init__(self, x, y):
        print("Initializing")
        self.x, self.y = x, y

    def __enter__(self):
        print("Entering Context")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exiting Context")
        print(exc_type)  # <type 'exceptions.AttributeError'>
        print(exc_value)  # 'Point' object has no attribute 'get_length'
        print(exc_traceback)  # <traceback object at 0x102c13050>
        return True  # 返回 True， 则忽略异常，不再对异常进行处理
        # return False  # 返回 False，重新抛出异常，让 with 之外的语句逻辑来处理异常
        # return        # 返回 None， 重新抛出异常，让 with 之外的语句逻辑来处理异常

    def get_distance(self):
        d = sqrt(pow(self.x, 2) + pow(self.y, 2))
        return d


if __name__ == "__main__":
    with Point(3, 4) as pt:
        print("Distance = ", pt.get_distance())
        pt.get_length()
