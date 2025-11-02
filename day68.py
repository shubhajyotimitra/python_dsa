#Class methods as alternative constructors:
class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

e1 =  Employee("Shanu",12000)
print(e1.name)
print(e1.salary)

string = "Rohan-12000"
e2=  Employee(string.split("-")[0],string.split("-")[1])
print(e2.name)
print(e2.salary)

# Now using class method as alternative constructor

class consultant:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def from_string(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])

c1 =  consultant("Shivam",12000)
print(c1.name)
print(c1.salary)

string = "Rohit-12000"
c2=  consultant.from_string(string)
print(c2.name)
print(c2.salary)