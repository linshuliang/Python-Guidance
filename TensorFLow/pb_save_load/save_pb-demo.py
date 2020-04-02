# coding=utf-8
"""
Help on function convert_variables_to_constants in module tensorflow.python.framework.graph_util_impl:

convert_variables_to_constants(sess, input_graph_def, output_node_names, variable_names_whitelist=None, variable_names_blacklist=None)
    Replaces all the variables in a graph with constants of the same values. (deprecated)

    Warning: THIS FUNCTION IS DEPRECATED. It will be removed in a future version.
    Instructions for updating:
    Use `tf.compat.v1.graph_util.convert_variables_to_constants`

    If you have a trained graph containing Variable ops, it can be convenient to
    convert them all to Const ops holding the same values. This makes it possible
    to describe the network fully with a single GraphDef file, and allows the
    removal of a lot of ops related to loading and saving the variables.

    Args:
      sess: Active TensorFlow session containing the variables.
      input_graph_def: GraphDef object holding the network.
      output_node_names: List of name strings for the result nodes of the graph.
      variable_names_whitelist: The set of variable names to convert (by default,
                                all variables are converted).
      variable_names_blacklist: The set of variable names to omit converting
                                to constants.

    Returns:
      GraphDef containing a simplified version of the original.
"""

import os

import tensorflow as tf
from tensorflow.python.framework import graph_util

with tf.Session(graph=tf.Graph()) as sess:
    x = tf.compat.v1.placeholder(tf.int32, name='x')
    y = tf.compat.v1.placeholder(tf.int32, name='y')
    b = tf.Variable(1, name='b')

    xy = tf.multiply(x, y)
    add_op = tf.add(xy, b, name='xy_add_b')

    sess.run(tf.compat.v1.global_variables_initializer())

    # convert variables to constants
    constant_graph = graph_util.convert_variables_to_constants(
        sess, sess.graph_def, ['xy_add_b'])

    pb_save_path = os.path.join(os.getcwd(), 'demo_model.pb')
    with tf.io.gfile.GFile(pb_save_path, mode='wb') as f:
        f.write(constant_graph.SerializeToString())
