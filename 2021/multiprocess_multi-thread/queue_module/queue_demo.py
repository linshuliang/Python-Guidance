# coding=utf-8
import queue
import threading


def worker(q: queue.Queue):
    while True:
        # 从队列中移除并返回一个任务
        item = q.get()
        print("working on %s" % item)
        # 当调用get()获取任务后，调用task_done()表示该任务的处理已完成
        q.task_done()


if __name__ == "__main__":
    q = queue.Queue()
    # 创建线程
    t1 = threading.Thread(target=worker, args=(q, ), daemon=True)
    # 线程启动活动
    t1.start()
    # 往队列中添加任务
    for item in range(30):
        q.put(item)
    print("all tasks send")
    # 阻塞至队列中所有的任务都被接收和处理完毕
    q.join()
