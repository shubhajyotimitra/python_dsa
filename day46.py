#local vs global variable
x=4
print(x)

def hello():
    x=5
    print(f"the local x is {x}")
    print("hello shubh")

print(f"the global x is {x}")
hello()
x=5
print(f"the global x is {x}")