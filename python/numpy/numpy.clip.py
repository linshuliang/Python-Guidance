# coding=utf-8
# Syntax:
#     clip(a, a_min, a_max, out=None, **kwargs)
#
# Usage:
#     Clip (limit) the values in an array.
#
#     Given an interval, values outside the interval are clipped to
#     the interval edges.  For example, if an interval of ``[0, 1]``
#     is specified, values smaller than 0 become 0, and values larger
#     than 1 become 1.
#
#     Parameters
#     ----------
#     a : array_like
#         Array containing elements to clip.
#     a_min : scalar or array_like or None
#         Minimum value. If None, clipping is not performed on lower
#         interval edge. Not more than one of `a_min` and `a_max` may be
#         None.
#     a_max : scalar or array_like or None
#         Maximum value. If None, clipping is not performed on upper
#         interval edge. Not more than one of `a_min` and `a_max` may be
#         None. If `a_min` or `a_max` are array_like, then the three
#         arrays will be broadcasted to match their shapes.
#     out : ndarray, optional
#         The results will be placed in this array. It may be the input
#         array for in-place clipping.  `out` must be of the right shape
#         to hold the output.  Its type is preserved.
#     **kwargs
#         For other keyword-only arguments, see the
#         :ref:`ufunc docs <ufuncs.kwargs>`.
#
#         .. versionadded:: 1.17.0
#
#     Returns
#     -------
#     clipped_array : ndarray
#         An array with the elements of `a`, but where values
#         < `a_min` are replaced with `a_min`, and those > `a_max`
#         with `a_max`.
import numpy as np

a = np.arange(10)

b = np.clip(a, 1, 8)
print('b = {}'.format(b))

c = np.clip(a, 3, 6, out=b)
print('b = {}'.format(b))
print('c = {}'.format(c))

d = np.clip(a, [3, 4, 1, 1, 1, 4, 4, 4, 4, 4], 8)
print('d = {}'.format(d))

# b = [1 1 2 3 4 5 6 7 8 8]
# b = [3 3 3 3 4 5 6 6 6 6]
# c = [3 3 3 3 4 5 6 6 6 6]
# d = [3 4 2 3 4 5 6 7 8 8]
