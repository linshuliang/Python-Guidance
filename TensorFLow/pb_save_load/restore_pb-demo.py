# coding=utf-8
import tensorflow as tf
from tensorflow.python.framework import graph_util

with tf.Session() as sess:
    tf.compat.v1.global_variables_initializer().run()

    pb_path = 'demo_model.pb'
    with open(pb_path, 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        # Imports the graph from graph_def into the current default Graph.
        _ = tf.graph_util.import_graph_def(graph_def, name="")

    input_x = sess.graph.get_tensor_by_name('x:0')
    input_y = sess.graph.get_tensor_by_name('y:0')
    bias = sess.graph.get_tensor_by_name('b:0')
    output = sess.graph.get_tensor_by_name('xy_add_b:0')
    print(input_x)  # Tensor("x:0", dtype=int32)
    print(input_y)  # Tensor("y:0", dtype=int32)
    print(bias)  # Tensor("b:0", shape=(), dtype=int32)
    print(output)  # Tensor("xy_add_b:0", dtype=int32)

    res = sess.run(output, {input_x: 1, input_y: 2})

    print(res)
