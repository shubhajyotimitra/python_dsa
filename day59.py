#Inheritance in python 
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee is {self.id} is {self.name}")
e1 = Employee ("Rohan Das", 101)  
e1.showDetails()   
e2 = Employee ("Leo Das", 102)  
e2.showDetails()   