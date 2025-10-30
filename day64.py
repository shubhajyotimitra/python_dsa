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

#Example 1:

class Employee:
    companyName = "TechCorp"  # Class Variable
    noofEmployees = 0  # Class Variable
    def __init__(self , name ):
        self.name = name  # Instance Variable
        self.raise_amount = 1.05  # Instance Variable
        Employee.noofEmployees += 1
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noofEmployees} sized {self.companyName} is {self.raise_amount}") 
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

#Example 2:

class Employee:
    # Class Variables
    companyName = "TechCorp"
    noofEmployees = 0  

    def __init__(self, name, salary):
        # Instance Variables
        self.name = name  
        self.salary = salary
        self.raise_amount = 1.05  
        Employee.noofEmployees += 1  # updates class variable count

    def showDetails(self):
        print(f"Employee Name   : {self.name}")
        print(f"Salary          : ₹{self.salary}")
        print(f"Company Name    : {self.companyName}")
        print(f"Raise Amount    : {self.raise_amount}")
        print(f"Total Employees : {Employee.noofEmployees}")
        print("-" * 40)

    @classmethod
    def showCompanyInfo(cls):
        print(f"🏢 Company: {cls.companyName}")
        print(f"👥 Total Employees: {cls.noofEmployees}")
        print("=" * 40)

    @staticmethod
    def greet():
        print("✨ Welcome to the Employee Management System ✨")
        print("=" * 40)


# ---- Program Execution ----
Employee.greet()

emp1 = Employee("Ramesh", 50000)
emp1.companyName = "InnovateLtd"  # creates instance variable
emp1.showDetails()

Employee.companyName = "GlobalTech"  # modifies class variable
Employee.showCompanyInfo()

emp2 = Employee("Suresh", 60000)
emp2.companyName = "AlphaSolutions"  # creates instance variable for emp2
emp2.showDetails()

# Accessing company name from class and instance
print("emp1.companyName →", emp1.companyName)
print("emp2.companyName →", emp2.companyName)
print("Employee.companyName →", Employee.companyName)

