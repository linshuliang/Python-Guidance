# coding=utf-8
import queue
import threading


def worker(q: queue.Queue):
    while True:
        # 从队列中移除并返回一个元素
        item = q.get()
        print("working on %s" % item)
        q.task_done()


if __name__ == "__main__":
    q = queue.Queue()
    # 创建线程
    t1 = threading.Thread(target=worker, args=(q, ), daemon=True)
    # 线程启动活动
    t1.start()
    # 往队列中添加元素
    for item in range(30):
        q.put(item)
    print("all tasks send")
    # 阻塞至队列中所有的元素都被接收和处理完毕
    q.join()
