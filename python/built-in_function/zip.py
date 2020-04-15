# coding=utf-8
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象。
# 我们可以使用 list() 转换来输出列表。
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

keys = ['a', 'b', 'c']
values = [1, 2, 3]
zipped = zip(keys, values)
zipped_list = list(zipped)

print('keys: {}'.format(keys))
print('values: {}'.format(values))
print('zip(keys, values): {}'.format(zipped))
print('list(zip(keys, values)): {}'.format(zipped_list))

# 一个星号* 可把 序列/集合 转为位置参数，
# 两个星号** 可把字典转为关键字参数
print(*zipped_list)
