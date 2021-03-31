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

Python的`for ... in`循环可以用在所有的可迭代对象上，包括：

* `list`
* `tuple`
* `set`
* `str`
* `dict`
* 生成器（generator）
* 其他可迭代对象

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

### 2.2 enumerate 索引-元素对

**enumerate 索引-元素对 Demo** :

```python
list_0 = ['A', 'B', 'C']

for i, value in enumerate(list_0):
    print(i, value)
```

## 生成器

在Python中，一边循环一边计算的机制，称为生成器(generator)。





## 参考

* [Python 切片](https://www.liaoxuefeng.com/wiki/1016959663602400/1017269965565856)
* [Python 迭代](https://www.liaoxuefeng.com/wiki/1016959663602400/1017316949097888)
* [Python 列表生成器](https://www.liaoxuefeng.com/wiki/1016959663602400/1017317609699776)
