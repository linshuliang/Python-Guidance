# coding=utf-8
# Syntax:
#     dict.update()
# Usage
#     D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
#     If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
#     If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
dict_demo = {'name': 'linda', 'gender': 'female'}

add_dict = {'work': 'Apple', 'site': 'California'}
dict_demo.update(add_dict)
print(dict_demo)
# {'name': 'linda', 'gender': 'female', 'work': 'Apple', 'site': 'California'}

list1 = [(1, 2), (3, 4), (5, 6)]
dict_demo.update(list1)
print(dict_demo)
# {'name': 'linda', 'gender': 'female', 'work': 'Apple', 'site': 'California', 1: 2, 3: 4, 5: 6}
