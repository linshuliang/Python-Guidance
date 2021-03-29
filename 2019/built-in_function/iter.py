# coding=utf-8
# list, tuple 都是可迭代对象，
# 通过 iter() 函数，可获得这些可迭代对象的迭代器，
# 然后，我们就能对迭代器使用 next() 函数来获取下一条数据。
"""
>>> li = [1, 2, 3, 4, 5]
>>> iter(li)
<list_iterator object at 0x104e3b9e8>
>>> next(iter(li))
1
>>> next(iter(li))
1
>>> li_iter = iter(li)
>>> next(li_iter)
1
>>> next(li_iter)
2
>>> next(li_iter)
3
>>> next(li_iter)
4
>>> next(li_iter)
5
>>> next(li_iter)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""

list_0 = [10, 2, 36, 4, 5]

# for 循环遍历迭代器，相当于将迭代器中的元素逐个赋值
iter_list_0 = iter(list_0)
for element in iter_list_0:
    print(element)

iter_list_0 = iter(list_0)
try:
    while True:
        print(next(iter_list_0))
except:
    pass
