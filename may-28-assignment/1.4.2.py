x = int((5**25)/5)
y = (5**25)//5
print(x, type(x))
print(y, type(y))

# The program is expected to give the same output, but notice that for x the value is converted to integer object which changes a whole lot
# This is because of the integer addition after crossing the 16 bit mark. 
# For Y, we are just getting the values of quotent of the expression which is nice enough and more accurate. 