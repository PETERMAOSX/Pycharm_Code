import tensorflow as tf
x = tf.constant([3.0,2.0])
w = tf.constant([[1.0],[9.0]])
y = tf.matmul(x,w)
print(y)
