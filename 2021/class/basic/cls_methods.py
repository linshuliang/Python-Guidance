# coding=utf-8


class CMethodDemo:
    def __init__(self):
        self._name = "python"
        self._company = "oppo"

    @classmethod
    def info(cls):
        print("调用类方法 info.cls : ", cls)


if __name__ == "__main__":
    # 1 可直接通过类来调用类方法
    CMethodDemo.info()
    # 2 可使用类对象来调用类方法
    c1 = CMethodDemo()
    c1.info()
