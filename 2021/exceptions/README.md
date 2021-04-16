# Python 异常处理

## 1 简介

一般情况下，在Python无法正常处理程序时就会发生一个异常。

异常是Python对象，表示一个错误。

当Python脚本发生异常时我们需要捕获并处理它，否则程序会终止执行。

## 2 捕捉异常并处理

`try/except`语句用来检测`try`语句块中的错误，从而让`except`语句捕获异常信息并处理。
如果你不想在异常发生时结束程序，只需在`try`里捕获它。

### 2.1 try-except-else 语句

```python
try:
    <语句>  # 执行代码
except <异常名称>:
    <语句>  # 如果 try 部分触发了此异常
else:
    <语句>  # 如果没有异常发生，执行 else 段的代码
```

* 如果当`try`中的语句块在执行时发生异常，Python就跳回到`try`并执行第一个匹配该异常的`except`子句，异常处理完毕，控制流就通过整个`try`语句（除非在处理异常时又引发新的异常）；
* 如果在`try`后的语句里发生了异常，却没有匹配的`except`子句，异常将被递交到上层的`try`，或者到程序的最上层（这样将结束程序，并打印默认的出错信息）；
* 如果在`try`子句执行时没有发生异常，Python将执行`else`语句后的语句（如果有`else`的话），然后控制流通过整个`try`语句；

Demo : 尝试打开文件并写入。

```python
import os

try:
    file_name = "test_open.txt"
    fh = open(file_name, "w")
    fh.write("Test : try-except-else \n")
except IOError as e:
    print(e)
else:
    print("Success : Open File %s" % file_name)
    fh.close()
    os.system("cat %s" % file_name)
    os.remove(file_name
```

### 2.2 except 不带任何异常类型

当 `except` 不带任何异常类型时，`try ... except ...` 会捕获所有发生的异常。

这其实是很糟糕的方式，因为即使发生了异常，我们也无法判断具体的异常信息。

### 2.3 `finally` 语句

`try ... finally` 语句：无论是否发生异常，都执行 `finally` 的字段。

```python
try:
    <语句>
finally:
    <语句>  # 退出try时总会执行
```

### 2.4 使用 `except ExceptionType as e` 打印出异常信息

```python
def convert2int(var) -> int:
    try:
        return int(var)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    convert2int("xyz")
```

程序输出为：

```shell
invalid literal for int() with base 10: 'xyz'
```

## 3 用户自定义异常

程序可以通过创建新的异常类来命名它们自己的异常。
异常应该直接或间接地从 `Exception` 类派生。

```python
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.

    Attributes:
        prev_stat -- state at beginning of transition
        next_stat -- attempted new state
        message   -- explanation of why the specific transition is not allowed
    """

    def __init__(self, prev_stat, next_stat, message):
        self.prev_stat = prev_stat
        self.next_stat = next_stat
        self.message = message

if __name__ == "__main__":
    try:
        raise InputError("int('xyz')", "Convertion Failure")
    except InputError as e:
        print(e.expression)
        print(e.message)
    finally:
        print("End")
```

自定义的异常可将名称以**Error**结尾，类似于标准异常的命名。

## 4 `raise` - 抛出异常

`raise` 语句用于抛出异常。

raise 唯一的参数就是要抛出的异常。这个异常可以是 Python 内置的异常，也可以是用户自定义的异常。

```python
try:
    raise ValueError("Forbidden")
except ValueError as e:
    print(e)

raise NameError("Name Not Exist")
```

## 5 使用`sys.exc_info`捕获异常

在实际调试程序的过程中，有时只获得异常的类型是远远不够的，还需要借助更详细的异常信息才能解决问题。

捕获异常时，有 2 种方式可获得更多的异常信息，分别是：

* 使用 `sys` 模块中的 `exc_info` 方法；
* 使用 `traceback` 模块中的相关函数。

```python
def sys.exc_info() -> tuple(exc_type, exc_value, exc_traceback):
    """
    返回 except 捕捉到的最近异常
    """
```

* `exc_type` : 异常的类型
* `exc_value` : 异常的实例
* `exc_traceback` : 一个 `traceback` 对象，封装了异常的堆栈信息。

示例：

```python
import sys
import traceback

try:
    raise ValueError("ValueError: raise")
except ValueError as e:
    print(e)
    print("=" * 20)

    ex_type, ex_val, ex_traceback = sys.exc_info()
    print(ex_type)  # 异常类型
    print(ex_val)   # 异常值
    for s in traceback.extract_tb(ex_traceback):
        print(s)    # 异常的堆栈信
```

## 参考

[Python官网 - 错误与异常](https://docs.python.org/zh-cn/3.6/tutorial/errors.html)
