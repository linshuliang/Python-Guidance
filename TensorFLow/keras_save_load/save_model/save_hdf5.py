# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import os

import tensorflow as tf
from tensorflow import keras

# Dataset
(train_images, train_labels), (_, _) = tf.keras.datasets.mnist.load_data()
train_labels = train_labels[:1000]
train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0


# 定义一个简单的序列模型
def create_model():
    model = tf.keras.models.Sequential([
        keras.layers.Dense(512, activation='relu', input_shape=(784, )),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model


# 创建一个基本的模型实例
model = create_model()

# 使用新的回调训练模型
model.fit(train_images, train_labels, epochs=10)

model.save('my_model.h5')
