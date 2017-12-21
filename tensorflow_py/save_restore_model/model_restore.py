import tensorflow as tf

# Let's laod a previous meta graph in the current graph in use: usually the default graph
# This actions returns a Saver
saver = tf.train.import_meta_graph('model/model.ckpt.meta')

# We can now access the default graph where all our metadata has been loaded
graph = tf.get_default_graph()

# Finally we can retrieve tensors, operations, etc.
global_step_tensor = graph.get_tensor_by_name('v1:0')
#train_op = graph.get_operation_by_name('v2:0')
hyperparameters = tf.get_collection('hyperparameters')

with tf.Session() as sess:
    # To initialize values with saved data
    saver.restore(sess, 'model/data.data-00000-of-00001')
    print(sess.run(global_step_tensor)) # returns 1000