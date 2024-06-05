import matplotlib.pyplot as plt
import numpy as np
import time
import math
import random


# fig, ax = plt.subplots()
# x = np.linspace(-2*math.pi,2*math.pi, 11)
# y = np.cos(x) + 1.5 * np.sin(x)

# ax.plot(x,y, label= "The trigoneometric function")
# ax.legend()
# plt.show()

## Second assignment 
x = np.linspace(100, 2000, 20)

sInterval = []
sLogInterval = []
#For the first 
for n in x:
    A = [[random.random() for i in range(int(n))] for j in range(int(n))]
    B = [[random.random() for i in range(int(n))] for j in range(int(n))]

    s0 = time.perf_counter()
    C = [[A[i][j] + B[i][j] for j in range(int(n))] for i in range(int(n))]
    s1 = time.perf_counter()
    theSTimeDifference = s1-s0
    sLogInterval.append(math.log10(theSTimeDifference)) 
    sInterval.append(theSTimeDifference)

tInterval = []
tLogInterval = []
for n in x:
    A = [[random.random() for i in range(int(n))] for j in range(int(n))]
    B = [[random.random() for i in range(int(n))] for j in range(int(n))]

    # Create ndarrays representing A and B:
    An = np.array(A)
    Bn = np.array(B)
    # Add them using numpy, and measure the time:
    t0 = time.perf_counter()
    Cn = An + Bn
    t1 = time.perf_counter()
    theTTimeDifference = t1-t0
    tLogInterval.append(math.log10(theTTimeDifference))
    tInterval.append(theTTimeDifference)

fig, ax = plt.subplots(2,1)
ax[0].plot(x, sInterval, label="Time graph without numpy")
ax[0].legend()
ax[0].plot(x, tInterval, label="Time graph with numpy")
ax[0].legend()
ax[1].plot(x, sLogInterval, label="The Logrithimic Time graph without numpy")
ax[1].legend()
ax[1].plot(x, tLogInterval, label="The Logrithimic Time graph with numpy")
ax[1].legend()
plt.show()

