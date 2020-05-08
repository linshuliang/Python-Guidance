# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
from tensorflow import keras

# Dataset
mnist = tf.keras.datasets.mnist
mnist_train, mnist_test = mnist.load_data()

strategy = tf.distribute.MirroredStrategy()
print("Number of devices: {}".format(strategy.num_replicas_in_sync))

num_train_examples = mnist_train[0].shape[0]
num_test_examples = mnist_test[0].shape[0]

BUFFER_SIZE = 10000

# 在训练具有多个 GPU 的模型时，可以通过增加批量大小（batch size）来有效地使用额外的计算能力
# 通常来说，使用适合 GPU 内存的最大批量大小（batch size），并相应地调整学习速率。
BATCH_SIZE_PER_REPLICA = 64
BATCH_SIZE = BATCH_SIZE_PER_REPLICA * strategy.num_replicas_in_sync


def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255
    return image, label
