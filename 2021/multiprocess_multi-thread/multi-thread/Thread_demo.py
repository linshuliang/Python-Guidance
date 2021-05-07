# coding=utf-8
import time
import threading


def test(name: str):
    print("Begin, thread: %s" % threading.current_thread().name)
    print("hello %s" % name)
    time.sleep(2)
    print("End, thread: %s" % threading.current_thread().name)


if __name__ == "__main__":
    print("Begin, main thread: %s" % threading.current_thread().name)
    # 新建一个线程
    t1 = threading.Thread(target=test, args=("oppo", ), name="TestDemo")
    # 设置线程名称，覆盖初始化时的名称
    t1.setName("ThreadNewName")
    # 返回线程名称
    print("thread name: %s" % t1.getName())
    # 启动线程活动
    t1.start()
    # 返回线程是否活动的
    print(t1.is_alive())  # True
    # 阻塞，等待线程终止
    t1.join()
    # 返回线程是否活动的
    print(t1.is_alive())  # False
    print("End, main thread: %s" % threading.current_thread().name)
