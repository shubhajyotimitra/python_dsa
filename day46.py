#local vs global variable:

x=4
print(x)

def hello():
    x=5
    y=1
    print(f"the local x is {x}")
    print(f"the local y is {y}")
    print("hello shubh")

print(f"the global x is {x}")
hello()
x=5
print(f"the global x is {x}")


x=10
def my_function():
    global x
    x=4
    y=5
    print(y)
my_function()
print(x)
 #in this if we print(y) then it will cause an error because y is a local varialbe and is not accessible outside of the functions.


