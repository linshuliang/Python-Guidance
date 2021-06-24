# coding=utf-8
import socket

# 创建一个 socket 对象，指定 域(domain) 和 协议(protocol)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 通过指定的 ·主机· 和 ·端口· 连接对端的服务器进程
s.connect(('127.0.0.1', 8088))

# 给服务器端发送数据
s.send(b'GET / HTTP/1.1\r\nHost: 127.0.0.1:8000\r\n\r\n')

# 接收服务器端发来的数据
data = s.recv(4096)
print(data)

# 关闭连接
s.close()
