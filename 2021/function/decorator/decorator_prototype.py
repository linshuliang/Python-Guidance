# coding=utf-8


def hello():
    return "hello world"


def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"

    return wrapped


if __name__ == "__main__":
    hello = makeitalic(hello)
    print(hello())
    # <i>hello world</i>
    print(hello.__name__)
    # wrapped
