# Hybrid and hierarchical Inheritance in python :

# Hybrid inheritance is a type of inheritance in Python where more than one type of inheritance (such as single, multiple, multilevel, or hierarchical) is combined together in the same program.
# It forms a complex relationship between classes by mixing different inheritance patterns.

class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(BaseClass):
    pass

class A:
    def show(self):
        print("I am from Class A")

class B(A):
    def show(self):
        print("I am from Class B")

class C(A):
    def show(self):
        print("I am from Class C")

class D(B, C):
    def show(self):
        print("I am from Class D")
        super().show()   # Calls next class in MRO

# Create object of D
obj = D()
obj.show()

# Check MRO (Method Resolution Order)
print(D.__mro__)

