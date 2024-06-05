import numpy as np
x1 = [1, 2, -1]
x2 = [2, 2, 1]
x3 = [1, -1, 1]

A = np.array([x1, x2, x3]).transpose()
b = np.array([1,2,1])

x = np.linalg.solve(A,b)
print(A@x)


print("Please enter the a postive integer: ")
N = int(input())

allDet = []
for i in range(1, 10001):
    m = np.random.rand(N,N)
    m_squared = np.matmul(m,m)
    det = float(np.linalg.det(m_squared))
    allDet.append(det)

sumOfDet = 0
for i in allDet:
    sumOfDet = sumOfDet + i

averageDet = sumOfDet/len(allDet)
print(averageDet)

# Now if A is an N * N matric whose entries are chosen uniformly at random from [0,1), the determinant is not 
# necessarily zero. Hence Now, for Alice, she is partially right but when a determinant is zero is not only when
# all the entries are zero. With the program in i the average of a determinant of these N x N matrix is not necessarily
# zero as N grows large, inface, as N grows large we assume to have positive determinant

