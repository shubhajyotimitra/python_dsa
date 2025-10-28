#Access specifiers =>

#Access specifiers in Python are used to define the visibility and accessibility of class members (attributes and methods). Python has three types of access specifiers:
#1. Public Access Specifier
#2. Protected Access Specifier
#3. Private Access Specifier

class Employee:
    def __init__(self):
        self.name = "Shubham"
    
a = Employee()
print(a.name) # Accessing public attribute

#private access specifier in python are used to restrict access to class members.
# private access specifier is used with double underscore __ 

class Employee:
    def __init__(self):
        self.__name = "Shubham"
    
a = Employee()
#print(a.__name) cannot be accessed directly 
print(a._Employee__name) #can be accessed indirectly using name mangling
print(a.__dir__()) #to see all attributes of the class including private ones
#name mangling is a mechanism in Python that alters the name of a private attribute to include the class name, making it harder to access from outside the class.

#Protected access specifier in python are used to indicate that a class member is intended for internal use within the class and its subclasses.
#Protected access specifier is used with a single underscore _

class Student:
    def __init__(self):
        self._name = "Shubh"

    def _funName(self):  #protected method
        return "Hello Shubh"
    
class Subject(Student):  #inherited class 
    pass 
    
obj = Student()
obj1 = Subject()

#calling by object of Student class =>
print(obj._name)  #accessing protected attribute
print(obj._funName())  #accessing protected method
#calling by object of Subject class =>
print(obj1._name)  #accessing protected attribute
print(obj1._funName())  #accessing protected method

# Example demonstrating all three access specifiers =>

class Car:
    def __init__(self, make, model):
        self.make = make          # Public attribute
        self._model = model       # Protected attribute
        self.__year = 2020        # Private attribute

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self._model}")
        print(f"Car Year: {self.__year}")

car1 = Car("Toyota", "Camry")   # create an object
car1.display_info()             # call the method

class Employee:
    def __init__(self, name, salary):
        self.name = name            # Public attribute
        self._department = "HR"     # Protected attribute
        self.__salary = salary      # Private attribute

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Department: {self._department}")
        print(f"Salary: {self.__salary}")


# Create an object of Employee
emp1 = Employee("Shubh", 50000)

# Call the method to display employee details
emp1.display_details()

# Accessing public attribute directly
print("\nAccessing Public Attribute:")
print(emp1.name)

# Accessing protected attribute (possible but not recommended)
print("\nAccessing Protected Attribute:")
print(emp1._department)

# Accessing private attribute (NOT directly accessible)
print("\nAccessing Private Attribute the safe way:")
print(emp1._Employee__salary)   # Name mangled form
