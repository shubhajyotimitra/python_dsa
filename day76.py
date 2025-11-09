# Single inheritance :
# Single inheritance is a type of inheritance in python Single Inheritance means a child class (derived class) inherits properties and behaviors (attributes and methods) from only one parent class (base class).
# This allows code reusability and the extension of existing functionality.

class Animal :
    def __init__(self,name,species):
        self.name = name 
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")    
class Dog (Animal):
    def __init__(self, name, breed):
         Animal.__init__(self,name,species="Dog")
         self.breed = breed
    def make_sound(self):
        print("Bark!")    

class Cat (Animal):
    def __init__(self, name, breed):
         Animal.__init__(self,name,species="Cat")
         self.breed = breed
    def make_sound(self):
        print("Meow!")         

d = Dog("Dog","Doggerman")
d.make_sound()
a = Animal("Dog","Dog")
a.make_sound()  

#Quick Quiz : implement a cat class by using the animal class. Add some methods specific to cat.

d = Cat("Cat","Persian")
d.make_sound()
a = Animal("Cat","Cat")
a.make_sound()  
