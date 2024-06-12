import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('./lubhouses.csv')
M = df.to_numpy()
print(M)

# Separate x and y values:
p = M[:,-1]
A = M[:,:-1]
newA = np.insert(A, 0, 1, axis= 1)


# Solve it.
soln = np.linalg.lstsq(newA,p,rcond=None)

w = soln[0]
c0, c1, c2, c3, c4, c5 =w[0], w[1], w[2], w[3], w[4], w[5]
print(c0, c1, c2, c3, c4, c5)
print("The introduction of c0 is what altered the result of the values")

print("The results are junks because the data set is too small")
print("Random data are prone to error and hence can't be used in real-life")

X = np.linspace(0,100,100)
Y = c0 + c1*X + c2*X + c3*X + c4*X + c5*X
fig,ax = plt.subplots()
ax.plot(X,Y)
plt.show()
