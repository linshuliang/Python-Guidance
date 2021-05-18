# coding=utf-8
from flask import Flask
from flask import escape

# print("name: ", __name__)  # app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Service is running\n"


@app.route("/home")
def totoro():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route("/user/<name>")
def user_page(name):
    return "User: %s\n" % escape(name)
