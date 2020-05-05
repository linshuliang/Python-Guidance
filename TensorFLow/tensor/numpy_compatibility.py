# coding=utf-8
import numpy as np
import tensorflow as tf

arr = np.ones([3, 3])

print("\nTensorFlow operations convert numpy arrays to Tensors automatically")
tensor = tf.multiply(arr, 42)
print(tensor)

print("\nNumPy operations convert Tensors to numpy arrays automatically")
arr_1 = np.add(tensor, 2)
print(arr_1)

print("\nThe .numpy() method explicitly converts a Tensor to a numpy array.")
print(tensor.numpy())
