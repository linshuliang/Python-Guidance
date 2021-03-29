# coding=utf-8
"""
Help on function squeeze in module numpy:

squeeze(a, axis=None)
    Remove single-dimensional entries from the shape of an array.
    如果数组 a 中有几个维度的 size 等于1，则 np.squeeze(a) 会删除这几个维度。

    Parameters
    ----------
    a : array_like
        Input data.
    axis : None or int or tuple of ints, optional
        Selects a subset of the single-dimensional entries in the
        shape. If an axis is selected with shape entry greater than
        one, an error is raised.

    Returns
    -------
    squeezed : ndarray
        The input array, but with all or a subset of the
        dimensions of length 1 removed. This is always `a` itself
        or a view into `a`.

    Raises
    ------
    ValueError
        If `axis` is not None, and an axis being squeezed is not of length 1

    See Also
    --------
    expand_dims : The inverse operation, adding singleton dimensions
    reshape : Insert, remove, and combine dimensions, and resize existing ones

    Examples
    --------
    >>> x = np.array([[[0], [1], [2]]])
    >>> x.shape
    (1, 3, 1)
    >>> np.squeeze(x).shape
    (3,)
    >>> np.squeeze(x, axis=0).shape
    (3, 1)
    >>> np.squeeze(x, axis=1).shape
    Traceback (most recent call last):
    ...
    ValueError: cannot select an axis to squeeze out which has size not equal to one
    >>> np.squeeze(x, axis=2).shape
    (1, 3)
"""
import numpy as np
x = np.array([[[0], [1], [2]]])
print(x.shape)  # (1, 3, 1)

x_squeeze = np.squeeze(x)
print(x_squeeze.shape)  # (3,)

x_squeeze_axis_0 = np.squeeze(x, axis=0)
print(x_squeeze_axis_0.shape)  # (3, 1)

x_squeeze_axis_2 = np.squeeze(x, axis=2)
print(x_squeeze_axis_2.shape)  # (1, 3)
