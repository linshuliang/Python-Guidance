# Flask

`Flask` 是典型的微框架，作为 web 框架来说，它仅保留了核心功能：

* 请求响应处理
* 模板渲染

这两类功能分别由 `Werkzeug`（WSGI 工具库）和 `Jinja`（模板渲染库）完成。

## 1 初识 Flask

编写一个 `app.py` 文件：

```python
# coding=utf-8
from flask import Flask

# 创建一个 Flask 对象
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Hello Flask"
```

在命令行中执行:

```shell
flask run
```

则会输出：

```shell
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

* 打开浏览器，地址栏填入 `http://127.0.0.1:5000/` 即可访问主页。
* `curl -X GET http://127.0.0.1:5000/` 则会返回 `Hello Flask`

### 1.1 `app.route()` 装饰器

使用 `app.route()` 装饰器，可以为函数绑定对应的`URL`。
当用户在浏览器访问这个`URL`时，就会触发这个函数，获取返回值，并把返回值显示到浏览器窗口。

### 1.2 Flask 请求的处理流程

* 当用户在浏览器地址栏访问这个地址，例如`http://localhost:5000/`
* 服务器解析请求，发现请求 URL 匹配的 URL 的`path` 是 `/`，因此调用对应的处理函数 `hello()`
* 获取 `hello()` 函数的返回值，处理后返回给客户端（浏览器）
* 浏览器接受响应，将其显示在窗口上

### 1.3 `flask run` 命令

> Flask 的默认设置：执行 `flask run` 时会自动调用当前路径中的 `app.py` 或者 `wsgi.py`。

如果当前路径没有 `app.py` 或者 `wsgi.py`，则需通过设置环境变量 `FLASK_APP` 来告诉 Flask 要启动的程序：

```shell
export FLASK_APP=hello.py
```

### 1.4 管理环境变量

`FLASK_ENV` 用来设置程序运行的环境，默认是 `production`。

在开发时，我们需要开启调试模式(`debug mode`)。
调试模式可以通过将系统环境变量 `FLASK_ENV` 设为 `development` 来开启。
调试模式开启后，当程序出错，浏览器界面上会显示错误信息。代码出现变动，会自动重载。

```shell
# Flask 开启调试模式
export FLASK_ENV=development
```

## 2 HTTP 方法

HTTP 协议（Web 应用的协议）中有访问 URL 的不同方法。
缺省情况下，一个路由只回应`GET`请求，但可通过`methods`参数使用不同的方法。

例如：

```python
# coding=utf-8
from flask import Flask
from flask import request  # 请求

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # 请求的方法
    if request.method == 'POST':
        return "flask.request.method : POST\n"
    else:
        return "flask.request.method : GET\n"
```

HTTP 方法（通常也被称为“动作”）告诉服务器一个页面请求要做什么。以下是常见的方法：

| HTTP 方法  | 作用 |
| :------:  | :------------------- |
| GET | 浏览器告诉服务器：只要得到页面上的信息并发送这些信息 |
| HEAD | 浏览器告诉服务器想要得到信息，但是只要得到信息头就行了，页面内容不要。一个应用应该像接受到一个 GET 请求一样运行，但是不传递实际的内容。在 Flask 中，你根本不必理会这个，下层的 Werkzeug 库会为你处理好 |
| POST | 浏览器告诉服务器想要向 URL 发表一些新的信息，服务器必须确保数据被保存好且只保存了一次。 HTML表单实际上就是使用这个请求向服务器传送数据的 |
| PUT | 与 POST 方法类似，不同的是服务器可能触发多次储存过程而把旧的值覆盖掉。你可能会问这样做有什么用？这样做是有原因的。假设在传输过程中连接丢失的情况下，一个处于浏览器和服务器之间的系统可以在不中断的情况下安全地接收第二次请求。在这种情况下，使用 POST 方法就无法做到了，因为它只被触发了一次。|
| DELETE | 删除给定位置的信息 |
| OPTIONS | 为客户端提供一个查询 URL 支持哪些方法的捷径。从 Flask 0.6 开始，自动为你实现了这个方法。|

## 3 Flask config - 配置处理

`Flask` 的 `config` 继承于字典，可以像字典一样修改它：

```python
app = Flask(__name__)
app.config['DEBUG'] = True
```

## 参考

* [Flask 入门教程](https://read.helloflask.com/)
* [Flask config - 配置处理](http://docs.jinkan.org/docs/flask/config.html)
