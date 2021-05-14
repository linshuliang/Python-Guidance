import threading
import queue
import time
import random


def worker(q: queue.Queue, thread_id: int):
    while True:
        try:
            item = q.get(timeout=3)
            print("Thread %d, %s, %d" % (thread_id, time.ctime(time.time()), item))
            time.sleep(1)
            q.task_done()
        except queue.Empty:
            break


def source(num: int):
    for i in range(num):
        time.sleep(0.1)
        yield random.randint(1, 100)


if __name__ == "__main__":
    threads = []
    q = queue.Queue()

    num_worker_threads = 4
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker, args=(q, i))
        t.start()
        threads.append(t)

    for item in source(10):
        q.put(item)

    # 阻塞，直至线程结束
    for t in threads:
        t.join()

    # 阻塞，直至队列为空
    q.join()

    print("END")
