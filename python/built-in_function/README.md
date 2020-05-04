# Python 内建函数

## 三个标准库的查询函数

Python 标准库很强大，此处先给出最常用的三个函数：

| 函数名称   | 功能                                                                    |
|:-----------| :---------------------------------------------------------------------- |
| type(obj)  | 确认对象 obj 属于哪种数据类型                                           |
| dir(obj)   | 返回对象 obj 的内置方法与属性的列表，列出特定数据类型能做是所有事情     |  
| help()     | 返回对象、方法或模块的文档                                              |

## 序列函数

| 函数名称                     | 功能                                                                                                        |
|:-----------------------------| :---------------------------------------------------------------------------------------------------------- |
| enumerate(series)            | 将序列组合为索引序列，返回 [(i, series[i]) for i in range(len(series))]                                     |
| sum(series)                  | 对序列进行求和，返回序列中所有元素的和                                                                      |
| zip(series1, series2)        | 将序列中的同位元素进行打包，返回 [(series1[i], series2[i]) for i in range(min(len(series1), len(series2)))] |

## 数学函数

| 函数名称                     | 功能                                                                    |
|:-----------------------------| :---------------------------------------------------------------------- |
| round(x, n)                  | 保留小数点的 n 位                                                       |