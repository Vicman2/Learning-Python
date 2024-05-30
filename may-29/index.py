L = [1,2,3,4,5,6,20]
for i in L:
    y = i**2
    print(f"{y}")

for m in range(1,101):
    n = m**2
    print(n)

p = 1

while m**3 - 45*m*2 + m -5 <= 0: 
    m = m + 1
print(f"The least postive integer is: {m}")
y_prev = (m-1)**3 - 45*(m-1)*2 + (m-1) -5

p = 0
for i in range(1,51):
    p = p + i
print(p)