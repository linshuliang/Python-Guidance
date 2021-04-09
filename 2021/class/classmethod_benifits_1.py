# coding=utf-8


class Info(object):
    object_num = 0

    def __init__(self):
        Info.object_num += 1

    @classmethod
    def get_intance_num(cls):
        return cls.object_num


if __name__ == "__main__":
    i1 = Info()
    i2 = Info()
    print(Info.get_intance_num())
