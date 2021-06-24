# -*- coding: UTF-8 -*-
# 文件名：client.py
import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = "127.0.0.1"  # 获取本地主机名
port = 12345  # 设置端口号

s.connect((host, port))  # 打开一个 TCP 连接到主机为 hostname 端口为 port 的服务
data = s.recv(1024).decode()
print(data)
s.close()
