# Python 列表

Python包含6种内建的序列：

* 元组
* 列表
* 字符串
* Unicode 字符串
* buffer 对象
* xrange 对象

序列通用的操作包括：

* 索引
* 切片
* 检查成员: `in`
* 组合，也即序列相加，`+`
* 重复，也即序列相乘，`*`
* 遍历，for 循环
* 求最小值: `min(seq)`
* 求最大值：`max(seq)`
* 求长度: `len(seq)`

## 创建列表

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

```python
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
```
## 访问列表 - 索引

与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。
使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符（切片），如下所示：


```python
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# list1[0]:  physics
# list2[1:5]:  [2, 3, 4, 5]
```

## 列表运算符

| 列表运算符       |  结果              | 描述                   |
|:---------------- | :----------------  | :--------------------- |
| len([1, 2, 3])   | 3                  | 计算元素个数           |
| [1, 2] + [5, 6]  | [1, 2, 5, 6]       | 连接列表               |
| [1, 2] * 3       | [1, 2, 1, 2, 1, 2] | 复制                   |
| 5 in [1, 2, 3]   | False              | 元素是否在列表中       |

## 列表迭代

```python
tup1 = (1, 2, 3, 5, 6)

for element in tup1:
    print(element)
```

## 对列表的数据项进行修改或更新

列表对象包含以下方法：

| 方法                                        | 作用                                                        |
|:-----------------------------------------   | :---------------------------------------------------------  |
| list.append(obj)                            | 在列表末尾添加新的对象                                      |
| list.count(obj)                             | 统计某个元素在列表中出现的次数                              |
| list.extend(seq)                            | 用新列表扩展原来的列表                                      |
| list.index(obj)                             | 从列表中找出某个值第一个匹配项的索引位置                    |
| list.insert(index, obj)                     | 将对象插入列表                                              |
| list.pop([index=-1])                        | 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值|
| list.remove(obj)                            | 移除列表中某个值的第一个匹配项                              |
| list.reverse()                              | 反向列表中元素                                              |
| list.sort(cmp=None, key=None, reverse=False)| 对原列表进行排序                                            |

示例：

```python
>>> a.append('c')
>>> a
[1, 2, 3, 'c']
>>> a.append('5')
>>> a
[1, 2, 3, 'c', '5']
>>> a.append(2)
>>> a
[1, 2, 3, 'c', '5', 2]
>>> a.count(2)
2
>>> a.count(1)
1
>>> a.count('a')
0
>>> a.extend([8, 9])
>>> a
[1, 2, 3, 'c', '5', 2, 8, 9]
>>> a.append([8, 9])
>>> a
[1, 2, 3, 'c', '5', 2, 8, 9, [8, 9]]
>>> a.remove(2)
>>> a
[1, 3, 'c', '5', 2, 8, 9, [8, 9]]
>>> a.pop()
[8, 9]
>>> a
[1, 3, 'c', '5', 2, 8, 9]
>>> a.pop(index=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop() takes no keyword arguments
>>> a.pop(0)
1
>>> a
[3, 'c', '5', 2, 8, 9]
>>> a.pop(-1)
9
>>> a
[3, 'c', '5', 2, 8]
>>> a.pop(2)
'5'
>>> a
[3, 'c', 2, 8]
>>> a.insert(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: insert() takes exactly 2 arguments (1 given)
>>> a.insert(3, 'orange')
>>> a
[3, 'c', 2, 'orange', 8]
>>> a.reverse()
>>> a
[8, 'orange', 2, 'c', 3]
>>> a.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
>>> b = [5, 2, 6]
>>> b
[5, 2, 6]
>>> b.sort()
>>> b
[2, 5, 6]
```
