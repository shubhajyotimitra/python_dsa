# Method overriding in python :
# method overriding is a powerful feature in oops that allows you to redefine in a derived class .
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y 

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        # return 3.14 * self.radius*self.radius => in place of this we can also write :
        return 3.14 * super().area()
rec = Shape(3,5)  
print(rec.area())  

c = Circle (5)
print(c.area())

class Shape:
    def area(self):
        return 0
    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def perimeter(self):
        print("Perimeter of square:")
        return super().perimeter()

sq = Square(4)
print("Area:", sq.area())
print("Perimeter:", sq.perimeter())

