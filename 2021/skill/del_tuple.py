# coding=utf-8

t1 = (1, '2', "apple", {'a', 'b', 'c'}, [99, 100])

t2 = [t1]

del t1

# print(t1)  # error : t1 is not defined
print(t2)
