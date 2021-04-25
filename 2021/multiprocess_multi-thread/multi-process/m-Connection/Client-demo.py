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
