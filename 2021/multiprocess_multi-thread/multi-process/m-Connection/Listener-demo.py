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
        conn.send_bytes(array('i', [12, 33]))
