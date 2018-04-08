# Este programa sirve para evidenciar si TensorFlow fue instalado correctamente
#Es te programa fue tomado de: https://www.tensorflow.org/install/install_windows

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
