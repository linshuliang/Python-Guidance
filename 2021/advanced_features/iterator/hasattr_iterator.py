_tuple = (1, 2, 3)
print(hasattr(_tuple, '__iter__'))  # True
print(hasattr(_tuple, '__next__'))  # False

_list = [1, 2, 3]
print(hasattr(_list, '__iter__'))  # True
print(hasattr(_list, '__next__'))  # False

_dict = {'a': 1, 'b': 2}
print(hasattr(_dict, '__iter__'))  # True
print(hasattr(_dict, '__next__'))  # False
