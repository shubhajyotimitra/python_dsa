#constructor in python
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
   def __init__(self,n,o):
      print("heyy i am a person")
      self.name = n
      self.occ = o

   def info(self):
    print(f"{self.name} is a {self.occ}")
c = Person2("harry", "programmer")
d = Person2("rohan", "manager")

c.info()
d.info()