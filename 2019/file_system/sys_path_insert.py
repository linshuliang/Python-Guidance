# coding=utf-8
import sys
import os
"""[sys.path 简介]
type: 字符串列表

作用：用于指定模块的搜索路径。

值：从环境变量PYTHONPATH初始化，再加上与安装有关的默认值。

可修改：程序可自行设定 sys.path 这个列表的取值
"""
"""[sys.path.insert 简介]

sys.path.insert(1, “./crnn”) 定义搜索路径的优先顺序，

序号从0开始，表示最大优先级，sys.path.insert()加入的也是临时搜索路径，程序退出后失效。
"""
sys.path.insert(0, os.getcwd())

# 回顾，list 的 insert() 方法
mixed_list = [1, 'a', {1, 2}]
print(mixed_list)
mixed_list.insert(2, 2)
print(mixed_list)
