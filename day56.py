#constructors in python
class Person:
    name = "shubh"
    occ = "developer"
    def info(self):
     print(f"{self.name} is a {self.occ}")
a = Person()
a.name = "Divya"
a.occ = "Data analyst"
a.info()

class Person2:
   def __init__(self,name,occ):
    #   print("heyy i am a person")
      self.name = name
      self.occ = occ

   def info(self):
    print(f"{self.name} is a {self.occ}")
c = Person2("harry", "programmer")
d = Person2("rohan", "manager")

c.info()
d.info()

#types of constructors:
#1. default constructor : it doesnt take any parameters and assigns default values to the object attributes.
#2. parameterized constructor : it takes parameters to initialize the object attributes with custom values.