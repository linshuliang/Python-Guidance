# coding=utf-8
"""
Help on function full in module numpy:

full(shape, fill_value, dtype=None, order='C')
    Return a new array of given shape and type, filled with `fill_value`.

    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    fill_value : scalar
        Fill value.
    dtype : data-type, optional
        The desired data-type for the array  The default, `None`, means
         `np.array(fill_value).dtype`.
    order : {'C', 'F'}, optional
        Whether to store multidimensional data in C- or Fortran-contiguous
        (row- or column-wise) order in memory.

    Returns
    -------
    out : ndarray
        Array of `fill_value` with the given shape, dtype, and order.

    See Also
    --------
    full_like : Return a new array with shape of input filled with value.
    empty : Return a new uninitialized array.
    ones : Return a new array setting values to one.
    zeros : Return a new array setting values to zero.

    Examples
    --------
    >>> np.full((2, 2), np.inf)
    array([[ inf,  inf],
           [ inf,  inf]])
    >>> np.full((2, 2), 10)
    array([[10, 10],
           [10, 10]])
"""
import numpy as np

x = np.full((1, 7), 10)
print(x)

y = np.full((2, 3), 2.5)
print(y)
