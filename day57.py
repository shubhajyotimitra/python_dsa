#Decorators in python

def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("have a nice day")
    return mfx

@greet
def hello ():
    print("heyy i am felling good today ")
hello ()
# A decorator is a function that takes another function as input and extends its behavior without modifying its structure.
# the above code can also be written as :
def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("have a nice day")
    return mfx

def hello ():
    print("heyy i am felling good today ")
greet(hello) ()

