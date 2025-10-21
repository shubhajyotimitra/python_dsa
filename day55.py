#classes and objects in python :
class person:
    name = "Shubh"
    occupation = "Software developer"
    networth = 1000000
    def info(self):
        print(f"{self.name} is a {self.occupation} having networth of {self.networth} ")
#the self parameter is a reference to the current instance of the class , and is used to access variables that belong to the class.

a = person()
b = person()
c = person()

a.name = "shubham"
a.occupation = "Data scientist"

b.name = "Nikita"
b.occupation = "HR"
print(a.name , a.occupation)

a.info()
b.info()
c.info() #in this case c will take the default values from the class person.
