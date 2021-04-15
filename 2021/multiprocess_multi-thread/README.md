# Python 多进程和多线程

## 1 简介

* 计算机的核心是 CPU，它承担着计算任务。
* 单个CPU一次只能运行一个进程，其他进程处于非运行的状态。
* 一个进程可以包括多个线程。
* 一个进程的内存空间是共享的，每个线程都可以使用这些共享内存。
* 一个线程使用某些共享内存时，其他线程必须等它结束，才能使用这一块内存。

操作系统的设计，可归结为三点：

* 以多进程形式，允许多个任务同时运行；
* 以多线程形式，允许单个任务分成不同的部分运行；
* 提供协调机制，一方面防止进程之间和线程之间产生冲突，另一方面允许进程之间和线程之间共享资源。

参考链接：

* [阮一峰 - 进程与线程的一个简单解释](http://www.ruanyifeng.com/blog/2013/04/processes_and_threads.html)

## 2 多进程

### 2.1 `fork()` 函数

`Unix/Linux` 操作系统提供了一个`fork()`系统调用。
普通的函数调用，调用一次，返回一次。
但`fork()`调用一次，返回两次。
因为操作系统将当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回，返回值分别是：

* 父进程返回子进程的ID
* 子进程返回`0`

这样做的理由：父进程要记下每个子进程的`ID`，而子进程只需要调用`getppid()`就可以拿到父进程的`ID`。

Python 的 `os` 模块封装了常见的系统调用，其中就包括了 `fork`，可以在 Python 程序中轻松创建子进程。

```python
import os

pid = os.fork()

if pid < 0:
    print("Fail to create process")
elif pid == 0:
    print("I am child process (%s) and my parent is (%s)" % (os.getpid(), os.getppid()))
else:
    print("I (%s) just create a child process (%s)" % (os.getpid(), pid))
```

函数的运行结果为：

```shell
I (10688) just create a child process (10704)
I am child process (10704) and my parent is (10688)
```

有了 `fork` 调用，一个进程在接到新任务时，就可以复制出一个子进程来处理新任务。常见的 Apache 服务器就是由父进程来监听端口，每当有新的HTTP请求，就`fork`出子进程来处理新的`HTTP`请求。

### 2.2 multiprocessing 模块

[Python multiprocessing 模块](https://docs.python.org/zh-cn/3.8/library/multiprocessing.html)

#### 2.2.1 `Process` 类 - 创建进程

`multiprocessing`模块中包含的`Process`是一个用于创建进程对象的类。

`Process` 类的初始化方法为：

```python
class multiprocessing.Process(target=None, name=None, args=(), kwargs={})
```

其中：

* `target` 指明进程要执行的函数；
* `name` 是进程的名称；
* `args` 为函数的位置参数；
* `kwargs` 为函数的关键字参数；

```python
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
    p = Process(target=fn, args=('oppo',))
    p.start()
    p.join()
```

输出为：

```shell
========== Enter info ==========
module name: __main__
parent process id:  13021
process id:  15582
========== Exit info ==========
Enter fn : oppo
========== Enter info ==========
module name: __mp_main__
parent process id:  15582
process id:  15599
========== Exit info ==========
Exit fn
```

`Process` 类的方法：

`start()`

> 启动进程。这个方法每个进程对象最多调用一次。

`join()`

> 用于阻塞子进程以外的所有进程，当子进程执行完毕，父进程才会继续执行，它通常用于进程间的同步。

#### 2.2.2 在进程之间交换对象

`multiprocessing` 支持进程之间的两种通信通道：`Queue` 和 `Pipe`。

##### 多进程中的队列

Python队列是线程和进程安全的。

```python
# -*- coding: utf-8 -*-
import time
from multiprocessing import Process, Queue

# 向队列中写入数据
def write_task(q : Queue):
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
def read_task(q : Queue):
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

    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))

    pr.start()   # 启动子进程 pr，读取
    pw.start()   # 启动子进程 pw，写入
    pw.join()    # 等待 pw 结束
    pr.join()    # 等待 pr 结束
    print("DONE")
```

`Queue`对象包含以下方法：

* `put()` ：发送信号
* `get()` ：接收信号

##### 多进程中的管道

`Pipe()` 函数返回一个由管道连接的连接对象，默认情况是双向的。

定义：

```python
def Pipe(duplex: bool = ...) -> Tuple[connection.Connection, connection.Connection]:
```

示例：

```python
from multiprocessing import Process, Pipe

def fn(conn : Pipe):
    conn.send([50, None, "Hello"])  # 发送信号
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=fn, args=(child_conn,))
    p.start()  # 开始执行这个子进程
    p.join()   # 阻塞这个子进程以外的所有进程
    print(parent_conn.recv())  # 接收信号
```

`Pipe()`返回的两个连接对象表示管道的两端。每个连接对象都有`send()`和`recv()`方法。

* 如果两个进程（线程）尝试读取/写入管道的同一端，则管道中的数据有可能会损坏。
* 在不同进程中使用管道的不同端，也即一个进程`send()`，另一个进程`recv()`，那么就不存在损坏的风险。

### 2.2.3 Pool

如果要启动多个子进程，可采用进程池的方式批量创建子进程。`multiprocessing`的`Pool`用于生成进程池。

示例：

```python
import os
import time
import random
from multiprocessing import Pool

def long_time_task(name):
    print("Run task %s (%s)" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  # 线程池的大小是4
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.'
```

运行结果：

```shell
Parent process 25399.
Waiting for all subprocesses done...
Run task 0 (25416)
Run task 1 (25417)
Run task 2 (25418)
Run task 3 (25419)
Task 1 runs 0.05 seconds.
Run task 4 (25417)
Task 4 runs 0.63 seconds.
Task 0 runs 1.73 seconds.
Task 3 runs 2.22 seconds.
Task 2 runs 2.44 seconds.
All subprocesses done.
```

可看出，`task 0, 1, 2, 3` 是立刻执行的，而`task 4` 则要等待前面某个`task`完成后才能执行。
因为 `Pool` 被初始化为4，同一时刻最多有4个进程在执行。

`Pool`方法说明：

* `apply_async()` : 对`Pool`对象调用此方法，可以使每个进程异步执行任务，也就是说不用等上一个任务执行完毕再执行下一个任务；
* `close()` : 关闭进程池，确保没有新的进程加入；
* `join()` : 等待所有子进程执行完毕；
