# coding=utf-8
# expand_dims(a, axis)
#    Expand the shape of an array.
#
#    Insert a new axis that will appear at the `axis` position in the expanded
#    array shape.
#
#    Parameters
#    ----------
#    a : array_like
#        Input array.
#    axis : int or tuple of ints
#        Position in the expanded axes where the new axis (or axes) is placed.
#
#        .. deprecated:: 1.13.0
#            Passing an axis where ``axis > a.ndim`` will be treated as
#            ``axis == a.ndim``, and passing ``axis < -a.ndim - 1`` will
#            be treated as ``axis == 0``. This behavior is deprecated.
#
#        .. versionchanged:: 1.18.0
#            A tuple of axes is now supported.  Out of range axes as
#            described above are now forbidden and raise an `AxisError`.
#
#    Returns
#    -------
#    result : ndarray
#        View of `a` with the number of dimensions increased.
#
#    See Also
#    --------
#    squeeze : The inverse operation, removing singleton dimensions
#    reshape : Insert, remove, and combine dimensions, and resize existing ones
#    doc.indexing, atleast_1d, atleast_2d, atleast_3d
#
#    Examples
#    --------
#    >>> x = np.array([1, 2])
#    >>> x.shape
#    (2,)
#
#    The following is equivalent to ``x[np.newaxis, :]`` or ``x[np.newaxis]``:
#
#    >>> y = np.expand_dims(x, axis=0)
#    >>> y
#    array([[1, 2]])
#    >>> y.shape
#    (1, 2)
#
#    The following is equivalent to ``x[:, np.newaxis]``:
#
#    >>> y = np.expand_dims(x, axis=1)
#    >>> y
#    array([[1],
#           [2]])
#    >>> y.shape
#    (2, 1)
#
#    ``axis`` may also be a tuple:
#
#    >>> y = np.expand_dims(x, axis=(0, 1))
#    >>> y
#    array([[[1, 2]]])
#
#    >>> y = np.expand_dims(x, axis=(2, 0))
#    >>> y
#    array([[[1],
#            [2]]])
import numpy as np

a = np.zeros((2, 3))
b = np.expand_dims(a, axis=-1)
print(b.shape)  #  (2, 3, 1)
