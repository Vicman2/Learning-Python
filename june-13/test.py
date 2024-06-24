import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
# Load the MNIST digits test set.
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()


model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape = (28, 28)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation='leaky_relu'))
model.add(tf.keras.layers.Dense(10, activation = 'leaky_relu'))
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(loss=loss_fn, metrics=['accuracy'])
# model.fit(x_train, y_train, epochs=5, verbose=2)

print("\nEvaluating on test set...")
# Evaluate the accuracy of the model on the test set:
model.evaluate(x_test, y_test, verbose=2)

# Evaluate the model on the first 25 inputs, so we can plot the results.
results = model(x_test[:25])
# Display the first 25 images and their predicted values.
fig,ax = plt.subplots(5,5)
fig.subplots_adjust(hspace=0.5)
print(results)
for k in range(25):
    r = k//5
    c = k%5
    maxv = -np.inf
    lu = np.argsort(results[k])
    print(lu, "Lululukulu")

    if lu[9] == y_test[k]:
            col = "green"
    else:
        col = "red"
    ax[r,c].imshow(x_test[k],cmap="gray", vmin=0.0, vmax=1.0)
    ax[r,c].set_title(f"Pd: {lu[9]} nx: {lu[8]}",color=col)
    ax[r,c].tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
    # Print results to the terminal as well:
    print(f"Test set item {k}: Actual={y_test[k]}, Pred={lu[9]}")
    res = np.round(results[k],2)
    print(f" NN output: {res}\n")
plt.show()