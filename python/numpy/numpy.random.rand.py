# coding=utf-8
# rand(...) method of mtrand.RandomState instance
#     rand(d0, d1, ..., dn)
#
#     Random values in a given shape.
#
#     Create an array of the given shape and populate it with
#     random samples from a uniform distribution over ``[0, 1)``.
#
#     Parameters
#     ----------
#     d0, d1, ..., dn : int, optional
#         The dimensions of the returned array, should all be positive.
#         If no argument is given a single Python float is returned.
#
#     Returns
#     -------
#     out : ndarray, shape ``(d0, d1, ..., dn)``
#         Random values.
import numpy
a = numpy.random.rand(2, 3, 5)
print(a)
