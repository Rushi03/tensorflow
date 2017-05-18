import tensorflow as tf

hello_world = tf.constant("Hello, World!")

with tf.Session() as sess:
    output = sess.run(hello_world)
    print(output)
