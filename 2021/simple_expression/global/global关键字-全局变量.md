# global 关键字

在 Python中，变量不需要先声明，直接使用即可，那我们怎么知道用的是局部变量还是全局变量呢？

首先：Python 使用的变量，在默认情况下一定是局部变量。

其次：Python 如果想使用作用域之外的全局变量，则需要加关键字 global。

## 示例1

```python
# coding=utf-8
a = 5


def test_1():
    a = 1
    print('In func test_1: a = %d' % a)


test_1()
print('global a = %d' % a)

# 程序执行结果为：
# In func test: a = 1
# global a = 5
```

可以看出，不加 global 时，函数内的局部变量与全局变量没有关联。

## 示例2

```python
# coding=utf-8
b = 5


def test_2():
    global b
    b = 1
    print('In func test_2: b = %d' % b)


test_2()
print('global b = %d' % b)

# 程序执行结果为：
# In func test_2: b = 1
# global b = 1
```

当加了 global 关键字时，使用的是全局变量。
