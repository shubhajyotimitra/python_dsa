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
    
obj = Myclass(10)
print(obj.ten_value)  #getter
obj.show() 