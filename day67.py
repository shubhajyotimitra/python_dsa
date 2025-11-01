#class methods:
class Employee:
 company = "apple"
 def show(self):
    print(f" the name is {self.name} and the company is {self.company}")

 def changeCompany(cls , newCompany):
    cls.company = newCompany

e1 = Employee()
e1.name = "Harry"
e1.changeCompany("Google")
e1.show()
e1.changeCompany("Microsoft")
e1.show()   
e2 = Employee()
e2.name = "Rohan"
e2.show()   
e2.changeCompany("Amazon")
e2.show()

print(Employee.company)
# it will change the company for all the objects of the class because class method works with class and not with the object.
