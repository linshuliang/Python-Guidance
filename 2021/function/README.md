# Python 函数

## 1 基础

### 1.1 调用函数

函数名其实就是一个函数对象的引用，可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

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

### 1.2 定义函数

在 Python 中定义函数 ：
* 使用`def`语句，依次写出函数名、括号、括号中的参数和冒号`:`
* 在缩进块中编写函数体，函数的返回值用`return`语句返回

#### 1.2.1 空函数

如果想定义一个什么事也不做的空函数，可以用`pass`语句：

```python
def nop():
    pass
```

`pass`语句什么都不做，那有什么用？
实际上`pass`可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个`pass`，让代码能运行起来。

`pass`还可以用在其他语句里，比如：

```python
if age >= 18:
    pass
```

缺少了`pass`，代码运行就会有语法错误。

#### 1.2.2 Python 函数能返回多个值？

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

#### 1.2.3 Python 函数定义要诀

* 定义函数时，需要确定函数名和参数个数；
* 如果有必要，可以先对参数的数据类型做检查；
* 函数体内部可以用`return`随时返回函数结果；
* 函数执行完毕也没有`return`语句时，自动`return None`;
* 函数可以同时返回多个值，但其实就是一个`tuple`;



## 参考
* [廖雪峰的官方网站 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400/1017106984190464)
