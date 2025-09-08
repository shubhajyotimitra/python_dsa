# Create a python program  capable of greeting you with good morning , good afternoon , good evening your program should uses time module to get the. Current hour here is a sample program and documentation link for you
# import time 
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

import time 
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)

if 5<=timestamp<12:
    print("good morning")
elif 12<=timestamp<16:
    print("good afternoon")
elif 16<=timestamp<21:
    print("good evening")
else:
    print("good night")

