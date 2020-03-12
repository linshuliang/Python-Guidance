# coding=utf-8
# Join a sequence of arrays along a new axis.
# numpy.stack(arrays, axis=0, out=None)
import numpy as np

arr_list = [np.random.rand(3, 4) for _ in range(10)]

# stack along axis 0
stack_axis_0 = np.stack(arr_list, axis=0)
print(stack_axis_0.shape)

# stack along axis 1
stack_axis_1 = np.stack(arr_list, axis=1)
print(stack_axis_1.shape)

# stack along axis 2
stack_axis_2 = np.stack(arr_list, axis=-1)
print(stack_axis_2.shape)
