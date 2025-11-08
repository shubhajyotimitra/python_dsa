# Operator Overloading in python :
# Operator overloading is a feature in python that allows deveelopers to redefine the behaviour of mathematical and comparison operators for custom data types.
# this means that you can use the standard mathematical operators (+,-,*,/,etc)
# comparisonn operators (<,>,==,etc.) in your own classes, just as you would for built-in data types like int,float, and str.

class Vector :
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}k + {self.k}k"
v = Vector(3,5,6)
print(v)          
    