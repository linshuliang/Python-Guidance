# coding=utf-8
import http.server
import socketserver

PORT = 8000

# 类 SimpleHTTPRequestHandler 用于创建基础的 webserver 文件服务，与当前目录关联
# 等同于 shell 中执行： python3 -m http.server 8000 --bind 127.0.0.1 --directory .
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port: ", PORT)
    httpd.serve_forever()
