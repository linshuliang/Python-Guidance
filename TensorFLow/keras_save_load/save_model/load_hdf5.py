# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import os

import tensorflow as tf
from tensorflow import keras

# Dataset
(train_images,
 train_labels), (test_images,
                 test_labels) = tf.keras.datasets.mnist.load_data()
test_labels = test_labels[:1000]
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

new_model = keras.models.load_model('my_model.h5')
new_model.summary()

loss, acc = new_model.evaluate(test_images, test_labels, verbose=2)
print("Restored model, accuracy: {:5.2f}%".format(100 * acc))
