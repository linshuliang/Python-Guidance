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
