#dir, __dict__and help method in python:
x = [1,2,3]
print(dir(x))
print(x.__add__)

y = (4,5,6)
print(dir(y))
print(y.__add__)
# The dir() function returns a list of valid attributes and methods for the specified object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.country = "India"
p = Person("Shubh", 21)
print(p.__dict__)
# The __dict__ attribute returns a dictionary representation of the instance's attributes.

print(help(Person))
# The help method provides an interactive help utility that displays the documentation of modules, classes, functions, and methods.