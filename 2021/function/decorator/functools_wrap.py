# coding=utf-8
from functools import wraps


def makeitalic(func):
    @wraps(func)
    def wrapped():
        return '<i>' + func() + '</i>'

    return wrapped


@makeitalic
def hello():
    return "hello world"


if __name__ == "__main__":
    print(hello())  # <i>hello world</i>
    print(hello.__name__)  # hello
