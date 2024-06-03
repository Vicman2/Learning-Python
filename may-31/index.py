class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def perimeter(self):
        p = 2 * self.length + 2 * self.width
        return p
    def area(self):
        a = self.length * self.width 
        return a 

R = Rectangle(5,10)
S = Rectangle(6,2)
print(R.area())
print(R.perimeter())
help(int.as_integer_ratio)