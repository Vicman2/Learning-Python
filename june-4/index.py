import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots(2,2)
print(ax, fig)
# ax.plot([0,10], [1.1, 4.7])
# plt.show()

# Plot the functuin y = x *^3 -2x + 1
# From -10 to 10

x = np.linspace(-2, 2, 200)
y = x **3 -2*x  + 1


ax[0,0].plot(x,y)

x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 2, 1000)
ax[0,1].scatter(x,y)
plt.show()
print(x)
print(y)