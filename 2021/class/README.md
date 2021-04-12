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
* 类中的实例函数，第一个参数为 `self`，指向实例本身；
* 如果一个类不继承其他类，就显式地从`object`继承：
  * 所有类最终都会继承自`object`类；
  * 即使一个类不继承其他类，也要显式地从`object`继承，这样做可自动定义一些特殊的方法，这些方法实现了对象的默认语义；

### 1.2 访问限制

* 如果要让内部属性不被外部访问，可以在属性的名称前加上两个下划线`__`，这样就变成了一个私有变量，只有内部可以访问，外部不能访问；
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

def hello(animal : Animal):
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

### 1.4 类方法和静态方法

#### 1.4.1 类方法

Python 类方法和实例方法相似，它最少也要包含一个参数：

* 实例方法的第一个参数为 `self`；
* 类方法的第一个参数为 `cls`；

类方法和实例方法的不同还有：

* 类方法需要使用`@classmethod`修饰符进行修饰；
* 类方法既可直接通过类来调用，也可通过使用实例来调用。实例方法必须通过实例来调用；

```python
# 类方法
class CMethodDemo:
    def __init__(self):
        self._name = "python"
        self._company = "oppo"

    @classmethod
    def info(cls):
        print("调用类方法 info.cls", cls)


if __name__ == "__main__":
    # 1 可直接通过类来调用类方法
    CMethodDemo.info()
    # 2 可使用实例来调用类方法
    c1 = CMethodDemo()
    c1.info()
```

#### 1.4.2 类方法(classmethod)的作用

* 当需要实现一些方法，其仅与类交互，而不需要和实例交互，那么`classmethod`有利于代码的维护；

    ```python
    class Info(object):
        object_num = 0
        def __init__(self):
            Info.object_num += 1

        @classmethod
        def get_intance_num(cls):
            return cls.object_num


    if __name__ == "__main__":
        i1 = Info()
        i2 = Info()
        print(Info.get_intance_num()  # 2
    ```

* `classmethod` 可作为工厂方法（`factory method`）提供额外的构造实例的途径；
* `classmethod` 可作为工厂类的借口，用来读取或者修改工厂类本身；

#### 1.4.3 静态方法

在类中有一些方法跟类有关系，但是又不会改变类和实例状态的方法，这种方法是**静态方法**。

静态方法，其实就是函数，和函数唯一的区别是，静态方法定义在**类命名空间**中，而函数定义在程序所在的空间（**全局命名空间**）中。

静态方法没有类似 `self`、`cls` 这样的特殊参数，因此 Python 解释器不会对它包含的参数做任何类或对象的绑定。也正因为如此，**类的静态方法，只能调用类的静态成员/静态方法，而无法调用类的非静态属性和非静态方法**。

> 静态方法使用 @staticmethod 装饰器，它是跟类有关系但在运行时又不需要实例和类参与的方法。可以使用类和实例来调用静态方法。

```python
class A(object):
    bar = 1
    @staticmethod
    def static_foo():
        print("A.bar = %d" % A.bar)


if __name__ == "__main__":
    # 1 可通过类直接调用静态方法
    A.static_foo()
    # 2 可通过实例调用静态方法
    a = A()
    a.static_foo()
```

### 1.5 获取对象信息

* `type()` 函数可用于判断对象类型；

    ```python
    >>> type(123)
    <class 'int'>
    >>> type('abc')
    <class 'str'>
    >>> type(None)
    <class 'NoneType'>
    >>> type(abs)
    <class 'builtin_function_or_method'>
    ```

* `isinstance(data, data_type)` 函数可用于判断数据的类型，其中第一个参数`data`为数据，第二个参数为数据的类型。

    ```python
    >>> isinstance(1, int)
    True
    >>> isinstance('abc', str)
    True
    ```

* 如果要获得对象的所有属性和方法，可使用 `dir()` 函数。

## 2 面向对象高级编程

### 2.1 `__slots__` 函数

Python 是动态语言:

* 当定义了`class`后，可以给该实例绑定属性和方法。
* 当创建了`class`的实例后，还可以给该实例绑定属性和方法。

```python
# coding=utf-8
# 给实例绑定属性和方法
from types import MethodType

class Student(object):
    pass

def set_age(self, age):
    self.age = age

if __name__ == "__main__":
    s = Student()
    # 给实例绑定属性
    s.name = "Michael"
    print(s.name)
    # 给实例绑定方法
    s.set_age = MethodType(set_age, s)
    s.set_age(25)
    print(s.age)
```

> 给一个实例绑定属性和方法，对其他实例是不起作用的。

```python
# coding=utf-8
from types import MethodType

class Student:
    pass

def set_score(self, s):
    self.score = s

# 给class添加方法
Student.set_score = set_score

if __name__ == "__main__":
    s1 = Student()
    s2 = Student()

    s1.set_score(75)
    s2.set_score(82)

    print(s1.score)
    print(s2.score)
```

> 给类`class`绑定属性/方法，所有的实例均可调用。

#### 2.1.1 使用 `__slots__`

为了达到限制的目的，Python 允许在定义`class`的时候，定义一个特殊的 `__slots__` 变量，来限制该`class`能添加的属性。

```python
# coding=utf-8

class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
    pass

s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'

try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)  
    # AttributeError: 'Student' object has no attribute 'score'

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)
```

### 2.2 使用 `@property` 方法

> `@property` 广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

先看一个例子：

```python
class Exam(object):
    def __init__(self, score=0):
        self._score = score

    def get_score(self):
        return self._score

    def set_score(self, val):
        if not isinstance(val, int):
            raise ValueError("score must be an integer")

        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val

if __name__ == "__main__":
    e1 = Exam(50)
    print(e1.get_score())

    e2 = Exam()
    e2.set_score(80)
    print(e2.get_score()
```

为了避免直接对属性`_score`操作，类`Exam`中定义了`get_score`和`set_score`方法，这样起到了封装对作用，把一些不想对外公开的属性隐蔽起来，只是提供方法给用户操作。

* 用于设置属性值的方法，称为 `setter`；
* 用于获取属性值的方法，称为 `getter`；

> Python 内置的 `@property` 装饰器，可将一个`getter`方法变成属性。

```python
class Student(object):
    def __init__(self, name):
        self._name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if not isinstance(val, int):
            raise ValueError("score must be an integer")

        if val < 0:
            self._score = 0
        elif val > 100:
            self._score = 100
        else:
            self._score = val

    @property
    def name(self):
        return self._name

if __name__ == "__main__":
    s1 = Student("plt")
    # s1.name = "zhu"  #  AttributeError: can't set attribute
    print(s1.name)

    s1.score = 99    # 调用 score.setter()，设置
    print(s1.score)  # 调用 @property score，获取
```

总结：

* `@property` 可将一个 `getter` 方法变为属性；
* 如果只定义了`@property`，而没有定义相应`setter`方法，那么这就是一个只读属性；
* 如果既定义了`@property`，又定义了相应的`setter`方法，那么这就是一个可读写属性；

## 参考

* [知乎 - Python 中的 classmethod 和 staticmethod 有什么具体用途？](https://www.zhihu.com/question/20021164)
