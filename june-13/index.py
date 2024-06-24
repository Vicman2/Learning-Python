import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np 

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Scale entries from int’s in [0,255] to floats in [0,1].
x_train, x_test = x_train / 255.0, x_test / 255.0
# Reshape: The Conv2D layer expects each input to be a 3-dimensional array,
# but x_train[j] is a 2-dimensional array.
x_train = x_train.reshape(*(x_train.shape),1)
x_test = x_test.reshape(*(x_test.shape),1)
R = tf.keras.layers.LeakyReLU()


model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Input(shape=(28,28,1)))
model.add(tf.keras.layers.Dropout(0.1))
model.add(tf.keras.layers.Conv2D(filters=16, kernel_size=(3,3),
activation=R))
model.add(tf.keras.layers.MaxPooling2D())
model.add(tf.keras.layers.Conv2D(filters=8, kernel_size=(3,3), activation=R))
model.add(tf.keras.layers.MaxPooling2D())
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(10,activation="softplus"))
print()