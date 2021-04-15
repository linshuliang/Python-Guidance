# coding=utf-8
import multiprocessing


def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = multiprocessing.Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
