import numpy as np
A = np.array([[2,1],[2.5,1],[3.4,1],[4.1,1],[5.2,1],[6.0,1],
[7.2,1],[7.8,1]])
y = np.array([5.2,5.4,6.9,8.5,9.8,10.7,13.4,13.3])
X = np.linalg.lstsq(A,y,rcond=None)
w,b = X[0]

print(type(X))
print(f"w={w}, b={b}")