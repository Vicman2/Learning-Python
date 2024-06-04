import random
print("=====Assignment======")
print()
print("======4.2.1======")

def methodUseCases():

    print("The int")
    print("The method investegated: __invert__")
    print("It is used to invert an integer")
    theInt = int(input("Enter any integer of your choice: "))
    print(theInt.__invert__())

    print()
    print("The float")
    print("The method investegated: __ceil__")
    print("Approximates the floating number to the nearest integer")
    theFloat = float(input("Enter any floating number of your choice: "))
    print(theFloat.__ceil__())

    print()
    print("The String")
    print("The method investegated: join")
    print("The string whose method is called is inserted in between each given string")
    theString = "I am"
    print(theString.join([" the", " best"]))

    print()
    print("The List")
    print("The method investegated: __iadd__")
    print("This method merges two lists to become one by appending the items in the list passed as an argument to the __iadd__ function")
    theList = [2]
    print(theList.__iadd__([4, 5]))
methodUseCases()
print()
print("======4.2.2======")
#The difference between a function and and method is that a method is a function that is embeded in a class. 
# So a method is a special type of function that is embedded in a class

print()
print("======4.2.5======")
class Dice():
    def __init__(self, noOfDice=2):
        self.numdice = noOfDice
        self.diceFaces = [1,2,3,4,5,6]
        self.roll()
    def roll(self):
        self.Values = []
        for i in range(1, self.numdice + 1):
            self.Values.append(random.choice(self.diceFaces))
        return sum(self.Values)
    def sum(self):
        if len(self.Values) == 0:
            print("You have to first roll the dice")
            return None
        else:
            sum = 0
            for i in self.Values:
                sum = sum + i
            return sum
        

        

D = Dice(3)
print("Rolling a dice")
D.roll()
print("The values after rolling a dice is", D.Values)
print("The sum of the values are: ",D.sum())

        


