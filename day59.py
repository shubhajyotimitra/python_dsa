#Inheritance in python 
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee is {self.id} is {self.name}")

class Programmer (Employee):
    def showLanguage(self):
       print("The default language is Python")

e1 = Employee ("Rohan Das", 101)  
e1.showDetails()   
e2 = Employee("Leo Das", 102)  
e2 = Programmer("Leo Das", 102) #Creating object of Programmer class
e2.showDetails()  
e2.showLanguage() 

#In the above example, the Programmer class inherits from the Employee class. This means that the Programmer class has access to all the attributes and methods of the Employee class.
#Inheritance allows us to create a new class that is a modified version of an existing class, which helps in code reusability and establishing a hierarchical relationship between classes.

#types of inheritance in python:
#1. Single Inheritance
#2. Multiple Inheritance
#3. Multilevel Inheritance
#4. Hierarchical Inheritance
#5. Hybrid Inheritance  