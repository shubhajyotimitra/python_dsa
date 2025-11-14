# Multilevel Inheritance :
# Multilevel Inheritance means when a class is derived from another derived class — i.e., inheritance happens in multiple levels.
# So,
# Class A → Base class
# Class B → Derived from A
# Class C → Derived from B
# This forms a chain of inheritance.

# Syntax :

# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

class Animal:
    def __init__(self, name , species):
        self.name = name 
        self.species = species

    def show_details(self):
        print(f"Name : {self.name}") 
        print(f"Species: {self.species}") 

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self , name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)  
        print(f"Breed: {self.breed}")

class GoldenRetriver(Dog):
    def __init__(self , name , color):
        Dog.__init__(self , name , breed = "Golden Retriever" )
        self.color = color 

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = GoldenRetriver("Tommy", "Black")
o.show_details()
             
