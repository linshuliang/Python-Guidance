# coding=utf-8
"""
def argmax(a, axis=None, out=None)
    Returns the indices of the maximum values along an axis.

    Parameters
    ----------
    a : array_like
        Input array.
    axis : int, optional
        By default, the index is into the flattened array, otherwise
        along the specified axis.
    out : array, optional
        If provided, the result will be inserted into this array. It should
        be of the appropriate shape and dtype.

    Returns
    -------
    index_array : ndarray of ints
        Array of indices into the array. It has the same shape as `a.shape`
        with the dimension along `axis` removed.

    Examples
    --------
    >>> a = np.arange(6).reshape(2,3) + 10
    >>> a
    array([[10, 11, 12],
           [13, 14, 15]])
    >>> np.argmax(a)
    5
    >>> np.argmax(a, axis=0)
    array([1, 1, 1])
    >>> np.argmax(a, axis=1)
    array([2, 2])

    Indexes of the maximal elements of a N-dimensional array:

    >>> ind = np.unravel_index(np.argmax(a, axis=None), a.shape)
    >>> ind
    (1, 2)
    >>> a[ind]
    15

    >>> b = np.arange(6)
    >>> b[1] = 5
    >>> b
    array([0, 5, 2, 3, 4, 5])
    >>> np.argmax(b)  # Only the first occurrence is returned.
    1

    >>> x = np.array([[4,2,3], [1,0,3]])
    >>> index_array = np.argmax(x, axis=-1)
    >>> # Same as np.max(x, axis=-1, keepdims=True)
    >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1)
    array([[4],
           [3]])
    >>> # Same as np.max(x, axis=-1)
    >>> np.take_along_axis(x, np.expand_dims(index_array, axis=-1), axis=-1).squeeze(axis=-1)
    array([4, 3])
"""
import numpy as np

a = np.arange(6).reshape(2, 3) + 10

print('\na = \n{}'.format(a))
print('\nnp.argmax(a) = {}'.format(np.argmax(a)))
