#Lambda functions in python:
def double(x):
    return x*2
print(double(5))
#in the above code while defining def function we can see there we have to define code into 2 lines .
#but while using lambda functions we can define any function in one line .


double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y : (x+y)/2
ag = lambda x,y,z : (x+y+z)/3
print(double(5))
print(cube(5))
print(avg(3,5))
print(ag(3,5,10))
    