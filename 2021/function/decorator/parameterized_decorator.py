# coding=utf-8


def wrap_in_tag(tag):
    def decorator(func):
        def wrapped(*args, **kwargs):
            ret = func(*args, **kwargs)
            return '<' + tag + '>' + ret + '</' + tag + '>'

        return wrapped

    return decorator


@wrap_in_tag('b')
def hello(name):
    return "hello %s" % name


@wrap_in_tag('p')
def hello2(name1, name2):
    return "hello %s, %s" % (name1, name2)


if __name__ == "__main__":
    print(hello("plt"))
    print(hello2("plt", "lsl"))
