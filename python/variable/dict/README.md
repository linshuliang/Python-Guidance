# Python 字典 dict

字典是一种可变容器模型，可存储任意类型对象。

字典的每个键值对 `key=>value` 用冒号 `:` 分割，每个键值对之间用逗号 `,` 分割，整个字典包括在花括号 `{}` 中，格式如下所示：

```python
d = {key1: value1, key2: value2}
```

## 字典的特性

* 字典的键的数据类型必须为`字符串/数字/元组`，而字典的值可以取任意的数据类型。
* 字典的键(key) 是 **唯一** 的，如果重复，最后面一个键值对会替换前面的，例如：

```python
dict_1 = {'a': 1, 'b':2, 'a':3, 'b': 5}
print(dict_1)  # {'a': 3, 'b': 5}
```

## 访问字典的值

把相应的键放入方括弧

```python
# coding=utf-8

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])  # Zara
print("dict['Age']: ", dict['Age'])  # 7

# 如果字典不存在相应的键，会报错
print(dict['Gender'])
# KeyError: 'Gender'
```

## 修改字典

可以增加新的键值对，也可以修改或删除已有的键值对。

### dict 包含了以下内置方法

```python
class dict(object):
    def clear():
        D.clear() -> None.  Remove all items from D.

    def copy():
        D.copy() -> a shallow copy of D

    def fromkeys(iterable, value=None):  # from builtins.type
        Returns a new dict with keys from iterable and values equal to value.

    def get(k, d):
        D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

    def items():
        D.items() -> a set-like object providing a view on D's items

    def keys():
        D.keys() -> a set-like object providing a view on D's keys

    def pop(k[, d]):
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised

    def popitem():
        D.popitem() -> (k, v), remove and return some (key, value) pair as a
        2-tuple; but raise KeyError if D is empty.

    def setdefault(k[, d]):
        D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

    def update(E):
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]

    def values():
        D.values() -> an object providing a view on D's values
```

| 方法                                 | 作用                                                                         |
|:-----------------------------------  | :--------------------------------------------------------------------------- |
| dict.keys()                          | 以列表返回一个字典所有的键                                                   |  
| dict.values()                        | 以列表返回字典中的所有值                                                     |
| dict.items()                         | 以列表返回可遍历的(键, 值) 元组                                              |
| dict.get(key[, default=None])        | 如果键在字典中，返回该键的对应值；如果键不在字典中，返回 default 值          |
| dict.setdefault(key[, default=None]) | 如果键在字典中，返回该键的对应值；如果键不在字典中，将在dict中添加键值对(key, default)，并返回default |
| dict.update(dict2)                   | 把字典 dict2 的 `键/值对` 添加到 dict 里                                     |
| dict.fromkeys(seq, value)            | 创建一个新字典，以序列seq 中的元素做字典的键，value 为字典所有键对应的初始值。|
| dict.pop(key[, default])             | 删除字典给定键(key)及对应的值(value)，返回值为被删除的值。                   |
| dict.popitem()                       | 删除字典中的最后一个键值对，返回值为(last\_key, last\_value)                 |
| dict.clear()                         | 删除字典内所有元素，字典变为空字典，此函数没有返回值。                       |

示例：

```python
# dict.keys()
>>> d0 = {'Name': 'Zara', 'Age': 7}
>>> d0
{'Name': 'Zara', 'Age': 7}
>>> d0.keys()
dict_keys(['Name', 'Age'])
>>> type(d0.keys())
<class 'dict_keys'>
>>> list(d0.keys())
['Name', 'Age']

# dict.values()
>>> d0.values()
dict_values(['Zara', 7])
>>> type(d0.values())
<class 'dict_values'>
>>> list(d0.values())
['Zara', 7]

# dict.get()
>>> d0
{'Name': 'Zara', 'Age': 7}
>>> d0.get('Name', 'HM')
'Zara'
>>> d0.get('Sale', 1000)  # 如果键不再字典中，则返回 default 值
1000
>>> d0  # dict.get() 不会改变字典
{'Name': 'Zara', 'Age': 7}
>>> d0.get('Sale')

# dict.setdefault()
>>> d0.setdefault('Sale')  # dict.setdefault() 会改变字典
>>> d0
{'Name': 'Zara', 'Age': 7, 'Sale': None}
>>> d0.setdefault('Fashion', True)
True
>>> d0
{'Name': 'Zara', 'Age': 7, 'Sale': None, 'Fashion': True}
```
