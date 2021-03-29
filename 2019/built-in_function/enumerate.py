# coding=utf-8
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)
# 组合为一个索引序列，其中每一个元素为：(序列号, 数据对象的元素)
# 一般用在 for 循环当中。
# 语法：
#   enumerate(sequence, [start=0])
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('seasons: {}'.format(seasons))
print('list(enumerate(seasons)):', list(enumerate(seasons)))

for i, element in enumerate(seasons):
    print(i, element)
