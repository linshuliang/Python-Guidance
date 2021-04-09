# Python 类

## 1 简介

Python 是一门面向对象编程（`Object Oriented Programming, OOP`）的语言，
这里的对象可以看做是由数据以及一系列可以存取、操作这些数据的方法所组成的集合。

面向对象编程主要有以下特点：

* 封装（Encapsulation）：对外部世界隐藏对象的工作细节
* 继承（Inheritance）  ：用基类进一步定义派生类
* 多态（Polymorphism） ：基类的引用/指针可指向派生类对象

在 Python 中，`元组(tuple)`、`列表(list)`、`集合(set)`、`字典(dict)`等数据类型是对象，`函数`也是对象。
那么，我们能创建自己的对象吗？
答案是肯定的。跟其他 OOP 语言类似，我们使用类来自定义对象。

### 1.1 类的定义

类是一个抽象的概念，我们可以把它理解为具有相同属性和方法的一组对象的集合，而实例是一个具体的对象。

Python 提供关键字 `class` 来声明一个类：

```python
class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am %s." % self.name)


if __name__ == "__main__":
    ani = Animal("dog")
    ani.greet()
```

* `__init__` 方法即为类的构造函数，创建实例时，需要传入与之匹配的参数；
* 类中的函数，第一个参数为 `self`，指向实例本身；
* 如果一个类不继承其他类，就显式地从`object`继承：
  * 所有类最终都会继承自`object`类；
  * 即使一个类不继承其他类，也要显式地从`object`继承，这样做可自动定义一些特殊的方法，这些方法实现了对象的默认语义；

### 1.2 访问限制

* 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，这样就变成了一个私有变量，只有内部可以访问，外部不能访问；
* 如果变量名前面只有一个下划线`_`，表示不要随意访问这个变量，虽然它可以直接被访问；
* 在 Python 中，以双下划线开头，并且以双下划线结尾的变量是特殊变量，例如`__name__`，特殊变量是可以直接访问的。所以，不要自定义 `__xxx__`这样的变量名；

```python
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == "__main__":
    bart = Student('Bart Simpson', 59)
    print('bart.get_name() =', bart.get_name())
    bart.set_score(60)
    print('bart.get_score() =', bart.get_score())
    # 类 className 中定义的 __xx 变量被Python解释器自动改成了 _className__xx
    # 虽然 Python 没有C++那样的阻止机制，但好的风格规范有利于代码的维护
    print('DO NOT use bart._Student__name:', bart._Student__name)
```

### 1.3 继承和多态

#### 1.3.1 继承

继承后，派生类可以拿到基类的所有数据和方法：

* 派生类可以重写基类的方法；
* 派生类也可以新增自己特有的方法；

```python
class Animal(object):
    def __init__(self, name=None):
        self.name = name
    def greet(self):
        print('Hello, I am %s.' % self.name)

# 直接从 Animal 类继承
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

    print('d is Animal?', isinstance(d, Animal)) # True
    print('d is Dog?',    isinstance(d, Dog))    # True
    print('d is Cat?',    isinstance(d, Cat))    # False
```

> 在继承关系中，如果一个实例的数据类型是某个派生类，那么它的数据类型也可以被看作是基类。

#### 1.3.2 多态

[多态](https://zh.wikipedia.org/wiki/%E5%A4%9A%E6%80%81_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6)) （polymorphism）是指为不同数据类型的实体提供统一的接口，或使用单一的符号来表示多个不同的类型。

* 把派生类对象赋给基类指针/引用，运行时根据对象的数据类型来选择调用的函数；
* Python 中，把派生类对象赋值给基类是允许的，但把基类对象赋值给派生类是禁止的；

例如：

```python
    hello(a)  # Hello, I am .
    hello(d)  # WangWang.., I am haba.
    hello(c)  # MiaoMiao.., I am kitty
```
