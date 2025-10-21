#classes and objects in python :
class person:
    name = "Shubh"
    occupation = "Software developer"
    networth = 1000000
    def info(self):
        print(f"{self.name} is a {self.occupation} having networth of {self.networth} ")
a = person()
# a.name = "shubham"
# a.occupation = "Data scientist"
# print(a.name , a.occupation)
a.info()