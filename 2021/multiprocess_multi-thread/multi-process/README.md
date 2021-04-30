# Python multiprocessing 模块

`multiprocessing` 支持三种启动进程的方法：

* `spawn`
* `fork`
* `forkserver`

可通过调用:

```python
multiprocessing.set_start_method(method : str)
```

来设定进程的启动方法。

例如：

```python
import multiprocessing as mp

def foo(q : mp.Queue):
    q.put("Hello")

if __name__ == "__main__":
    mp.set_start_method("fork")
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
```

## 1 `Process` 类 - 创建进程

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

> 启动进程，这个方法每个进程对象最多调用一次。

`join([timeout])`

> 如果可选参数`timeout`是`None`（默认值），则该方法将阻塞子进程以外的所有进程，当子进程执行完毕，父进程才会继续执行，它通常用于进程间的同步。如果`timeout`是一个正数，它最多会阻塞`timeout`秒。
> 一个进程可以被`join` 多次。
> 进程无法`join`自身，因为这会导致死锁。尝试在进程启动之前`join`进程是错误的。

`close()`

> 关闭`Process`对象，释放与之关联的所有资源。

`run()`

表示进程活动的方法，函数实现为:

```python
def run():
    target(*args, **kwargs)
```

`terminate()`

> 终止进程。在Unix上，这是使用`SIGTERM`信号完成的；

`kill()`

> 终止进程。在Unix上使用`SIGKILL`信号；

`exitcode`

> 子进程的退出代码，如果进程尚未终止，`exitcode`为`None`；

`is_alive()`

> 返回进程是否还活着。从`start()`方法返回到子进程终止之前，进程对象都处于活动状态。

### multiprocessing.Process 类的方法

```python
# coding=utf-8
import time
import multiprocessing
import signal

# 创建 Process 对象
p = multiprocessing.Process(target=time.sleep, args=(1000,))

# 当前进程并没有 start， is_alive() 返回 False
print(p, p.is_alive())

# 启动进程
p.start()

# 当前进程已经 start, 而且仍未终止， is_alive() 返回 True
print(p, p.is_alive())

# 终止进程
p.terminate()

# 间隔 0.1s
time.sleep(0.1)

# 进程已终止，is_alive() 返回 False
print(p, p.is_alive())

# 进程退出时，返回码为 p.exitcode
print(p.exitcode == -signal.SIGTERM)  # True
```

## 2 进程之间的通信

`multiprocessing` 支持进程之间的两种通信通道：`Queue` 和 `Pipe`。

### 2.1 `Queue` - 多进程中的队列

定义：

```python
class multiprocessing.Queue([maxsize])
```

`multiprocessing.Queue`会返回一个使用管道和少量锁/信号量实现的共享队列实例。
当一个进程将一个对象放进队列中，一个写入线程会启动并将对象从缓冲区写入管道中。

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
    pr = Process(target=read_task,  args=(q,))

    pr.start()   # 启动子进程 pr，读取
    pw.start()   # 启动子进程 pw，写入
    pw.join()    # 等待 pw 结束
    pr.join()    # 等待 pr 结束
    print("DONE")
```

`Queue`对象包含以下方法：

`put(obj, block=True, timeout=None)`

> 将`obj`放入队列。如果可选参数`block`是`True`而且`timeout`是`None`，将会阻塞当前进程，直到有空的缓冲槽。
> 如果`timeout`是正数，将会在阻塞了最多`timeout`秒之后还是没有可用的缓冲槽时抛出`queue.Full`异常。
> 当`block`是`False`时，仅当有可用缓冲槽时才放入对象，否则抛出`queue.Full` 异常 (在这种情形下`timeout`参数会被忽略)。

`get(block=True, timeout=None)`

> 从队列中取出并返回对象。如果可选参数`block`是`True`(默认值) 而且`timeout` 是`None` (默认值), 将会阻塞当前进程，直到队列中出现可用的对象。
> 如果`timeout`是正数，将会在阻塞了最多`timeout`秒之后还是没有可用的对象时抛出`queue.Empty`异常。
> 当`block`是`False`时，仅当有可用对象能够取出时返回，否则抛出`queue.Empty`异常 (在这种情形下`timeout`参数会被忽略)。

`put_nowait(obj)`

> 等同于`put(obj, False)`，仅当有可用缓冲槽时才放入对象，否则抛出`queue.Full`异常。

`get_nowait()`

> 等同于 `get(False)`，仅当有可用对象能够取出时返回，否则抛出 `queue.Empty` 异常。

### 2.2 `Pipe` - 多进程中的管道

定义：

```python
def Pipe(duplex: bool = ...) -> Tuple[connection.Connection, connection.Connection]:
```

`Pipe`返回一对`Connection`对象`(conn1, conn2)`，分别表示管道的两端。

参数 `duplex`:

* 如果 `duplex` 被置为 `True` (默认值)，那么该管道是双向的。
* 如果 `duplex` 被置为 `False`，那么该管道是单向的，即 `conn1` 只能用于接收消息，而 `conn2` 仅能用于发送消息。

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

### 2.3 Connection - 连接对象

`Connection`对象允许收发可以序列化的对象或字符串。它们可以看作面向消息的连接套接字。

#### `class multiprocessing.connection.Connection`

`send(obj)`

> 将一个对象发送到连接的另一端，可用 `recv` 读取。

`recv()`

> 返回由另一端使用 `send()` 发送的对象，
> 该方法会一直堵塞，直到接收到对象，
> 如果对端关闭了连接，或者没有东西可接收，将抛出 `EOFError` 异常。

`poll([timeout])`

> 返回连接对象中是否有可以读取的数据。是返回`True`，否返回`False`；
> 如果未指定 `timeout`，此方法会马上返回；
> 如果 `timeout` 是一个数字，则指定了最大堵塞的秒数；
> 如果 `timeout` 是 `None`，那么将一直等待，不会超时；

`send_bytes(buffer)`

> 从一个字节类对象(`bytes-like object`)中取出字节数组，并作为一条完整消息发送。

`recv_bytes(maxlength)`

> 以字符串形式，返回一条从连接对象另一端发送过来的字节数据。
> 此方法在接收到数据前一直堵塞。
> 如果连接对象被对端关闭，或者没有数据可读取，将抛出 `EOFError` 异常。
> 如果给定了 `maxlength` 并且消息长于 `maxlength`，那么将抛出 `OSError` 并且该连接对象将不再可读。

#### multiprocessing.connection.Connection Demo

```python
# coding=utf-8
import multiprocessing as mp

s, r = mp.Pipe()

# 发送对象
s.send([1, 'hello', None])
# 接收对象
print(r.recv())

# 发送字节类对象
s.send_bytes(b'thank you')
# 接收字节类对象
print(r.recv_bytes())
```

监听者和客户端常用到`Connection`，详情可查看[监听者和客户端](./m-Connection/README.md)

## 3 Pool - 进程池

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
    p = Pool(4)  # 进程池的大小是4
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
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

## 4 进程间共享状态

并发编程，通常最好尽量避免使用共享状态。使用多个进程时尤其如此。

如果需要在进程间共享状态，`multiprocessing`模块提供了两种方法：

* 共享内存 - `multiprocessing.Value` / `multiprocessing.Array`
* 服务进程 - `multiprocessing.Manager`

优缺点比较：

* 使用服务进程管理器比使用共享内存对象更灵活，因为它们可以支持任意对象类型。此外，单个管理器可以通过网络由不同计算机上的进程共享。
* 共享内存比服务进程快。

### 4.1 Manager - 服务进程管理器

由 `Manager()` 返回的管理器对象控制一个服务进程，
该进程保存Python对象，并允许其他进程使用代理操作它们。

```python
import multiprocessing

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = multiprocessing.Process(target=f, args=(d, l))
        p.start()
        p.join()

        print(d)
        print(l)
```
