# Python 高级特性

## 1 切片

取一个`list`或`tuple`的部分元素是极常见的操作。

`L[start, end]` 表示：从索引`start`开始取，直到索引`end`为止，但不包括索引`end`。

### 1.1 负数索引为倒序取值

* `L[-1]`  为倒数第一个元素
* `L[-n:]` 为倒数的`n`个元素
* `L[-n, -1]` 为 `L[-n], L[-n + 1], ..., L[-2]`，注意不包含 `L[-1]`

### 1.2 间隔取值

`L[start:end:interval]`：默认间隔`interval`为1，我们可设成其他数。

例子：

* `L[::2]` : 取间隔1个的元素
* `L[1:5:3]` : 取 `L[1], L[4]`
* `L[:30:10]` : 取 `L[0], L[10], L[20]`

## 2 迭代

在Python中，迭代是通过`for ... in`语句来完成的。

可直接作用于`for ... in`循环的数据类型包括：

* 一类是集合数据类型，如`list`、`tuple`、`dict`、`set`、`str`等
* 一类是生成器(`generator`)

这些可以直接作用于`for ... in`循环的对象统称为可迭代对象：`Iterable`。

> 可迭代对象(`Iterable`) 的定义 ：包含 `__iter__()` 方法或 `__getitem__()` 方法的对象称之为可迭代对象。

### 2.1 迭代 dict

* 默认情况下，`dict`迭代的是`key`
* 如果要迭代`value`，用`for v in d.values()`
* 如果要同时迭代`key`和`value`，用`for k, v in d.items()`

**dict 迭代 Demo**:
```python
d = {'a': 1, 'b': 2, 'c': 3}

# 默认情况下，dict 迭代的是键key
for k in d:
    print(k)

# 迭代值value
for v in d.values():
    print(v)

# 迭代键-值对 key-value
for k,v in d.items():
    print(k, v)
```

### 2.2 `enumerate` 索引-元素对

**enumerate 索引-元素对 Demo** :

```python
list_0 = ['A', 'B', 'C']

for i, value in enumerate(list_0):
    print(i, value)
```

## 3 迭代器

### 3.1 迭代器定义

迭代器是指遵循迭代器协议（iterator protocol）的对象。从这句话我们可以知道，迭代器是一个对象，但比较特别，它需要遵循迭代器协议，那什么是迭代器协议呢？

> 迭代器协议（iterator protocol）是指要实现对象的`__iter()__`和 `__next__()`，其中，`__iter()__`方法返回迭代器对象本身，`__next__()` 方法返回容器的下一个元素，在没有后续元素时抛出 `StopIteration` 异常。

#### 3.1.1 集合数据类型

```python
>>> from collections import Iterator
>>>
>>> isinstance((), Iterator)
False
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('', Iterator)
False
>>> isinstance(123, Iterator)
False
```

可见，`list`、`tuple`、`dict`、`set`、`str`等集合数据类型虽然是可迭代对象(`Iterable`)，却不是迭代器(`Iterator`)。

为什么集合数据类型不是迭代器？
> `list`、`tuple`、`dict`、`set`、`str`等集合数据类型只包含了`__iter__()` 方法，但不包含 `__next__()` 方法。

为什么集合数据类型不定义为迭代器？
> `Iterator`可以表示一个无限大的数据流，例如全体自然数。然而`list`、`tuple`、`dict`、`set`、`str` 存储空间有限，只能保存有限的数据。

#### 3.1.2 生成器都是迭代器对象`Iterator`

生成器是`Iterator`对象。

### 3.2 迭代器的本质 - 调用`next()`按需计算

Python的迭代器（`Iterator`）对象表示的是一个数据流，`Iterator`对象可以被`next()`函数调用并不断返回下一个数据，直到没有数据时抛出`StopIteration`错误。

可以把数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过`next()`函数按需计算下一个数据，所以`Iterator`的计算是惰性的，只有在需要返回下一个数据时它才会计算。

### 3.3 如何将可迭代对象(Iterable) 变为 迭代器对象(Iterator)

对于`list`、`tuple`、`dict`、`set`、`str`这些可迭代对象，可以使用 Python 内置的 [iter()](https://www.runoob.com/python/python-func-iter.html) 函数获得它们的迭代器对象。

### 3.4 `for ... in` 循环的本质

Python的`for ... in`循环就是先通过内置函数`iter()`获得一个迭代器，然后再不断调用`next()`函数实现的。

```python
def for_in(L, f):
    it = iter(L)  # 首先获得Iterator对象
    # 循环
    while True:
        try:
            x = next(it)  # 获得下一个值
            f(x)
        except StopIteration:
            break  # 遇到StopIteration就退出循环


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]
    for_in(L, print)
```

### 3.5 自定义迭代器

```python
# 将 Fibonacci 数列定义为一个迭代器
from collections import Iterator

class Fib(object):
    def __init__(self, maxLimit=100):
        self.a, self.b = 0, 1
        self.maxLimit = maxLimit

    # __iter__ 方法返回迭代器对象本身
    def __iter__(self):
        return self

    # __next__ 方法返回容器的下一个元素
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a < self.maxLimit:
            return self.a
        else :
            raise StopIteration


if __name__ == "__main__":
    fib = Fib()
    print("ininstance(fib, Iterator): ", isinstance(fib, Iterator))

    for element in fib:
        print(element)
```

## 4 生成器

生成器也是一种迭代器，在每次迭代时返回一个值，直到抛出异常（`raise StopIteration`）。

### 4.1 生成器的构造方法

**(1) 生成器表达式**

生成器表达式与列表推导式的定义方式相同，唯一的区别：

* 生成器表达式使用 `()`
* 列表推导式使用 `[]`

```python
# 生成器表达式
numbers = (x for x in range(5))
for num in numbers:
    print(num)
```

**(2) 生成器函数**

含有 `yield` 关键字的函数，调用该函数时会返回一个生成器。

### 4.2 生成器函数

带有`yield`的函数执行过程：

* 调用该函数的时候不会立即执行代码，而是返回了一个生成器对象；
* 当`next()` 作用于返回的生成器对象时，函数开始执行，在遇到 `yield` 的时候会『暂停』，并返回当前的迭代值；补充两点说明：
    * 在 `for ... in` 循环中会自动调用 `next()`；
    * 暂停时，会保留中断的位置和所有的变量值，也就是执行时的**上下文环境**被保留起来；
* 当再次使用`next()`的时候，函数会从原来『暂停』的地方继续执行，直到遇到 `yield`语句，如果没有`yield`语句，则抛出异常(`raise StopIteration`)；

简而言之，调用`yield`函数会返回生成器对象，`next()`使函数执行，`yield`使函数暂停。

**生成器 Demo**：

```python
# 通过 yield 来生成 Fibonacci 数列
def fib(maxLimit=100):
    a, b = 0, 1
    while(a < maxLimit):
        a, b = b, a+b
        yield a


if __name__ == "__main__":
    f_gen = fib(200)
    for item in f_gen:
        print(item)
```

处理大文件时，可使用生成器，详细参考[大文件分段处理](./big_file_rw/README.md)

## 参考

* [Python 切片](https://www.liaoxuefeng.com/wiki/1016959663602400/1017269965565856)
* [Python 迭代](https://www.liaoxuefeng.com/wiki/1016959663602400/1017316949097888)
* [极客学院 Python 生成器](https://wiki.jikexueyuan.com/project/explore-python/Advanced-Features/generator.html)
