# coding=utf-8
"""
def vstack(tup):
    Stack arrays in sequence vertically (row wise).

    np.vstack 函数不会新增维度。
    而 np.stack 函数会新增一个维度。

    This is equivalent to concatenation along the first axis after 1-D arrays
    of shape `(N,)` have been reshaped to `(1,N)`. Rebuilds arrays divided by
    `vsplit`.

    This function makes most sense for arrays with up to 3 dimensions. For
    instance, for pixel-data with a height (first axis), width (second axis),
    and r/g/b channels (third axis). The functions `concatenate`, `stack` and
    `block` provide more general stacking and concatenation operations.

    Parameters
    ----------
    tup : sequence of ndarrays
        The arrays must have the same shape along all but the first axis.
        1-D arrays must have the same length.

    Returns
    -------
    stacked : ndarray
        The array formed by stacking the given arrays, will be at least 2-D.

    Examples
    --------
    >>> a = np.array([1, 2, 3])
    >>> b = np.array([2, 3, 4])
    >>> np.vstack((a,b))
    array([[1, 2, 3],
           [2, 3, 4]])

    >>> a = np.array([[1], [2], [3]])
    >>> b = np.array([[2], [3], [4]])
    >>> np.vstack((a,b))
    array([[1],
           [2],
           [3],
           [2],
           [3],
           [4]])
"""
import numpy as np

a = np.floor(10 * np.random.rand(2, 3))
b = np.floor(10 * np.random.rand(2, 3))
ab = np.vstack((a, b))
print('a = \n{}'.format(a))
print('\nb = \n{}'.format(b))
print('\nnp.vstack(a, b) = \n{}'.format(ab))

ab_1 = np.stack((a, b), axis=0)
print('\nnp.stack(a, b, axis=0) = \n{}'.format(ab_1))
