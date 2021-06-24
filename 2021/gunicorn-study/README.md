# gunicorn

## 1 简介

![green unicorn logo](./gunicorn_logo.jpg)

[Gunicorn](https://docs.gunicorn.org/en/stable/index.html) 全称是 Green unicorn，它是一个适用于 UNIX 的 Python WSGI HTTP 服务器。
Gunicorn 服务器与各种 web 框架广泛兼容，实现简单，服务资源少，速度相当快。

特性：

* 原生支持 `WSGI`, `Django`, `Paster`
* 自动管理工作进程
* 简单的 Python 配置
* 多个工作器配置
* 可拓展的各种服务挂钩(Sever hook)
* 兼容 Python 3.5 以上版本

## 2 运行 Gunicorn

Gunicorn 的安装：

```shell
pip install -U git+https://github.com/benoitc/gunicorn.git
```

### 2.1 终端执行命令 `gunicorn`

安装 `gunicorn` 包后，可在终端执行 `gunicorn` 命令：

```shell
gunicorn [OPTIONS] [WSGI_APP]
```

其中 `WSGI_APP` 的常见形式为 `$(MODULE_NAME):$(VARIABLE_NAME)`。

常见命令行选项(OPTIONS) ：

* `-c CONFIG, --config=CONFIG` ：指定配置文件，默认为`./gunicorn.conf.py`；
* `-b BIND, --bind=BIND` ：指定一个服务器套接字(server socker)，形式为 `$(HOST)`, `$(HOST):$(PORT)`，默认为`127.0.0.1:8000`；
* `-w WORKERS, --workers=WORKERS` ：处理请求的工作进程数目；

在终端执行 `gunicorn -h`，可查看所有的选项。

#### 示例1

`readline_app.py ` ：读取输入，并显示

```python
# coding=utf-8
from gunicorn import __version__

def app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain'), ('Transfer-Encoding', "chunked"),
                        ('X-Gunicorn-Version', __version__)]
    start_response(status, response_headers)
    body = environ['wsgi.input']

    lines = []
    while True:
        line = body.readline()
        if line == b"":
            break
        print(line)
        lines.append(line)

    return iter(lines)
```

在 `readline_app.py` 目录下执行命令以启动服务：

```shell
gunicorn -w3 readline_app:app
```

在同机器的另一个终端下发送请求：

```shell
curl -X POST -d 'test\r\ntest2\r\n' -H "Transfer-Encoding: Chunked" http://localhost:8000
```

### 2.2 配置的优先级

`gunicorn` 命令启动服务时，其配置加载的优先级为（由低到高）：

* 框架设置(Framework Settings)
* 配置文件，默认为`./gunicorn.conf.py`
* [环境变量 GUNICORN_CMD_ARGS](https://docs.gunicorn.org/en/stable/settings.html#settings)
* 命令行选项(Command Line)

### 2.3 配置文件

配置文件是一个 python 源文件，文件名拓展为`.py`，默认为 `./gunicorn_conf.py`。
配置文件中可指定的配置选项可参考 [Gunicorn Settings](https://docs.gunicorn.org/en/stable/settings.html#logging)。

示例：

```python
# 指定服务器套接字(server sock)
bind = '0.0.0.0:8000'

# 在工作进程分叉前，加载应用程序
# 通过预加载应用程序，可以节省一些 RAM 资源，并缩短服务器启动时间
preload_app = True

# 处理请求的工作进程数目
workers = 4

# 工作进程的类别
worker_class = 'egg:meinheld#gunicorn_worker'

# 日志输出等级
loglevel = 'info'

# 启用 gRPC
from framework import grpc_server
import chat_gen_grpc
grpc_server.enable(chat_gen_grpc.setup, port=50051)
```

## 参考

* [gunicorn简介、架构、安装与配置](https://blog.csdn.net/bbwangj/article/details/82684573)
* [Gunicorn-配置详解](https://blog.csdn.net/y472360651/article/details/78538188?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-8.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-8.control)
