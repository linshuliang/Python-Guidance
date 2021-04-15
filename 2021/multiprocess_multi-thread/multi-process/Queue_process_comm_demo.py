# -*- coding: utf-8 -*-
import time
from multiprocessing import Process, Queue


# 向队列中写入数据
def write_task(q: Queue):
    try:
        n = 1
        while n < 5:
            print("write, %d" % n)
            q.put(n)
            time.sleep(1)
            n += 1
    except BaseException:
        print("write_task error")
    finally:
        print("write_task end")


# 从队列读取数据
def read_task(q: Queue):
    try:
        n = 1
        while n < 5:
            print("read, %d" % q.get())
            time.sleep(1)
            n += 1
    except BaseException:
        print("read_task error")
    finally:
        print("read_task end")


if __name__ == "__main__":
    q = Queue()  # 父进程创建Queue，并传给各个子进程

    pw = Process(target=write_task, args=(q, ))
    pr = Process(target=read_task, args=(q, ))

    pr.start()  # 启动子进程 pr，读取
    pw.start()  # 启动子进程 pw，写入
    pw.join()  # 等待 pw 结束
    pr.join()  # 等待 pr 结束
    print("DONE")
