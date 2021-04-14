# coding=utf-8
import os
from multiprocessing import Process


def info():
    print("=" * 10, "Enter info", "=" * 10)
    print("module name:", __name__)
    print("parent process id: ", os.getppid())
    print("process id: ", os.getpid())
    print("=" * 10, "Exit info", "=" * 10)


def fn(para):
    print("Enter fn : %s" % para)
    info()
    print("Exit fn")


if __name__ == "__main__":
    info()
    p = Process(target=fn, args=('oppo', ))
    p.start()
    p.join()
