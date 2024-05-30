print("=======Assignement=========")

print()
print("=======2.2.1=========")
print("Please input a postive number for the N-th harmonic number")
N = int(input())

tempSum = 0
for i in range(1, N+1):
    tempSum = (1/i) + tempSum;
print(f"The Nth harmonic number is {tempSum}")

print()
print("=======2.2.3=========")

n =float(1)

while (2**(-n)) != 0.0:
    n = n + 1.0
    print(n)
print(n)

print()
print("=======2.2.4=========")
for n in range(1,1001):
    if (n * (1/n) != 1.0):
        print(f"One of the values is {n}")
#It is not wise to check equality for floating point numbers because of the floating point error
# Just as we have seen in our previous exercicse. 
    

