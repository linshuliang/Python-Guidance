# coding=utf-8


class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am %s." % self.name)


if __name__ == "__main__":
    ani = Animal("dog")
    ani.greet()
