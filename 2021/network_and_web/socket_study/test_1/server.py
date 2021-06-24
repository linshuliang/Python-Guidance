# coding=utf-8
import socket

# 创建 socket 对象，指定域(domain) 和 协议(protocol)
# AF_INET : 通过 IPv4 进行通信
# SOCK_STREAM :
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置 socket 选项，当服务器端进程终止后，
# 本例将 socket.S0.REUSEADDR 设为 1，
# 表示服务器进程终止后，操作系统会为它绑定的端口保留一段时间
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 将 socket 对象绑定到一个地址上
s.bind(('127.0.0.1', 8000))

# 侦听
s.listen(5)

while 1:
    cli_sock, cli_addr = s.accept()
    # 接收来自客户端发送的数据
    req = cli_sock.recv(4096)
    # 把数据发给客户端
    cli_sock.send(b'hello world')
    cli_sock.close()
