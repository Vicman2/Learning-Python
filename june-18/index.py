import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('calhousing.csv')
X = df.to_numpy()
x_train = X[:16512,:8].copy()
y_train = X[:16512,8].copy()
x_test = X[16512:,:8].copy()
y_test = X[16512:,8].copy()
# cahouse = tf.keras.datasets.california_housing
# (x_train, y_train),(x_test,y_test) = cahouse.load_data()
num_features = x_train.shape[1]

# Scale target values to a reasonable range.
y_test /= 100000
y_train /= 100000
############ The model ###############
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Input(shape=(num_features,)))
# Normalization layer to scale input features to mean 0, std 1.
# L = tf.keras.layers.Normalization(axis=1)
# L.adapt(x_train) # Use the training set to determine scaling factors

# model.add(L)
model.add(tf.keras.layers.Dense(32))
model.add(tf.keras.layers.LeakyReLU(negative_slope=0.1))
model.add(tf.keras.layers.Dense(16))
model.add(tf.keras.layers.LeakyReLU(negative_slope=0.1))
model.add(tf.keras.layers.Dropout(0.1))
model.add(tf.keras.layers.Dense(8))
model.add(tf.keras.layers.LeakyReLU(negative_slope=0.1))
model.add(tf.keras.layers.Dense(1, activation="softplus"))
model.compile(optimizer="adam", loss="mse")

callback = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=50,
restore_best_weights=True)
model.fit(x_train, y_train, epochs=100, validation_split=0.1,
callbacks=[callback], verbose=2)
history = model.history.history
# Evaluate on the test set.
h = model.evaluate(x_test, y_test, verbose=2)

###########################################################
# Plot the loss on train & validate sets by epoch:
num_epochs = len(history["loss"])
fig,ax = plt.subplots(1,2)
ep = range(1,num_epochs+1)
ax[0].plot(ep, history["loss"], color="black")
ax[0].plot(ep, history["val_loss"], color="blue")
ax[0].set(xlim=(1,num_epochs+1))
ax[0].set(title="Loss by epoch", xlabel="epoch", ylabel="MSE loss")
ax[0].legend(["train", "validation"], loc="upper left")
# Now plot the predictions vs true values on the test set:
y0,y1 = y_test.min(), y_test.max()
ax[1].plot([y0,y1],[y0,y1], color="red")
y_pred = model(x_test)
ax[1].scatter(y_test, y_pred,s=1)
ax[1].set(title=f"Test set (in $100k) (loss={h:0.2f})",
xlabel="actual", ylabel="predicted")
plt.show()


#12.3.1
# i. There is little or no loss in the validation but 
# there is a drastic decrease in loss from 0-2 epoch, then there 
# there is a constant loss around zero when the epoch ranges from 2.0-4.5

# ii. Increasing the patience argument gives a good and correlative loss with the train and validation data
# Also the loss with epoch decreased to 1 from 0-20 epoch and constantly tending to 
# zero from 21-80 epoch, Also there is a positive correlation in the actual vs predicted data
#Conclusion, we can get our former result by increasing the patience level
# and removing the normalization layer

# 12.3.3
# Of course Bob's model should have a greater accuracy because all the models he generated
# are trained and validated against the test data while Alice had only one of here best model 
# applied against the test data
