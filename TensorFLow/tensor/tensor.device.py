# coding=utf-8
import time
import tensorflow as tf


def time_matmul(x):
    start = time.time()
    for loop in range(10):
        y = tf.matmul(x, x)

    result = time.time() - start
    print("10 loops: {:0.2f}ms".format(1000 * result))


# Force execution on CPU
print('On CPU')
with tf.device("CPU:0"):
    x = tf.random.uniform([1000, 1000])
    assert x.device.endswith("CPU:0")
    time_matmul(x)

# Force execution on GPU
print("On GPU")
if tf.config.experimental.list_physical_devices("GPU"):
    with tf.device("GPU:0"):
        x = tf.random.uniform([1000, 1000])
        assert x.device.endswith("GPU:0")
        time_matmul(x)
