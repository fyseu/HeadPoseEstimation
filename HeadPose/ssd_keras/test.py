import tensorflow as tf
import numpy as np

y_true = np.array([[[1,0.5, 0.8], [1,0.1, 0.7], [1,0.1, 0.1]], [[1,0.2, 0.1], [1,0.4, 0.1], [1,0.8, 0.9]]])
y_pred = np.array([[[1,0.4, 0.4], [1,0.1, 0.2], [1,0.1, 0.1]], [[1,0.2, 0.6], [1,0.4, 0.1], [1,0.8, 0.4]]])
print(y_true.shape)
print(y_true)
positives = y_true[:,:,0]
print(positives.shape)
print(positives)
print(y_true[:,:,1:3] - y_pred[:,:,1:3])
angle_loss = tf.to_float(tf.reduce_sum(5 * (y_true[:,:,1:3] - y_pred[:,:,1:3]) ** 2, axis=-1))
angle_pos_loss = tf.reduce_sum(angle_loss * positives, axis=-1)
with tf.Session() as sess:
    print(sess.run(angle_loss))
    print(sess.run(angle_pos_loss))
    # print(positives.eval())

