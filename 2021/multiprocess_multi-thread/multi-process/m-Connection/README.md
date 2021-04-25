# 监听者和客户端

## 1 multiprocessing.connection.Client

尝试在监听者(服务端)上使用`address`地址初始化一个连接，返回 `Connection` 对象。

```python
multiprocessing.connection.Client(address, family=None, authkey=None) -> multiprocessing.connection.Connection:
```

参数：

* `address` : 地址
* `family` : 连接的类型，通常可忽略，可通过 `address` 的格式推导出来；
* `authkey` : `isinstance(authkey, bytes)`，`authkey`必须是`byte string`，认证密钥。

## 2 multiprocessing.connection.Listener

可以监听连接请求，是对`绑定套接字`或`Windows命名管道`的封装。

```python
multiprocessing.connection.Listener(address=None, family=None, backlog=1, authkey=None)
```

* `address` : 监听器对象中的绑定套接字 / Windows 命名管道
* `family` : 套接字使用的类型，可以是
  * `AF_INET` (TCP 套接字类型)
  * `AF_UNIX` (Unix 域套接字)

### 2.1 `Listener` 对象的方法

`accept()`

> 接受一个连接，并返回一个`Connection`对象，其连接的监听器对象已绑定了套接字/命名管道。
> 如果已经尝试过，并且认证失败了，则会抛出 `AuthenticationError` 异常。

`close()`

关闭监听器上的绑定套接字或者命名管道。此函数会在监听器被垃圾回收后自动调用。不过仍然建议显式调用函数关闭。

### 2.2 `Listener` 对象的属性

监听器对象拥有下列只读属性:

`address`

> 被监听器对象使用的地址

`last_accepted`

> 最后一个连接所使用的地址。如果没有的话就是 `None`

## 3 监听者-客户端 Demo

监听者（服务端）:

```python
# coding=utf-8
from array import array
from multiprocessing.connection import Listener

addr = ('localhost', 6000)

with Listener(addr, authkey=b'secret password') as l:
    # 被监听对象使用的地址
    print("address : ", l.address)  # ('127.0.0.1', 6000)

    with l.accept() as conn:
        # 最后一个连接所使用的地址，没有的话就是 None
        print("connection accepted from : ", l.last_accepted)  # ('127.0.0.1', 55750)
        # 发送对象
        conn.send([2.25, None, "junk", float])
        # 发送字节对象
        conn.send_bytes(b'hello')
        # 发送字节对象
        conn.send_bytes(array('i', [12, 33])
```

客户端：

```python
# coding=utf-8
from array import array
from multiprocessing.connection import Client

addr = ('localhost', 6000)

with Client(addr, authkey=b'secret password') as conn:

    print(conn.recv())
    print(conn.recv_bytes())

    arr = array('i', [0, 0, 0, 0, 0])
    print(conn.recv_bytes_into(arr))
    print(arr)
```

## 4 就绪状态

```python
multiprocessing.connection.wait(object_list, timeout=None)
```

一直等待直到 `object_list` 中某个对象处于就绪状态。返回 `object_list` 中处于就绪状态的对象。
如果`timeout`是一个浮点型，该方法会最多阻塞这么多秒。
如果`timeout`是`None`，则会允许阻塞的事件没有限制。
`timeout`为负数的情况下和为`0`的情况相同。

> 就绪状态: 当一个连接或者套接字对象拥有有效的数据可被读取的时候，或者另一端关闭后，这个对象就处于就绪状态。

```python
# coding=utf-8
import multiprocessing as mp

def foo(s):
    for i in range(10):
        s.send((i, mp.current_process().name))
    s.close()

if __name__ == "__main__":
    readers = list()

    for i in range(4):
        r, s = mp.Pipe(duplex =False)
        readers.append(r)
        p = mp.Process(target=foo, args=(s,))
        p.start()
        s.close()

    while readers:
        for r in mp.connection.wait(readers):
            try:
                msg = r.recv()
            except EOFError:
                readers.remove(r)
            else:
                print(msg
```

## 参考

[Python - 监听者及客户端](https://docs.python.org/zh-cn/3.6/library/multiprocessing.html#multiprocessing-listeners-clients)
