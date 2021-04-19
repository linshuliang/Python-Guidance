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

### 2.2 Python multiprocessing 模块

* [multiprocessing 个人总结](./multi-process/README.md)
* [Python官方文档 multiprocessing 模块](https://docs.python.org/zh-cn/3.8/library/multiprocessing.html)
