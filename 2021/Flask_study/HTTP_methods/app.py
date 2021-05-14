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
