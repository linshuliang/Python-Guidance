# coding=utf-8
# Python 字典的 items() 函数以列表返回可遍历的(键, 值) 元组数组。
# Args:
#     dict.items()
dict_example = {'Google': 'www.google.com', 'taobao': 'www.taobao.com'}

print(dict_example.items())
# dict_items([('Google', 'www.google.com'), ('taobao', 'www.taobao.com')])

print(type(dict_example.items()))
# <class 'dict_items'>

for element in dict_example.items():
    print(element)
# ('Google', 'www.google.com')
# ('taobao', 'www.taobao.com')

for key, values in dict_example.items():
    print(key, values)
# Google www.google.com
# taobao www.taobao.com
