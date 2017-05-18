import tensorflow as tf

x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    output = sess.run(z, feed_dict = {x: 'Test', y: 3, z: 20.17})
    print(output)
