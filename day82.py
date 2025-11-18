# Time module in python :
# the time module in Python provides various time-related functions. It allows you to work with time in different ways, such as getting the current time, pausing the execution of a program for a specified duration, and formatting time values.

import time
def usingWhile():
 i = 0 
 while i <500000:
    i +=1
    print(i)

def usingFor():
    for i in range (500000):
        print(i)

init = time.time()
usingFor()
t1 = (time.time() -init)
init = time.time()
usingWhile()
print (time.time() -init)
print(t1)

# Time sleep function :
print(4)
time.sleep(3)
print("This is printed after 3 seconds")


