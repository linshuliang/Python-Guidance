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


class Cat(Animal):
    def greet(self):
        super(Cat, self).greet()
        print("Miao")


if __name__ == "__main__":
    d = Dog("haba")
    d.greet()
    c = Cat("bu'ou")
    c.greet()
