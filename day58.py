#Getter and Setter in python:

class Myclass:
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}")
    @property 
    def value(self):
        return self._value
    
obj = Myclass(10)
print(obj.value)  #getter
obj.show() 


class Myclass:
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}")
    @property 
    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value / 10
    
obj = Myclass(10)
obj.ten_value = 50   #setter
print(obj.ten_value) #getter
obj.show() 

#Getter in python is used to access the value of a private attribute, while Setter is used to modify the value of a private attribute.
#Setters in python are defined using the @property_name.setter decorator, where property_name is the name of the property for which the setter is being defined.