#Static methods in python:
# A static method is a method that belongs to a class rather than an instance of the class.
# It can be called on the class itself, rather than on an instance of the class.
# Static methods are defined using the @staticmethod decorator.
class Math:
    def __init__(self,num):
        self.num = num 
    def addtonum(self,n):
        self.num = self.num +n
    @staticmethod
    def multiply(a,b):
        return a*b  
a = Math(5)
print(a.num)
a.addtonum(3)
print(a.num)
print(Math.multiply(4, 6))  
print(a.multiply(2, 5))
# Note: Is it necessary to create an instance to call a static method? No