#"is" vs "=" in python:
a = 4
b = "4"
print(a is b)#exact location of object in memory 
print(a == b)#value comparison

a = (1,2)
b = (1,2)
print(a is b)
print(a == b)