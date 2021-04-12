# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == "__main__":
    bart = Student('Bart Simpson', 59)
    print('bart.get_name() =', bart.get_name())
    bart.set_score(60)
    print('bart.get_score() =', bart.get_score())
    # 类 className 中定义的 __xx 变量被Python解释器自动改成了 _className__xx
    # 虽然 Python 没有C++那样的阻止机制，但好的风格规范有利于代码的维护
    print('DO NOT use bart._Student__name:', bart._Student__name)
