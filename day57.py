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

#to pass arguments to the decorated function:
def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("have a nice day")
    return mfx 
@greet
def hello ():
    print("hello world !")

def add (a,b):
    print (a+b)
hello ()
greet(add)(5,7)

#practical use case of decorators:
#1. logging
#2. authentication
#3. caching
#4. validation
#5. timing  

# example of logging decorator:    
#Important =>
import logging

logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

print(my_function(3, 5))
