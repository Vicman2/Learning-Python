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
model.fit(x_train, y_train, epochs=5, verbose=2)
print(model.history.history['accuracy'][4], "Accuracy")
theMainAccuracy = model.history.history['accuracy'][4]

noOfBetterAccuracy = 0
for i in range(50):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape = (28, 28)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation='leaky_relu'))
    model.add(tf.keras.layers.Dense(10, activation = 'leaky_relu'))
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(loss=loss_fn, metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=5, verbose=2)
    if model.history.history['accuracy'][2] >= theMainAccuracy:
        print(model.history.history['accuracy'][4], "Greater")
        noOfBetterAccuracy = noOfBetterAccuracy + 1
    else: 
        print(model.history.history['accuracy'][4], "Not greater")

print(noOfBetterAccuracy)
# print("\nEvaluating on test set...")
# # Evaluate the accuracy of the model on the test set:
# model.evaluate(x_test, y_test, verbose=2)

# # Evaluate the model on the first 25 inputs, so we can plot the results.
# results = model(x_test[:25])
# # Display the first 25 images and their predicted values.
# fig,ax = plt.subplots(5,5)
# fig.subplots_adjust(hspace=0.5)
# for k in range(25):
#     r = k//5
#     c = k%5
#     maxv = -np.inf
#     for j in range(10):
#         if results[k][j] > maxv:
#             maxv = results[k][j]
#             pred = j
#     if pred == y_test[k]:
#             print("---------",y_test, "--------")
#             col = "green"
#     else:
#         col = "red"
#     ax[r,c].imshow(x_test[k],cmap="gray", vmin=0.0, vmax=1.0)
#     ax[r,c].set_title(f"Pred: {pred}",color=col)
#     ax[r,c].tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
#     # Print results to the terminal as well:
#     print(f"Test set item {k}: Actual={y_test[k]}, Pred={pred}")
#     res = np.round(results[k],2)
#     print(f" NN output: {res}\n")

# deResults = model(x_test[:1000])
# success = 0
# for k in range(1000):
#     maxv = -np.inf
#     for j in range(10):
#         if deResults[k][j] > maxv:
#             maxv = deResults[k][j]
#             pred = j
#     if pred == y_test[k]:
#             success = success + 1
# print('Success',success, 145/1000)

# noOf145 = 0
# for i in range(200):
#     model = tf.keras.Sequential()
#     model.add(tf.keras.layers.Input(shape = (28, 28)))
#     model.add(tf.keras.layers.Flatten())
#     model.add(tf.keras.layers.Dense(128, activation='leaky_relu'))
#     model.add(tf.keras.layers.Dense(10, activation = 'leaky_relu'))
#     loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
#     model.compile(loss=loss_fn, metrics=['accuracy'])
#     # model.fit(x_train, y_train, epochs=5, verbose=2)

#     print("\nEvaluating on test set...")
#     # Evaluate the accuracy of the model on the test set:
#     model.evaluate(x_test, y_test, verbose=2)

#     # Evaluate the model on the first 25 inputs, so we can plot the results.
#     results = model(x_test[:25])
#     # Display the first 25 images and their predicted values.
#     fig,ax = plt.subplots(5,5)
#     fig.subplots_adjust(hspace=0.5)
#     for k in range(25):
#         r = k//5
#         c = k%5
#         maxv = -np.inf
#         for j in range(10):
#             if results[k][j] > maxv:
#                 maxv = results[k][j]
#                 pred = j
#         if pred == y_test[k]:
#                 print("---------",y_test, "--------")
#                 col = "green"
#         else:
#             col = "red"
#         ax[r,c].imshow(x_test[k],cmap="gray", vmin=0.0, vmax=1.0)
#         ax[r,c].set_title(f"Pred: {pred}",color=col)
#         ax[r,c].tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
#         # Print results to the terminal as well:
#         print(f"Test set item {k}: Actual={y_test[k]}, Pred={pred}")
#         res = np.round(results[k],2)
#         print(f" NN output: {res}\n")

#     deResults = model(x_test[:1000])
#     success = 0
#     for k in range(1000):
#         maxv = -np.inf
#         for j in range(10):
#             if deResults[k][j] > maxv:
#                 maxv = deResults[k][j]
#                 pred = j
#         if pred == y_test[k]:
#                 success = success + 1
#     print('Success',success, 145/1000)

#     if success == 145:
#          noOf145 = noOf145 + 1 
# print(noOf145)
         
     

    
     
# plt.show()


#11.3.1
# WE first use the start we an input of 2dimension 
#The input is a 2-dimensional array (28, 28)
#For the first hidden layer it is not 
# [28 * 28 + 1(the constant) ] * 128 = 100480 
# The second hidden layer
# (128 + 1) * 10  = 1290 = 1290
#Hence trainable parameters = 100480 + 1290 = 101770

#11.3.2
#I will expect the accuracy level to decrease and it actually decreased. 
# On confirmation, the accuracy decreased from 0.9528 to 0.8892
# The loss increased from 0.2803 to 1.0959

#11.34

# The probability of success for uniformly random ways is 145/1000, i.e 0.145
# The probabilility that model making such random prediction would achieve an accuracy rate 
# at or above observed level is 0.001
