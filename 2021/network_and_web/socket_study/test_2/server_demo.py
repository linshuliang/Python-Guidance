# coding=utf-8
import socket

# 创建 socket 对象
s = socket.socket()
host = "127.0.0.1"
port = 8088
s.bind((host, port))

# 开始 TCP 监听
# 参数 backlog 指定在拒绝连接之前，系统可以挂起的最大连接数量
# 该值至少为 1，大部分设置为 5
s.listen(5)

while True:
    # Wait for an incoming connection.
    # Returns (socket object, address info) : a new socket representing the connection, and the address of the client.
    # For IP sockets, the address info is a pair (hostaddr, port)
    conn_sock, addr = s.accept()
    print("连接地址:", addr)
    conn_sock.send(b"Welcome")
    conn_sock.close()  # 关闭连接
