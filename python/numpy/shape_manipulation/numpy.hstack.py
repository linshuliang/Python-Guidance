# coding=utf-8
"""
def hstack(tup):
    Stack arrays in sequence horizontally (column wise).

    将数组沿着方向水平方向来堆叠。

    This is equivalent to concatenation along the second axis, except for 1-D
    arrays where it concatenates along the first axis. Rebuilds arrays divided
    by `hsplit`.

    This function makes most sense for arrays with up to 3 dimensions. For
    instance, for pixel-data with a height (first axis), width (second axis),
    and r/g/b channels (third axis). The functions `concatenate`, `stack` and
    `block` provide more general stacking and concatenation operations.

    Parameters
    ----------
    tup : sequence of ndarrays
        The arrays must have the same shape along all but the second axis,
        except 1-D arrays which can be any length.

    Returns
    -------
    stacked : ndarray
        The array formed by stacking the given arrays.

    See Also
    --------
    stack : Join a sequence of arrays along a new axis.
    vstack : Stack arrays in sequence vertically (row wise).
    dstack : Stack arrays in sequence depth wise (along third axis).
    concatenate : Join a sequence of arrays along an existing axis.
    hsplit : Split array along second axis.
    block : Assemble arrays from blocks.

    Examples
    --------
    >>> a = np.array((1, 2, 3))
    >>> b = np.array((2, 3, 4))

    >>> np.hstack((a,b))
    array([1, 2, 3, 2, 3, 4])

    >>> a = np.array([[1],[2],[3]])
    >>> b = np.array([[2],[3],[4]])

    >>> np.hstack((a,b))
    array([[1, 2],
           [2, 3],
           [3, 4]])
"""
import numpy as np

a = np.floor(10 * np.random.rand(2, 3))
b = np.floor(10 * np.random.rand(2, 3))
ab = np.hstack((a, b))
print('\na = \n{}'.format(a))
print('\nb = \n{}'.format(b))
print('\nnp.hstack(a, b) = \n{}'.format(ab))

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[7, 8], [9, 0], [0, 1]])
res = np.hstack((a, b))
print('\na = \n{}'.format(a))
print('\nb = \n{}'.format(b))
print('\nnp.hstack(a, b) = \n{}'.format(res))
