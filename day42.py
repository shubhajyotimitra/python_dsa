#how to import work in python
import math
result = math.sqrt(9)
print(result)

from math import sqrt,pi
result = sqrt(80) * pi
print(result)

from math import *
result = sqrt(9)
print(result)
print(pi)
#the above snippet is generally not reccomanded as it can lead to confusion and make it harder to understand where specific functions and variable are coming from.


import math as m
result = m.sqrt(9)* m.pi
print(result)
#the above as keyword is can be useful when you want to use a shorter or more descriptive name for a module

#dir function
import math
print(dir(math))
#in this we got to know the names of all the functions and variables defined in a module.

import math
print(math.nan,type(math.nan))
#by this we can also find the type of the function.


from shubh import welcome,shubh
welcome()
print(shubh)

from shubh import *
welcome()
print(shubh)
