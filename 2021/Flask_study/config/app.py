# coding=utf-8
from flask import Flask
from flask import request

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '123'


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        return "POST : hello flask\n"
    elif request.method == "GET":
        return "GET : hello flask\n"
