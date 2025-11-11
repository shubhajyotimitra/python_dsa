# Multiple inheritance:
# Multiple Inheritance means a child class inherits from more than one parent class.
# That is, a derived class can access attributes and methods from multiple base classes.

# Syntax:

# class Parent1:
#     pass

# class Parent2:
#     pass

# class Child(Parent1, Parent2):
#     pass

class Employee:
    def __init__(self, name):
        self.name = name
    def show (self):
        print(f"The name is {self.name}")
    

class Dancer:
    def __init__(self,dance):
        self.dance = dance
    def show (self):
        print(f"The dance is {self.dance}")    

class DancerEmployee(Dancer,Employee):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name

o = DancerEmployee("Kathak","Shivani")
print(o.name)
print(o.dance)
o.show()
