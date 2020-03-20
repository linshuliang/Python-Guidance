# coding=utf-8
# help(numpy.sort)
import numpy as np

a = np.array([[[1, 4], [3, 1]], [[2, 6], [1, 2]]])
print(a)
print('#' * 100)

# sort along the last array
print(np.sort(a))
print('#' * 100)

# sort along axis=0
print(np.sort(a, axis=0))
print('#' * 100)

# sort along axis=1
print(np.sort(a, axis=1))
print('#' * 100)

# if axis=None, flatten before sort
print(np.sort(a, axis=None))
print('#' * 100)

dtype = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38), ('Galahad', 1.7, 38)]
arr = np.array(values, dtype=dtype)

print(arr)
print('#' * 100)

# Use the `order` keyword to specify a field to use when sorting a structured array:
print(np.sort(arr, order='height'))
print('#' * 100)
