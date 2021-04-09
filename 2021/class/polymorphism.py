# coding=utf-8


class Animal(object):
    def __init__(self, name=''):
        self.name = name

    def greet(self):
        print('Hello, I am %s.' % self.name)


class Dog(Animal):
    def greet(self):
        print('WangWang.., I am %s.' % self.name)


class Cat(Animal):
    def greet(self):
        print('MiaoMiao.., I am %s' % self.name)


def hello(animal):
    animal.greet()


if __name__ == "__main__":
    a = Animal()
    d = Dog('haba')
    c = Cat('kitty')

    print('d is Animal?', isinstance(d, Animal))
    print('d is Dog?', isinstance(d, Dog))
    print('d is Cat?', isinstance(d, Cat))

    hello(a)  # Hello, I am .
    hello(d)  # WangWang.., I am haba.
    hello(c)  # MiaoMiao.., I am kitty
