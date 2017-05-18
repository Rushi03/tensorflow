import tensorflow as tf

# Addition
x = tf.add(4, 5)

# Division
a = tf.divide(tf.constant(6), tf.constant(3))

# Multiplication
b = tf.multiply(5, 5)

# Subtraction
y = tf.subtract(7, 3)

# n = (8 / 4) * 3 + 9 - 5
f = tf.constant(8)
g = tf.constant(4)
h = tf.constant(3)
i = tf.constant(9)
j = tf.constant(5)

n = tf.subtract(tf.add(tf.multiply(tf.divide(f, g), tf.cast(h, tf.float64)),
                tf.cast(i, tf.float64)), tf.cast(j, tf.float64))

with tf.Session() as sess:
    output = sess.run(n)
    print(output)
