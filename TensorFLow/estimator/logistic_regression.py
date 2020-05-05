# coding=utf-8
import os
import sys

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from six.moves import urllib

import tensorflow as tf
import tensorflow.compat.v2.feature_column as fc

# Load dataset.
dftrain = pd.read_csv(
    'https://storage.googleapis.com/tf-datasets/titanic/train.csv')
dfeval = pd.read_csv(
    'https://storage.googleapis.com/tf-datasets/titanic/eval.csv')
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

print(dftrain)

CATEGORICAL_COLUMNS = [
    'sex', 'n_siblings_spouses', 'parch', 'class', 'deck', 'embark_town',
    'alone'
]
NUMERIC_COLUMNS = ['age', 'fare']

# ------  Base Feature Columns -------
feature_columns = list()
for feature_name in CATEGORICAL_COLUMNS:
    vocabulary = dftrain[feature_name].unique()
    feature_columns.append(
        tf.feature_column.categorical_column_with_vocabulary_list(
            feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
    feature_columns.append(
        tf.feature_column.numeric_column(feature_name, dtype=tf.float32))


# The input_function specifies how data is converted to a tf.data.Dataset that feeds the input pipeline in a streaming fashion.
# tf.data.Dataset can take in multiple sources such as a dataframe, a csv-formatted file, and more.
def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True,
                  batch_size=32):
    def input_function():
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
        if shuffle:
            ds = ds.shuffle(1000)
        ds = ds.batch(batch_size).repeat(num_epochs)
        return ds

    return input_function


train_input_fn = make_input_fn(dftrain, y_train)
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)

ds = make_input_fn(dftrain, y_train, batch_size=10)()
"""
for feature_batch, label_batch in ds.take(1):
    print('Some feature keys:', list(feature_batch.keys()))
    print('A batch of class:', feature_batch['class'].numpy())
    print('A batch of Labels:', label_batch.numpy())
"""

#  Training a model is just a single command using the tf.estimator API
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)
linear_est.train(train_input_fn)
result = linear_est.evaluate(eval_input_fn)
print(result)

# -------- Derived Feature Columns --------
age_x_gender = tf.feature_column.crossed_column(['age', 'sex'],
                                                hash_bucket_size=100)
derived_feature_columns = [age_x_gender]
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns +
                                           derived_feature_columns)
linear_est.train(train_input_fn)
result = linear_est.evaluate(eval_input_fn)
print(result)
