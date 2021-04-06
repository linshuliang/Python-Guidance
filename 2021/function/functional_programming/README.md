# 函数式编程

## 1 简介

### 1.1 Python 函数

在 Python 中，我们可以像使用变量一样使用函数：

* 函数可以被赋值给变量
* 函数可以被删除
* 可以在函数中再定义函数
* 函数可以作为参数传递给另一个函数
* 函数可作为返回值

简而言之，函数就是一个对象。

### 1.2 函数式编程的特点

* 可以把函数作为参数传递给另一个函数，也就是`高阶函数`。
* 可以返回一个函数，这样就可以实现闭包或者惰性计算。

函数式编程的两个特点还仅仅是简化了代码。

### 1.3 函数式编程的特点

从代码的可维护性上讲，函数式编程最大的好处是引用透明，即函数运行的结果只依赖于输入的参数，
而不依赖于外部状态，因此，我们常常说函数式编程没有副作用。

没有副作用有个巨大的好处，就是函数内部无状态，即输入确定，输出就是确定的，容易测试和维护。

## 2 高阶函数

* 变量可以指向函数（函数名其实就是指向函数的变量）
* 传入函数（变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数）

内置函数示例：

* `map`
* `reduce`
* `filter`
* `sorted`

### 2.1 内置`map`函数

`map`的定义:

```python
def map(__func: Callable[[_T1], _S], __iter1: Iterable[_T1]) -> Iterator[_S]:
```

`map`的作用：

`map` 将传入的函数依次作用于序列的每个元素，并把结果作为新的 `Iterator` 返回。

### 2.2 `functools`库中的`reduce`函数

`reduce`函数定义：

```python
def reduce(function, sequence, initial=None) -> value:
```

`reduce`函数作用：

`reduce`把一个函数`f`作用在一个序列`[x1, x2, x3, ...]`上，这个函数`f`必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算，其效果就是:

```python
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

## 3 函数作为返回值(闭包)

在 Python 中，函数也是一个对象。因此，我们在定义函数时，可以再嵌套定义一个函数，并将该嵌套函数返回，比如：

```python
# coding=utf-8
from math import pow


def make_pow(n : int):
    def inner_func(x):
        return pow(x, n)  
    return inner_func


if __name__ == "__main__":
    pow2 = make_pow(2)
    print(pow2)
    # <function make_pow.<locals>.inner_func at 0x7f9b6d89b670>
    print(pow2(9))
    # 81

    del make_pow
    # pow3 = make_pow(3)
    # NameError: name 'make_pow' is not defined
    print(pow2(10))
    # pow2 仍可正常调用，自由变量 2 仍保存在 pow2 中
```

> 闭包 (Closure) : 一个函数返回了一个内部函数，该内部函数引用了外部函数的相关参数和变量，我们把该返回的内部函数称为闭包。

闭包的特点：

* 闭包的最大特点就是引用了自由变量，即使生成闭包的环境已经释放，闭包仍然存在； (携带状态)
* 闭包在运行时可以有多个实例，即使传入的参数相同。

  ```python
  pow_a = make_pow(2)
  pow_b = make_pow(3)
  pow_a == pow_b  # False
  ```

### 3.1 闭包最常见的误区 - 引用会变化的变量

```python
def count():
    funcs = list()
    for i in [1, 2, 3]:
        def f():
            print(i)
        funcs.append(f)

    return funcs

if __name__ == "__main__":
    f1, f2, f3 = count()
    f1()  # 3
    f2()  # 3
    f3()  # 3
```

为什么函数的返回结果是 `3 3 3`？

因为函数`f`引用了变量`i`，但函数`f`并非立刻执行。
当`for`循环结束时，变量`i`的值是3，所以`funcs`里面的函数引用的变量都是3。

> 返回一个函数时，要牢记该函数并未执行，返回函数尽量不要引用任何可能会变化的变量。

如果非要引用变量，怎么解决呢？

再创建一个函数，将循环变量的值传给该函数。

```python
def count_right():
    funcs = list()
    for i in range(1,4):

        def g(param : int):
            def f():
                print(param)
            return f

        funcs.append(g(i))
    return funcs
```

## 4 装饰器

### 4.1 装饰器简介

> 可以动态修改函数（类）功能的函数就是装饰器。本质上，它是一个高阶函数，以被装饰的函数为参数，并返回一个包装后的函数给被装饰函数。

先看一个例子，如何给字符串加上 HTML 标签 ：

```python
def hello():
    return "hello world"


def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped


if __name__ == "__main__":
    hello = makeitalic(hello)
    print(hello())
    # <i>hello world</i>
    print(hello.__name__)
    # wrappe
```

`makeitalic` 就是一个装饰器（decorator），它『装饰』了函数 `hello`，并返回一个函数`wrapped`，将其赋给`hello`。

可使用装饰器提供的`@`语法糖（Syntactic Sugar）来简化写法：

```python
def makeitalic(func):
    def wrapped():
        return "<i>" + func() + "</i>"
    return wrapped


@makeitalic
def hello():
    return "hello world
```
