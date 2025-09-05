#exception handling examples
try:
    x = int("abc")
except ValueError as e:
    print("Error:", e)
finally:
    print("Execution completed")


#file handling examples
with open("demo.txt", "w") as f:
    f.write("Hello Python")

with open("demo.txt", "r") as f:
    print(f.read())


#useful python modules
import math, random
print(math.factorial(5))    
print(random.randint(1,10)) 

from collections import Counter
print(Counter("programming"))
