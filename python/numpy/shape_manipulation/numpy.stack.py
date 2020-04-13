# coding=utf-8
# Syntax:
#     stack(arrays, axis=0, out=None)
# Usage:
#     Join a sequence of arrays along a new axis.
#
#     The ``axis`` parameter specifies the index of the new axis in the
#     dimensions of the result. For example, if ``axis=0`` it will be the first
#     dimension and if ``axis=-1`` it will be the last dimension.
#
#     .. versionadded:: 1.10.0
#
#     Parameters
#     ----------
#     arrays : sequence of array_like
#         Each array must have the same shape.
#
#     axis : int, optional
#         The axis in the result array along which the input arrays are stacked.
#
#     out : ndarray, optional
#         If provided, the destination to place the result. The shape must be
#         correct, matching that of what stack would have returned if no
#         out argument were specified.
#
#     Returns
#     -------
#     stacked : ndarray
#         The stacked array has one more dimension than the input arrays.
#
#    See Also
#    --------
#    concatenate : Join a sequence of arrays along an existing axis.
#    split : Split array into a list of multiple sub-arrays of equal size.
#     block : Assemble arrays from blocks.
import numpy as np

arrays = [np.random.randn(3, 4) for _ in range(10)]

print(np.stack(arrays, axis=0).shape)
# (10, 3, 4)

print(np.stack(arrays, axis=1).shape)
# (3, 10, 4)

print(np.stack(arrays, axis=2).shape)
# (3, 4, 10)

a = np.array([1, 2, 3])
b = np.array([2, 3, 4])

print(np.stack((a, b)))
# [[1, 2, 3],
#  [2, 3, 4]]

print(np.stack((a, b), axis=-1))
# [[1, 2],
#  [2, 3],
#  [3, 4]]
