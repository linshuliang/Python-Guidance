# coding=utf-8
# The tf.data.Dataset API is used to build a pipeline for feeding data to your model.
import os
import tensorflow as tf

ds_tensors = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5, 6])

# Create a CSV file
filename = "temp.csv"
os.system("touch " + filename)

with open(filename, 'w') as f:
    f.write("Line 1\n")
    f.write("Line_2\n")
    f.write("Line_3\n")

ds_file = tf.data.TextLineDataset(filename)

# Use the transformations functions like `map`, `batch` and `shuffle` to
# apply transformations to dataset records.
ds_tensors = ds_tensors.map(tf.square).shuffle(2).batch(2)
ds_file = ds_file.batch(2)

# Iterate
# tf.data.Dataset objects support iteration to loop over records.
print("\nElement of ds_tensors:")
for x in ds_tensors:
    print(x)

print("\nElement in ds_file:")
for x in ds_file:
    print(x)
