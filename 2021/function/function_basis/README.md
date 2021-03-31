# Python 函数基础

## 1 调用函数

函数名其实就是一个函数对象的引用，可以把函数名赋给一个变量，相当于给这个函数起了一个`别名`：

**例 1** ：

```python
a = abs  # 把函数名赋给一个变量
positive_a = a(-1)  # 被赋值的变量为函数对象
print(positive_a)
```

**例 2** :

```python
# 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
n1 = 255
n1_hex = hex(n1)
print(n1_hex)  # 0xff
```

## 2 定义函数

在 Python 中定义函数 ：
* 使用`def`语句，依次写出函数名、括号、括号中的参数和冒号`:`
* 在缩进块中编写函数体，函数的返回值用`return`语句返回

## 2.1 空函数

如果想定义一个什么事也不做的空函数，可以用`pass`语句：

```python
def nop():
    pass
```

`pass`语句什么都不做，那有什么用？
实际上`pass`可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个`pass`，让代码能运行起来。

`pass`还可以用在其他语句里，例如：

```python
if age >= 18:
    pass
```

缺少了`pass`，代码运行就会有语法错误。

## 2.2 Python 函数能返回多个值？

* 从表象来看，Python 函数能返回多个值
* 但实质上，Python 函数返回的是一个 `tuple`

**例3** ：

```python
# coding=utf-8
import math

def justify_num(x):
    """
    数据类型检查可以用内置函数 isinstance() 实现
    """
    if(not isinstance(x, (int, float))):
        raise TypeError("Type Error")


def move(x, y, step, angle):
    """
    坐标移动
    """
    justify_num(x)
    justify_num(y)
    justify_num(step)
    justify_num(angle)

    nx = x + step * math.cos(angle)
    ny = x + step * math.sin(angle)
    return nx, ny


ret = move(100, 100, 60, math.pi/6)
print(type(ret))  # <class 'tuple'>
print(ret)
```

## 2.3 Python 函数定义要诀

* 定义函数时，需要确定函数名和参数个数；
* 如果有必要，可以先对参数的数据类型做检查；
* 函数体内部可以用`return`随时返回函数结果；
* 函数执行完毕也没有`return`语句时，会自动`return None`;
* 函数可以同时返回多个值，但其实就是一个`tuple`;

## 3 函数的参数

函数的参数包括：

* 位置参数
* 默认参数 (使用默认参数最大的好处就是降低函数调用的复杂度)
* 可变参数
* 关键字参数
* 命名关键字参数

## 3.1 默认参数

定义默认参数要牢记一点：默认参数必须指向`不变对象`。

为什么要设计`str`、`None`这样的不变对象呢？
* 不变对象一旦创建，对象内部的数据就不能修改，这样就减少了修改数据导致的错误；
* 由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有；

我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成`不变对象`。

例如:
```python
def add_end(L=None):
    if L is None:
        L = []
    L.append("end")
    return L

_list = [1, 2]
print(add_end(_list))  # [1, 2, 'end']
```

如果默认参数不是`不变对象`，当调用函数多次时，会出现错误，例如：

```python
def add_end_wrong(L=[]):
    L.append("end")
    return L

print(add_end_wrong())  # ['end']
print(add_end_wrong())  # ['end', 'end']
```

**错误原因分析**：

Python 函数在定义的时候，默认参数`L`的值就被计算出来了，即空列表`[]`。因为默认参数`L`也是一个变量，它指向对象`[]`，如果调用该函数时改变了`L`的内容，则下次调用时默认参数的内容就会改变，不再是最初的空列表`[]`。

## 3.2 可变参数和关键字参数

* `*args`是可变参数，`args`接收的是一个`tuple`；
* `**kw`是关键字参数，`kw`接收的是一个`dict`；

调用函数时，传入可变参数和关键字参数的语法：

* 可变参数
    * 可直接传入，例如`func(v1, v2, v3)`；
    * 可先组装成`list`或`tuple`，再通过`*args`传入，例如`func(*(v1, v2, v3))`；
* 关键字参数
    * 可直接传入，例如`func(v1=1, v2=2)`;
    * 可先组装成`dict`，再通过`**kw`传入，例如`func(**{v1:1, v2:2})`

**例子：可变参数**
```python
def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # greeting='Hi', args=()
hello('Hi', 'Sarah') # greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # greeting='Hello', args=('Bart', 'Lisa')
```

**例子：关键字参数**
```python
def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_scores(Adam=99, Lisa=88, Bart=77)

data = {
    'Adam Lee': 99,
    'Lisa S': 88,
    'F.Bart': 77
}

print_scores(**data)
```

## 3.3 Python中星号(*, **)的作用

* 一个星号 `*` 可将 `list/tuple` 解包(unpack)为位置参数
* 两个星号 `**`可将 `dict` 解包为关键字参数

## 3.4 命名关键字参数

如果要限制关键字参数的名字，就可以用命名关键字参数。

和关键字参数`**kw`不同，命名关键字参数需要一个特殊分隔符`*`，`*`后面的参数被视为命名关键字参数。

例如，只接收`gender`、`city`、`age`作为关键字参数。这种方式定义的函数如下：

```python
def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()

print_info('Bob',  gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)
```

* 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
* 在没有可变参数的情况下，定义命名的关键字参数，不要忘了写分隔符`*`，否则定义的将是位置参数。

# 参考
* [廖雪峰的官方网站 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400/1017106984190464)
