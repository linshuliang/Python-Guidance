# Python import - 导入

## 1 Python 模块

Python 模块，是一个 Python 文件，包含了 Python 对象定义和 Python 语句。
模块让你能够有逻辑地组织 Python 代码段。
把相关的代码分配到一个模块里能让代码更好用，更易懂。
模块能定义函数、类、变量，模块里也能包含可执行的代码。

### 1.1 `import` 语句

模块定义好后，我们可以使用 `import` 语句来引入模块，语法如下：

```python
import module1 [, module2[,... moduleN]]
```

采用 `import` 导入的模块，调用模块中的函数时，必须这么引用：

```python
模块名.函数名
```

### 1.2 搜索路径

当你导入一个模块，Python解释器对模块路径的搜索顺序是：

* 当前目录
* shell 变量 PYTHONPATH 中的每个目录
* 默认目录 （安装过程决定）

模块搜索路径存储在 `sys.path` 变量中。
变量中包含当前目录、PYTHONPATH 和由安装过程决定的默认目录。

> `sys.path` 是一个`list`，通过修改`sys.path`可修改`import`的搜索路径和搜索顺序。

例如:

```python
# 将当前文件所在的目录加入到模块搜索路径中
import os
import sys
sys.path.append(path.dirname(path.abspath(__file__)))
```

### 1.3 `from ... import` 语句

Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：

```python
from modname import name1 [, name2, ..., nameN]
```

如果想将模块全部引入，可使用：

```python
from modName import *
```

[如何控制模块被全部导入时的内容？](https://python3-cookbook.readthedocs.io/zh_CN/latest/c10/p02_control_the_import_of_everything.html)

> 可在模块中定义变量 `__all__` 来明确列出需要导出的内容。

如果没有自定义`__all__`，那么在全部导入时，不以下划线开头的`函数、类、变量`都会被导入。

## 2 Python 包

Python 包是一个分层次的文件目录结构，
它定义了一个由`模块`及`子包`，和`子包下的子包`等组成的 Python 应用环境。

简单来说，包就是文件夹，但该文件夹下必须存在 `__init__.py` 文件，
`__init__.py`文件的内容可以为空。`__init__.py`用于标识当前文件夹是一个包。

现展示包的构建与调用的一个示例：

* [`call_separate.py`](./call_separate.py)
* separate
  * [`__init__.py`](./separate_module/__init__.py)
  * [`run1.py`](./separate_module/run1.py)
  * [`run2.py`](./separate_module/run2.py)

> 封装成Python包是很简单的。在文件系统上组织你的代码，并确保每个目录都定义了一个`__init__.py`文件。

### 2.1 `__init__.py` 文件

定义模块的层次结构就像在文件系统上建立目录结构一样容易。
文件`__init__.py`的目的是要**包含不同运行级别的包的可选的初始化代码**。

举个例子，如果你执行了语句`import graphics`，文件`graphics/__init__.py`将被导入，建立`graphics`命名空间的内容。

如果要导入`import graphics.format.jpg`，
`graphics/__init__.py`和`graphics/formats/__init__.py`将在`graphics/formats/jpg.py`之前导入。

`__init__.py`文件的写法，会改变`import`的写法：

* 如果 `__init__.py` 为空，那么只能通过 `from module_name.file_name import func_name` 的方式来导入。例如 [`__init__.py`为空的包](./separate_module)
* 如果 `__init__.py` 中`import`了文件，那么在`import module_name`后可通过`module_name.file_name.func_name`来调用函数。例如 [`__init__.py`导入了文件](./integrate_file/)
* 如果 `__init__.py` 中直接`import`了函数，那么在`import module_name`后可通过`module_name.func_name`来调用函数。例如 [`__init__.py`导入了函数](./integrate_func/)

## 参考

* [RUNOOB - Python模块](https://www.runoob.com/python/python-modules.html)
* [Python3-cookbook 模块与包](https://python3-cookbook.readthedocs.io/zh_CN/latest/c10/p01_make_hierarchical_separate_of_modules.html)
