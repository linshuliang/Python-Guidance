# coding=utf-8

d = {'a': 1, 'b': 2, 'c': 3}

# 默认情况下，dict 迭代的是键key
for k in d:
    print(k)

# 迭代值value
for v in d.values():
    print(v)

# 迭代键-值对 key-value
for k, v in d.items():
    print(k, v)
