#coutom errors in python
a = int(input("enter any value between 5 and 9 :"))

if (a<5 or a>9):
    raise ValueError ("Value should be between 5 and 9")

#in python we can raise coutom errors bu using the raise keyword.

#Defining custom errors in python

class NegativeNumberError(Exception):
    pass

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    return num ** 0.5

try:
    print(square_root(25))
    print(square_root(-9))
except NegativeNumberError as e:
    print("Error:", e)


# wrong way to use raise keyword:
# a = (input("enter any value between 5 and 9 or type quit :"))
# if a == "quit":
#     print("program is executed")
# elif (a<5 or a>9 ):
#     raise ValueError ("Value should be between 5 and 9")

#correct way to use raise keyword:
a = input("Enter any value between 5 and 9 or type quit: ")

if a == "quit":
    print("Program is executed")
elif a.isdigit():
    a = int(a)
    if a <=5 or a >= 9:
        raise ValueError("Value should be between 5 and 9")
    else:
        print("Valid input:", a)
else:
    raise TypeError("Only numbers between 5 and 9 or 'quit' are allowed")
