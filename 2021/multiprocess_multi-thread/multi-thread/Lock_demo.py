# coding=utf-8
import time
import threading

balance = 0
lock = threading.Lock()


def change(n: int):
    global balance
    balance += n
    balance -= n


def loop(n: int):
    for i in range(2000000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


if __name__ == "__main__":
    t1 = threading.Thread(target=loop, args=(5, ))
    t2 = threading.Thread(target=loop, args=(8, ))
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print("[Total time %s] balance = %s" % (end - start, balance))
