import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
def f(x, mu, sigma):
    # A sample noisy function to be fitted.
    n = x.shape[0]
    y = x**2 + np.random.normal(mu,sigma,size=(n,1))
    return y
num_samples = 100
inputs = np.random.uniform(-10,10,size=(num_samples,1))
outputs = f(inputs, 0, 0.1)

# Now, pretend that we don’t know the function ’f’; all we know is
# the sample inputs and outputs above. Let’s try to approximate it
# with a neural network. We will use 2 hidden layers having 3 nodes each,
# with a ’softplus’ activation.
model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(1,)))
model.add(tf.keras.layers.Dense(3, activation='softplus'))
model.add(tf.keras.layers.Dense(3, activation='softplus'))
model.add(tf.keras.layers.Dense(1, activation='softplus'))

model.compile(optimizer="adam", loss="mse")

# Fit this model to the data.
H = model.fit(inputs, outputs, epochs=2000, verbose=2)
final_mse = H.history['loss'][-1]

fig,ax = plt.subplots()
ax.scatter(inputs, outputs, label="Data points")
xr = np.linspace(-10,10,100)
yr = model(xr)
ax.plot(xr, yr, label=f"NN model: MSE={final_mse}", color='r')
ax.legend()
plt.show()