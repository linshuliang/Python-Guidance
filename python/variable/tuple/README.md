# Python 元组

Python包含6中内建的序列：

* 列表
* 元组
* 字符串
* Unicode 字符串
* buffer 对象
* xrange 对象

序列通用的操作包括：

* 索引
* 求长度: `len(seq)`
* 组合，也即序列相加，`+`
* 重复，也即序列相乘，`*`
* 遍历，for 循环
* 求最小值: `min(seq)`
* 求最大值：`max(seq)`

## 创建元组

Python 的元组与列表类似，不同之处在于元组的元素是固定的，不能修改。
元组使用小括号，列表使用方括号。
创建元组很简单，只需要在括号中添加元素，并使用逗号`,`隔开即可。

如下实例：

```python
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
```

创建空元组：

```python
empty_tuple = ()
```

元组只包含一个元素时，需要在元素后面添加逗号：

```python
tup1 = (50,)
```

如果只有一个元素，且不加逗号, 那么相当于实数，不是创建出元组：

```python
tup = (2)  # 等同于 tup = 2
```

## 访问元组 - 索引

元组与字符串类似，下标索引从0开始，可以进行截取，组合等。

```python
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print('tup1[0] = {}'.format(tup1[0]))
print('tup2[1:5] = {}'.format(tup2[1:5]))
```

## 元组运算符

| 元组运算符       |  结果              | 描述                   |
|:---------------- | :----------------  | :--------------------- |
| len((1, 2, 3))   | 3                  | 计算元素个数           |
| (1, 2) + (5, 6)  | (1, 2, 5, 6)       | 连接元组               |
| (1, 2) * 3       | (1, 2, 1, 2, 1, 3) | 复制                   |
| 5 in (1, 2, 3)   | False              | 元素是否在元组中       |

## 元组迭代

```python
tup1 = (1, 2, 3, 5, 6)

for element in tup1:
    print(element)
```

## 列表和元组的异同有哪些？

### 相同点

1) 均具有序列的特性，均可以进行序列通用的操作；

2) 通常均使用括号表示，且括号内的元素以逗号分隔值出现，数据项均不需要具有相同的类型；

3) 均包含内置函数 `max`、`min`、`len`；

4) 可相互转换:
    * 列表转元组：`tuple(seq)`
    * 元组转列表：`list(seq)`