# coding=utf-8
import time
import threading


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        def print_time(threadName, delay, counter):
            while counter:
                time.sleep(delay)
                print("%s: %s" % (threadName, time.ctime(time.time())))
                counter -= 1

        print("Begin : ", self.name)
        print_time(self.name, self.counter, 5)
        print("End : ", self.name)


if __name__ == "__main__":
    t1 = myThread(1, "Thread-1", 1)
    t2 = myThread(2, "Thread-2", 2)
    t1.start()
    t2.start()
