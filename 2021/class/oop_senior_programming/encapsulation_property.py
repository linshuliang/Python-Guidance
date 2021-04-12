# coding=utf-8


class Exam(object):
    def __init__(self, score=0):
        self._score = score

    def get_score(self):
        return self._score

    def set_score(self, val):
        if not isinstance(val, int):
            raise ValueError("score must be an integer")

        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val


if __name__ == "__main__":
    e1 = Exam(50)
    print(e1.get_score())

    e2 = Exam()
    e2.set_score(80)
    print(e2.get_score())
