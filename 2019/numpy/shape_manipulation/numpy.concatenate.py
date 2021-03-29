# coding=utf-8
"""
concatenate(...)
    concatenate((a1, a2, ...), axis=0, out=None)

    Join a sequence of arrays along an existing axis.

    Parameters
    ----------
    a1, a2, ... : sequence of array_like
        The arrays must have the same shape, except in the dimension
        corresponding to `axis` (the first, by default).
    axis : int, optional
        The axis along which the arrays will be joined.  If axis is None,
        arrays are flattened before use.  Default is 0.
    out : ndarray, optional
        If provided, the destination to place the result. The shape must be
        correct, matching that of what concatenate would have returned if no
        out argument were specified.

    Returns
    -------
    res : ndarray
        The concatenated array.

    Examples
    --------
    >>> a = np.array([[1, 2], [3, 4]])
    >>> b = np.array([[5, 6]])
    >>> np.concatenate((a, b), axis=0)
    array([[1, 2],
           [3, 4],
           [5, 6]])
    >>> np.concatenate((a, b.T), axis=1)
    array([[1, 2, 5],
           [3, 4, 6]])
    >>> np.concatenate((a, b), axis=None)
    array([1, 2, 3, 4, 5, 6])
"""
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

ab = np.concatenate((a, b))
print('np.concatenate((a, b)) = \n{}'.format(np.concatenate((a, b))))

ab_vstack = np.vstack((a, b))
print('np.vstack((a,b)) = \n{}'.format(np.vstack((a, b))))
