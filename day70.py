# Super keyword in python :
# super keyword is used to call a method from a parent class in a child class.

class ParentClass:
    def parent_method(self):
        print("This is the parent method. ")
class ChildClass(ParentClass):
    def parent_method(self):
        print("Harry")
        super().parent_method()
    def child_method(self):
        print("This is the child method. ")
        super().parent_method()
child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name= name
        self.id = id
class Programmer(Employee):
    def __init__(self, name ,id , lan):
        self.lan = lan
        super().__init__(name , id)

rohan = Employee("Rohan", "101")
shubh = Programmer("Shubh", "102", ["Python" , "C++"])    
print(shubh.name)
print(shubh.id)
print(shubh.lan)