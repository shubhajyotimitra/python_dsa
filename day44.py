#os module in python:

import os 
os.mkdir("data")
for i in range(0, 100):
    os.mkdir(f"data/day{i+1}")
#from the above program creates a main folder named data, and inside it, it automatically creates 100 subfolders named day1 to day100.


import os 
if(not os.path.exists("data")):
  os.mkdir("data")
for i in range(0, 100):
    os.mkdir(f"data/day{i+1}")
#if(not os.path.exists("data")): checks whether the folder named data exists or not, and runs the following code only if it doesn’t exist.

import os
for i in range(0, 100):
    os.rename(f"data/day{i+1}", f"data/Tutorial{i+1}")
#this will helps in rename the file.
