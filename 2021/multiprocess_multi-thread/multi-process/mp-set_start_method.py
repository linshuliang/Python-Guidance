# coding=utf-8
import multiprocessing as mp


def foo(q: mp.Queue):
    q.put("Hello")


if __name__ == "__main__":
    mp.set_start_method("fork")
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q, ))
    p.start()
    print(q.get())
    p.join()
