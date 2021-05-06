# coding=utf-8
import threading


def test(name: str):
    print("Begin, thread: %s" % threading.current_thread().name)
    print("hello %s" % name)
    print("End, thread: %s" % threading.current_thread().name)


if __name__ == "__main__":
    print("Begin, main thread: %s" % threading.current_thread().name)
    # 新建一个线程
    t1 = threading.Thread(target=test, args=("oppo", ), name="TestDemo")
    t1.start()
    t1.join()
    print("End, main thread: %s" % threading.current_thread().name)
