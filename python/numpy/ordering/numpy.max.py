# coding=utf-8
"""
np.max(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
    Return the maximum of an array or maximum along an axis.

    Parameters
    ----------
    a : array_like
        Input data.
    axis : None or int or tuple of ints, optional
        Axis or axes along which to operate.  By default, flattened input is
        used.

        .. versionadded:: 1.7.0

        If this is a tuple of ints, the maximum is selected over multiple axes,
        instead of a single axis or all the axes as before.
    out : ndarray, optional
        Alternative output array in which to place the result.  Must
        be of the same shape and buffer length as the expected output.
        See `ufuncs-output-type` for more details.

    Returns
    -------
    amax : ndarray or scalar
        Maximum of `a`. If `axis` is None, the result is a scalar value.

        if `axis` is a tuple:
            amax.ndim = ``a.ndim - len(axis)``.
        elif `axis` is an integer:
            amax.ndim = ``a.ndim - 1``
"""
import numpy as np

a = np.arange(0, 60).reshape((2, 3, 10))

print('\na = \n{}'.format(a))
print('\nnp.max(a) = {}'.format(np.max(a)))
print('\nnp.max(a, axis=0) = \n{}'.format(np.max(a, axis=0)))
print('\nnp.max(a, axis=(0, 1)) = \n{}'.format(np.max(a, axis=(0, 1))))
print('\nnp.max(a, axis=(0, 2)) = \n{}'.format(np.max(a, axis=(0, 2))))
print('\nnp.max(a, axis=(1, 2)) = \n{}'.format(np.max(a, axis=(1, 2))))
