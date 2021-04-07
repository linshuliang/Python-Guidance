# coding=utf-8


def makeitalic(func):
    def wrapped(*args, **kwargs):
        ret = func(*args, **kwargs)
        return '<i>' + ret + '</i>'

    return wrapped


@makeitalic
def hello(name):
    return "hello %s" % name


@makeitalic
def hello2(name1, name2):
    return "hello %s, %s" % (name1, name2)


if __name__ == "__main__":
    print(hello("plt"))
    print(hello2("lsl", "plt"))
