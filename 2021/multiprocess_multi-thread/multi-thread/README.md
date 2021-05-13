# Python 多线程

## 1 简介

多线程类似于同时执行多个程序。多线程运行有以下优点：

* 使用线程可以把占据长时间的任务放到后台去处理；
* 用户界面可以更吸引人，这样比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度；
* 程序的运行速度可能加快；
* 在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等；

每个独立的进程有：

* 程序运行的入口
* 顺序执行序列
* 程序运行的出口

线程不能独立执行，必须依存在进程中，进程提供多个线程执行控制。

每个线程都有它自己的一组CPU寄存器，称为线程的上下文。
该上下文反映线程上次运行该线程的CPU寄存器的状态。

`指令指针寄存器`和`堆栈指针寄存器`是线程上下文中两个最重要的寄存器，
线程总是在进程的上下文中运行，这些地址都用于标志拥有`线程`的进程地址空间中的内存。

## 2 threading 模块

`threading`模块提供的其他方法：

* `threading.currentThread()` : 返回当前的线程变量；
* `threading.enumerate()` : 返回一个包含正在运行的线程的`list`。正在运行指线程启动后、结束前，不包括启动前和终止后的线程；
* `threading.activeCount()` : 返回正在运行的线程数量，与`len(threading.enumerate())`有相同的结果；

### 2.1 `threading.Thread` 类

```python
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
```


参数解释：

* `group` 应该为 `None`；为了日后扩展 `ThreadGroup` 类实现而保留。
* `target` 是用于 `run()` 方法调用的可调用对象。默认是 `None`，表示不需要调用任何方法。
* `name` 是线程名称。默认情况下，由 “Thread-N” 格式构成一个唯一的名称，其中 N 是小的十进制数。
* `args` 是用于调用目标函数的参数元组。默认是 `()`。
* `kwargs` 是用于调用目标函数的关键字参数字典。默认是 `{}`。
* 如果不是 `None`，`daemon` 参数将显式地设置该线程是否为守护模式。 如果是 `None` (默认值)，线程将继承当前线程的守护模式属性。

`threading.Thread`类的方法:

* `run()`: 用以表示线程活动的方法。
* `start()`: 启动线程活动，它在一个线程里最多只能被调用一次。
* `join([time])`: 等待至线程终止。这阻塞调用线程直至线程的`join()`方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
* `is_alive()`: 返回线程是否活动的。
* `getName()`: 返回线程名。
* `setName()`: 设置线程名。

`threading.Thread` 示例：

```python
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
```

### 2.2 重写 `threading.Thread` 模块创建线程

继承 `threading.Thread`，重写 `__init__` 和 `run` 方法，就可以自定义线程。

> 如果子类型重载了构造函数，它一定要确保在做任何事前，先调用基类构造器`Thread.__init__()`。

```python
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
```

### 2.3 `Lock` - 锁

多线程和多进程最大的区别在于：

* 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响；
* 多线程中，所有变量都由所有线程共享；

> 任何一个变量都可以被任何一个线程修改。因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容改乱了。

示例 - 两个线程在没有加锁的条件下同时修改一个全局变量，导致计算结果出错

```python
# coding=utf-8
import time
import threading

balance = 0

def change(n : int):
    global balance
    balance += n
    balance -= n


def loop(n : int):
    for i in range(2000000):
        change(n)


if __name__ == "__main__":
    t1 = threading.Thread(target=loop, args=(5,))
    t2 = threading.Thread(target=loop, args=(8,))
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print("[Total time %s] balance = %s" % (end-start, balance)
```

示例 - 修改共享的全局变量前加锁，保证一次只有一个线程在修改

```python
# coding=utf-8
import time
import threading

balance = 0
lock = threading.Lock()

def change(n : int):
    global balance
    balance += n
    balance -= n


def loop(n : int):
    for i in range(2000000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


if __name__ == "__main__":
    t1 = threading.Thread(target=loop, args=(5,))
    t2 = threading.Thread(target=loop, args=(8,))
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print("[Total time %s] balance = %s" % (end-start, balance))
```

当多个线程同时执行`lock.acquire()`时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。

获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
所以我们用`try...finally`来确保锁一定会被释放。

锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，
坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。

#### `class threading.Lock`

实现原始锁对象的类。一旦一个线程获得一个锁，会阻塞随后尝试获得锁的线程，直到它被释放；任何线程都可以释放它。

需要注意的是 `threading.Lock` 其实是一个工厂函数，返回平台支持的具体锁类中最有效的版本的实例。

```python
acquire(blocking=True, timeout=-1)
```

可以阻塞或非阻塞地获得锁。

```python
release()
```

释放一个锁。这个方法可以在任何线程中调用，不单指获得锁的线程。
当锁被锁定，将它重置为未锁定，并返回。

### `threading.Event` - 事件对象

线程之间通信最简单的机制之一：一个线程发出事件信号，而其他线程等待该信号。

一个事件对象，管理一个内部标志：

* 调用 `set()` 方法可设置其为 `True`
* 调用 `clear()` 方法可将其设置为 `False`
* 调用 `wait()` 方法将阻塞，直至标志为 `True`

```python
class threading.Event
```

实现事件对象的类。事件对象管理一个内部标志，调用 set() 方法可将其设置为true。调用 clear() 方法可将其设置为false。调用 wait() 方法将进入阻塞直到标志为true。这个标志初始时为false。

```python
is_set()
```

Return true if and only if the internal flag is true.

```python
set()
```

将内部标志设置为true。所有正在等待这个事件的线程将被唤醒。当标志为true时，调用 wait() 方法的线程不会被被阻塞。

```python
clear()
```

将内部标志设置为false。之后调用 wait() 方法的线程将会被阻塞，直到调用 set() 方法将内部标志再次设置为true。

```python
wait(timeout=None)
```

阻塞线程直到内部变量为true。如果调用时内部标志为true，将立即返回。否则将阻塞线程，直到调用 set() 方法将标志设置为true或者发生可选的超时。

当提供了timeout参数且不是 None 时，它应该是一个浮点数，代表操作的超时时间，以秒为单位（可以为小数）。
