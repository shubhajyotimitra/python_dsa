# "Added Python fundamental exercises and examples."

# variable assignment =>
x = 5
y = "John"
print(x)
print(y)

# casting =>
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)    
print(y)
print(z)

# assigning multiple values =>
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

# output variable =>
x = "python is osm "
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + " " + y + " " + z)

x= 5
y = "john"
print(x)
print(y)

# global variable =>
x = "awesome"   
def myfunc():
  print("Python is " + x)   
myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# Getting he data type =>
x = 5
print(type(x))
y = "John"
print(type(y))      

# Python Numbers =>
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

#Integer =>
x = 1
y = 356562225548877110
z = -32555222
print(type(x))
print(type(y))
print(type(z))

#Float =>
x = 1.10        
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


#Complex =>
x = 3+5j
y = 5j
z = -5j 
print(type(x))
print(type(y))
print(type(z))

#Type Conversion =>
x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Random Number =>
import random

print(random.randrange(1, 10))

#Python Casting =>
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)
print(y)
print(z)

#Python String =>

#Quotes inside the quote 
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multiline String =>
a = """Aur bhai pankaj ,
kaise ho bhai,
bolo na bhai ,
koi bolta hi ni hai."""
print (a)

#String and Arrays 
a = "Hello, World!"
print(a[8])

#Looping Through a string =>
for x in "banana":
  print (x)

# String length =>
a = "Hello, World!"
print(len(a))  

#Check String =>
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best thing in the life is blessing "
if "blessing" in txt :
  print("yes , 'blessing' is present")

# Check if Not =>
txt = "The best thing in the life is free"
print ("expensive" not in txt)

txt = "the best thing in the life is free"
if "expensive" not in txt:
  print ("no , 'expensive' is not present")

# Slicing Strings 
b = "Hello, World!"
print(b[2:5])

# Slice from start 
b = "Hello, World!"
print(b[:5])

#Slicing to the end 
b = "bolo na bhai "
print(b[2:])

# Negative indexing 
b = "Hello, World!"
print(b[-5:-2])

# Modifing Strings =>
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

# Remove Whitespace
a = " Hello, World! "
print(a.strip())

# Replacing String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String 
a = "Hello, World!"
print(a.split(","))

# String concatenation 
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format =>
 # f-strings
age = 36
txt = f"My name is John, and I am {age} years old."
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

# Escape Characters =>
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#Python Booleans =>
# boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 20
b = 332

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# Evaluate Values and Variables 
print(bool("Hello"))
print(bool(15))  

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  x = 200
print(isinstance(x, int))

#Python Operators =>
print (10 + 5)   # Addition
sum1 = 10 + 5
print (sum1)
sum2 = sum1 + 20
print (sum2)  
sum3 = sum2 + sum2
print (sum3)
# Arithmetic Operators =>
x = 15
y = 13 
print(x + y)   # Addition
print(x - y)   # Subtraction
print(x * y)   # Multiplication
print(x / y)   # Division
print(x % y)   # Modulus
print(x ** y)  # Exponentiation
print(x // y)  # Floor Division (rounds down to the nearest whole number)

# Assignment Operators =>
x = 5
print(x)
x += 3
print(x)
x -= 2  
print(x)  
x *= 4  
print(x)  
x /= 2  
print(x)  
x %= 3  
print(x)  
x //= 2  
print(x)  
x **= 3  
print(x)  
x &= 4  
print(x)  
x |= 2  
print(x)  
x ^= 3  
print(x)  
x >>= 1  
print(x)  
x <<= 2  
print(x)  

# Walrus Operator =>
# The walrus operator := assigns values to variables as part of a larger expression.
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
  print(f"list has {count} elements ")

# Comparison Operators =>
x = 12
y = 7

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Chaining compariso operators 
x = 5
print(4 < x < 10)
print(1 < x and x < 10)

# Logical Operators =>
# and , or , not
a = 5
print(a > 3 and a < 10) 
print(a > 3 or a < 4)    
print(not(a > 3 and a < 10))  

# Identity Operators =>
# is , is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x 
print(x is z)
print(x is y)
print(x is not y)

# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

# Membership Operators =>
# in , not in
x = ["apple", "banana", "cherry"]
print("banana" in x)  
print("pineappple" not in x)

# Bitwise operator =>
print(6 & 3)
print(6 | 3)
print(6 ^ 3)

# Python operator precedence =>
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)

# List =>
# Lists are used to store multiple items in a single variable
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

# Access list items 
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# change list items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Add list items 
# append items 
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove list items 
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Loop list =>
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping using list comprehension =>
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] 

# List comprehension => (*)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Sort list =>
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist1 = [100, 50, 65, 82, 23]
thislist1.sort()
print(thislist1)
thislist1.sort(reverse = True)
print(thislist1)

# Costomize sort function =>
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy list =>
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) 
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#by slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Join list =>
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# List Method =>

# Method	-> Description
# append() ->	Adds an element at the end of the list
# clear() ->	Removes all the elements from the list
# copy() ->	Returns a copy of the list
# count()	-> Returns the number of elements with the specified value
# extend()	-> Add the elements of a list (or any iterable), to the end of the current list
# index()	-> Returns the index of the first element with the specified value
# insert()	-> Adds an element at the specified position
# pop()	-> Removes the element at the specified position
# remove()	-> Removes the item with the specified value
# reverse()	-> Reverses the order of the list
# sort()	-> Sorts the list

# Python Tuples =>
thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# MAIN DIFFERENCES =>
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Change tuple values =>
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Unpack tuple =>
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry") # (*)
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Loop through a tuple =>

# using for loop
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# using while loop 
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join tuple =>
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiple tuples =>
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Tuple Method =>
# count() ->	Returns the number of times a specified value occurs in a tuple
# index()	->  Searches the tuple for a specified value and returns the position of where it was found

# Python if else statememnt =>
# Python if 
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

is_logged_in = True
if is_logged_in:
  print("Welcome back!")

# Python Elif =>
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Multiple elif => We use elif when you have multiple mutually exclusive conditions to check. 
# This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

# Python else =>
# Use int() to convert the input string into an integer
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# complete if-elif-else chain =>
Temperature = int(input("Enter the temperature: "))
if Temperature > 30:
  print("It's a hot day")
elif Temperature > 20:
  print("It's a nice day")
elif Temperature > 10:
  print("It's a bit cold")
else:
  print("It's cold")

Username = input("Enter username: ")
if len(Username) > 0 :
  print(f"Welcome {Username}")
else:
  print("Username cannot be empty")  

# Short hand if =>
a = 5
b = 10
if a < b: print("a is less than b")

c = 3 
d = 7 
print("A") if c < d else print("B")

a = 10
b = 5
bigger = a if a > b else b
print("Bigger is", bigger)

# Logical operators =>
# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Nested if =>
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Multiple level of nesting =>
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

# Pass statement =>

# The pass statement is useful in several situations:
# When you're creating code structure but haven't implemented the logic yet
# When a statement is required syntactically but no action is needed
# As a placeholder for future code during development
# In empty functions or classes that you plan to implement later

a = 33
b = 200 
if b > a:
  pass  

# Pass with multiple conditions  =>
    
value = 42
if value < 0:
    print("Negative value")
elif value == 0:
    pass  # Placeholder for future logic when value is zero
else:
    print("Positive value") 

# Python functions =>

def my_function():
  print("Hello from a function")

my_function()
# Why we use =>
# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions, you would have to write the same calculation code repeatedly:

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

def get_greeting():
  return "Hello from a function"

print(get_greeting())

# If you need to create a function placeholder without any code, use the pass statement:
# because functions cannot be empty.

# Python function arguments =>
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(name): # name is a parameter
  print("Hello", name)
my_function("Emil") # "Emil" is an argument

# Number of arguments =>
def my_function(fname, lname):
  print(fname + " " + lname)  
my_function("Emil", "Refsnes") 

# Default parameter value =>



# Python Range =>

# Call range() with one Argument
x = range(3,10)
for i in x:
  print(i)

# Using List to Display Ranges =>
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))  

# Slicing range =>
r = range(10)
print(r[2])
print(r[:3])

# Membership Testing =>
r = range(0, 10, 2)
print(6 in r)
print(7 in r)

# Length =>
r = range(0, 10, 2)
print(len(r))

# Python Arrays => (Doubt in this topic)

# append()	Adds an element at the end of the list
# clear()	  Removes all the elements from the list
# copy()	  Returns a copy of the list
# count()	  Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	  Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	  Sorts the list
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

# Python iterators =>
# An iterator is an object that contains a countable number of values.
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)  
print(next(myit))
print(next(myit))
print(next(myit)) 

# Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping through an iterator =>
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

mystr = "banana"

for x in mystr:
  print(x)  

# Create an iterator =>
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

# Example (Doubt)
# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Stopiteration =>
# Stop after 20 iteration 

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

# Python Modules =>
import mymodule
mymodule.greeting("Pankaj")

# Variable in module =>
import mymodule

a = mymodule.person1["age"]
print(a)

# Renaming a module =>
import mymodule as mx

a = mx.person1["age"]
print(a)

# Built in modules =>
import platform
x = platform.system()
print(x)


import platform

x = dir(platform)
print(x)

from mymodule import person1

print (person1["age"])

# Python Datetime =>
import datetime

x = datetime.datetime.now()
print(x)


# Date Output =>
# Return the year and name of that weekday =>
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


# Creating Date Objects
import datetime

x = datetime.datetime(2003, 10, 7)

print(x)

import datetime

x = datetime.datetime(2003, 10, 7)

print(x.strftime("%B"))

# Python Math
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#The abs() function returns the absolute (positive) value of the specified number:

x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)

# The Math Module =>
import math

x = math.sqrt(64)

print(x)

# The math.ceil() method rounds a number upwards to its nearest integer 
# math.floor() method rounds a number downwards to its nearest integer, and returns the result:
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) 
print(y) 

import math

x = math.pi

print(x)

# Python JSON => (Doubt)
# Parse JSON - Convert from JSON to Python
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# Convert from Python to JSON
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# Python Regex (Doubt)


# Python Try Except =>
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling =>
try:
  print(x)
except:
  print("An exception occurred")

# Many Exceptions =>
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")  

# Else =>
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Finally =>
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Raise an Exception =>
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

# Python String formatting =>
txt = f"The price is 49 dollars"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Performing operations in F-String =>
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

# Execute Functions in F-String =>
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

# String Format =>
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Multiple Values =>
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Python None =>
x = None
print(x)
print(type(x))

result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")

result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")

# True or False =>
print(bool(None)) 

# Functions that return None =>
def myfunc():
  x = 5

x = myfunc()
print(x)

# Python User Input =>
name = input("Enter your name:")
print(f"Hello {name}")

# Multiple inputs =>
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# Input Number =>
x = input("Enter a number:")
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")

# Validate Input => (Doubt)
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")


# File Handling =>
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# Open a file on the server =>
f = open("demofile.txt")
print(f.read())

# If the file is located in a different location, you will have to specify the file path, like this:
# f = open("D:/myfiles/demofile.txt")
# print(f.read()) 

# Using the with statement =>
# The with statement is used in Python for resource management and exception handling.
# You can also use the with statememt when opening a file 
with open("demofile.txt") as f:
  print(f.read())

# Close a file =>
# If you are not using the with statement, you must write a close statement in order to close the file:
f = open("demofile.txt")
print(f.readline())
f.close()

# Read Only Parts of the File =>
with open("demofile.txt") as f:
  print(f.read(5))
  print(f.read(10))

# Read Lines =>
with open("demofile.txt") as f:
  print(f.readline())

# Looping Through the File Line by Line =>
with open("demofile.txt") as f:
  for line in f:
    print(line)  

# Python file write =>

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())

# "x" - Create - will create a file, returns an error if the file exists
# f = open("myfile.txt", "x")

# Python delete file =>

# Delete a file 
import os
os.remove("myfile.txt")

# Check if file exist:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# Delete folder =>
import os
os.rmdir("myfolder")