# coding=utf-8


class Student(object):
    def __init__(self, name):
        self._name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if not isinstance(val, int):
            raise ValueError("score must be an integer")

        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val

    @property
    def name(self):
        return self._name


if __name__ == "__main__":
    s1 = Student("plt")
    # s1.name = "zhu"  #  AttributeError: can't set attribute
    print(s1.name)

    s1.score = 99  # 调用 score.setter()，设置
    print(s1.score)  # 调用 @property score，获取
