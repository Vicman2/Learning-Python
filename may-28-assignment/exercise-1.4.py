print("Assignment")

print("==============================")

print("===1.4.1===")

x = 49 * (1/49)

print(x)

# The unexpected result is because python just like every other programming language will first compute the expression 
# in bracket before multiplying it by 49, now python 1/49 cannot be represented precicely by a flotating point number
# Hence, there is an error in precession which we can attribute as a floating point error.

print("===1.4.2===")

p = int((5**25)/5)
q = (5**25)//5
print(p)
print(q)

# The program is expected to give the same output, but notice that for x the value is converted to integer object which changes a whole lot
# This is because of the integer addition after crossing the 16 digit mark. 
# For Y, we are just getting the values of quotent of the expression which is nice enough and more accurate. 
# On increasing the exponent from 25 to 30, we can see the significance change after crossing the 16th digit. 

print("===1.4.3===")
print()
print("Finding the roots of your quadratic equation")
print()
print("Please input the coefficient of x^2 in your quadratic equation")
A = float(input())
print("Please input the coefficient of x in your quadratic equation")
B = float(input())
print("Please input the constant term in your quadratic equation")
C = float(input())
x1 = (-B + (B**2 - 4*A*C)**(1/2))/(2*A)
x2 = (-B - (B**2 - 4*A*C)**(1/2))/(2*A)
print ("The first solution for the quadratic equation is ",x1)
print ("The second solution for the quadratic equation is ",x2)
print()
print("If the value of A = 0, then we will have a ZeroDivisionError, this is a float division by zero, mathematically, it is undefined")

# i. 
# The intended purpose of this program is to find the roots of a quadratic equation, this is sometimes called the quadratic formula


# ii. 
# I used the following values;
# The first values are A = 1, B = -3, C = 2, Projected output, x1 = 2.0, x2 = 1.0
# The second values are A = 1, B = 0, C = -4 Projected output, x1 = 2.0, x2 = -2.0
# Program did not work correctly 

#iii 
# First, I realized that we can't use a variable before declaring them hence, the variables A,B,C will have to come up before we can use them
# Second, The 2A should be 2*A as python just like any other programming language can't interprete 2A
# Third, just like any programming language, any mathematical computation uses the precedence of BODMAS,i.e
# Bracket before of, before Division, before Multiplication, before Addition, before Subtraction
# The expression we had was running exponential 1 before dividing by 2 but what we wanted was exponential (1/2)
# Adding an additional bracket on the 1/2 solves the problem, the program now sees that it has to run exponential (1/2)
# The mistakes has been corrected and the output of my program is as expected

#iv 
#I have added the appropriate prompt and prints so that the inputs can be user friendly

#v. I have added a print to explain what happens when A=0