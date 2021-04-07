# coding=utf-8
import time
from functools import wraps


def metric(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        t_begin = time.time()
        result = fn(*args, **kwargs)
        t_end = time.time()
        print('%s executed in %s ms' % (fn.__name__, (t_end - t_begin)))
        return result

    return decorator


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


if __name__ == "__main__":
    f = fast(11, 22)
    s = slow(11, 22, 33)
    print(f)
    print(s)
