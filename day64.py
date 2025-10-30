#Instance varialbles vs Class Variables in Python
class Employee:
    def __init__(self , name ):
        self.name = name  # Instance Variable
        self.raise_amount = 1.05  # Instance Variable
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount is {self.raise_amount}") 
emp1 = Employee("Alice")
emp1.raise_amount = 1.10  # Modifying instance variable for emp1
emp2 = Employee("Bob")
emp1.showDetails()  # Output: Employee Name: Alice
# Employee.showDetails(emp1)  # Output: Employee Name: Alice
#It is same as above line
emp2.showDetails()  # Output: Employee Name: Bob

class Employee:
    companyName = "TechCorp"  # Class Variable
    def __init__(self , name ):
        self.name = name  # Instance Variable
        self.raise_amount = 1.05  # Instance Variable
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}") 
emp1 = Employee("Ramesh")
emp1.companyName = "InnovateLtd"  # This creates an instance variable, does not modify class variable
emp1.showDetails()  # Output: Employee Name: Ramesh
Employee.companyName = "GlobalTech"  # Modifying class variable
print( Employee.companyName)

emp2 = Employee("Suresh")
emp2.companyName = "AlphaSolutions"  # This creates an instance variable for emp2
emp2.showDetails()  # Output: Employee Name: Suresh
print( emp2.companyName)  # Output: AlphaSolutions
#the above program says that emp1 is able to access the class variable companyName through the instance emp1.
