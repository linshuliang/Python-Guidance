# coding=utf-8
"""
def numpy.ndarray.view(dtype=None, type=None)

    New view of array with the same data.

    ndarray.view 方法会创建一个新的数组对象，但这个新的数组对象，和原来的数组对象共享相同的数据。

    Parameters
    ----------
    dtype : data-type or ndarray sub-class, optional
        Data-type descriptor of the returned view, e.g., float32 or int16. The
        default, None, results in the view having the same data-type as `a`.
        This argument can also be specified as an ndarray sub-class, which
        then specifies the type of the returned object (this is equivalent to
        setting the ``type`` parameter).
    type : Python type, optional
        Type of the returned view, e.g., ndarray or matrix.  Again, the
        default None results in type preservation.

    Examples
    --------
    >>> x = np.array([(1, 2)], dtype=[('a', np.int8), ('b', np.int8)])

    Viewing array data using a different type and dtype:

    >>> y = x.view(dtype=np.int16)
    >>> y
    array([[513]], dtype=int16)
"""
import numpy as np

a = np.arange(0, 6).reshape((2, 3)).astype(np.int64)
print('\na = \n{}'.format(a))
# [[0 1 2]
#  [3 4 5]]

b = a.view(dtype=np.float32)
print('\nb = \n{}'.format(b))
# [[0.e+00 0.e+00 1.e-45 0.e+00 3.e-45 0.e+00]
#  [4.e-45 0.e+00 6.e-45 0.e+00 7.e-45 0.e+00]]

a[0][0] = 10

print('\na = \n{}'.format(a))
# [[10  1  2]
#  [ 3  4  5]]

print('\nb = \n{}'.format(b))
# [[1.4e-44 0.0e+00 1.4e-45 0.0e+00 2.8e-45 0.0e+00]
#  [4.2e-45 0.0e+00 5.6e-45 0.0e+00 7.0e-45 0.0e+00]]

b[1][0] = 2

print('\na = \n{}'.format(a))
# [[        10          1          2]
#  [1073741824          4          5]]

print('\nb = \n{}'.format(b))
# [[1.4e-44 0.0e+00 1.4e-45 0.0e+00 2.8e-45 0.0e+00]
#  [2.0e+00 0.0e+00 5.6e-45 0.0e+00 7.0e-45 0.0e+00]]
