import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
# Load the MNIST digits test set.
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Scale entries from int’s in [0,255] to floats in [0,1].
x_train, x_test = x_train / 255.0, x_test / 255.0
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Input(shape=(28,28,1)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128))
model.add(tf.keras.layers.LeakyReLU(negative_slope=0.1))
model.add(tf.keras.layers.Dense(32))
model.add(tf.keras.layers.LeakyReLU(negative_slope=0.1))
model.add(tf.keras.layers.Dense(10, activation="softplus"))
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer="adam", loss=loss_fn, metrics=["accuracy"])

max_epochs = 50
# Note: validation_split=0.2 will reserve the LAST 20 percent
# of the samples for validation, so it’s important that
# x_train,y_train already be in a shuffled order!
vs=0.2
val_size = int(vs*x_train.shape[0])
model.fit(x_train, y_train, epochs=max_epochs, validation_split=vs, verbose=2)
history = model.history.history
print(model.summary(), "++++++++++++++++++++++++++++")


#######################################
# Roughly a 95% confidence interval estimate for true accuracy
# based on the validation results per epoch.
alpha = stats.norm.ppf(0.95)
dev = (0.1*0.9/val_size)**(1/2)
fig,ax = plt.subplots(1,2)
fig.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.1)
# Plot the accuracy on train & validate sets by epoch:
x = [j for j in range(1,max_epochs+1)]
ax[0].plot(x, history["accuracy"], color="black")
ax[0].plot(x, history["val_accuracy"], color="blue")
v0 = [a-dev for a in history["val_accuracy"]]
v1 = [a+dev for a in history["val_accuracy"]]
ax[0].fill_between(x, v0, v1, color="blue", alpha=0.1)
ax[0].axis([1,max_epochs,0.95,1.0])
ax[0].set(title="Accuracy", xlabel="epoch", ylabel="accuracy")
ax[0].legend(["train", "test", "95% CI estimate"], loc="upper left")
# Similarly with the loss:
ax[1].plot(x, history["loss"])
ax[1].plot(x, history["val_loss"])
ax[1].axis([1,max_epochs, 0, 0.2])
ax[1].set(title="Loss", xlabel="epoch", ylabel="loss")

ax[1].legend(["train", "test"], loc="upper left")
plt.show()