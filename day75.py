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
    def __add__(self,x):
        return f"{self.i +x.i}i + {self.j+x.j}k + {self.k+x.k}k"
v1= Vector(3,5,6)
print(v1)          
v2= Vector(3,5,6)
print(v2)     
print(v1 +v2) 
print(type(v1+v2))
# for the above code the type of the output is str 
# in an order to get the output as the real vector we have to do this like below :
class Vector :
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}k + {self.k}k"
    def __add__(self,x):
        return Vector(self.i + x.i, self.j + x.j , self.k + x.k)
v1= Vector(3,5,6)
print(v1)          
v2= Vector(3,5,6)
print(v2)     
print(v1 +v2) 
print(type(v1+v2))