# coding=utf-8


class Animal(object):
    def __init__(self, name):
        self._name = name

    def greet(self):
        print("Hello, i am %s." % self._name)


class Dog(Animal):
    def greet(self):
        super().greet()
        print("Wang")


if __name__ == "__main__":
    d = Dog("haba")
    d.greet()
