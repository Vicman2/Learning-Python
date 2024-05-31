import math
print("=====Assignment======")
print()
print("======3.3.1======")
def f(n):
    if n % 2 == 0:
        return n/2
    else:
        return ((3*n) + 1)/2
    
def F3(n):
    return int(f(n))

print(F3(60))

print()
print("======3.3.2======")

def Fseq(n):
    L = [n]
    while n>=2:
        L.append(f(n))
        n = f(n)
    return L
print(Fseq(30))

print()
print("======3.3.3======")

# According to our computation, the expected length of 

def expectedLengthOfF3(n):
    k = (2 *math.log10(n))/math.log10(4/3)
    return k

print(expectedLengthOfF3(10))

def averageOfSuchN(n):
    L1 = []
    for i in range(1, n+1):
        L1.append(expectedLengthOfF3(i))
    #Computing the average
    print(L1)
    total = 0
    for i in L1:
        total = total + i
    average = total/len(L1)

    return average

print(averageOfSuchN(10000))
