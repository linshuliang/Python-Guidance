# coding=utf-8
"""
def numpy.sort(a, axis=-1, kind=None, order=None)
    Return a sorted copy of an array.

    Parameters
    ----------
    a : array_like
        Array to be sorted.
    axis : int or None, optional
        Axis along which to sort. If None, the array is flattened before
        sorting. The default is -1, which sorts along the last axis.
    kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, optional
        Sorting algorithm. The default is 'quicksort'. Note that both 'stable'
        and 'mergesort' use timsort or radix sort under the covers and, in general,
        the actual implementation will vary with data type. The 'mergesort' option
        is retained for backwards compatibility.

        .. versionchanged:: 1.15.0.
           The 'stable' option was added.

    order : str or list of str, optional
        When `a` is an array with fields defined, this argument specifies
        which fields to compare first, second, etc.  A single field can
        be specified as a string, and not all fields need be specified,
        but unspecified fields will still be used, in the order in which
        they come up in the dtype, to break ties.

    Returns
    -------
    sorted_array : ndarray
        Array of the same type and shape as `a`.

"""
import numpy as np

a = np.array([[[1, 4], [3, 1]], [[2, 6], [1, 2]]])
print('\na = \n{}'.format(a))

# sort along the last array
print('\nnp.sort(a) = \n{}'.format(
    np.sort(a)))  # The default value of axis is -1

# sort along axis=0
print('\nnp.sort(a, axis=0) = \n{}'.format(np.sort(a, axis=0)))

# sort along axis=1
print('\nnp.sort(a, axis=1) = \n{}'.format(np.sort(a, axis=1)))

# if axis=None, flatten before sort
print('\nnp.sort(a, axis=None) = \n{}'.format(np.sort(a, axis=None)))

print('#' * 100)

dtype = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38), ('Galahad', 1.7, 38)]
arr = np.array(values, dtype=dtype)

print('\narr = \n{}'.format(arr))

# Use the `order` keyword to specify a field to use when sorting a structured array:
print("\nnp.sort(arr, order='height') = \n{}".format(
    np.sort(arr, order='height')))
