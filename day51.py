#Map, filter and reduce in python:
#simplest way to understand map function is to see it as a for loop that applies a function to each item in an iterable (like a list) and returns a new iterable (like a list) with the results.
#by using defined function:

def cube(x):
    return x**3
print(cube(3))
l = [1,2,3,4,5]
newl = []
for item in l:
    newl.append(cube(item))
print(newl)

#by using map function and defined function:
def cube(x):
    return x**3
print(cube(3))
l = [1,2,3,4,5]
newl = list(map(cube,l))
print(newl)

#filter function:
def filter_function(x):
 return x>4
newnewl = list(filter(filter_function,l))
print(newnewl)

#by lambda function:
l = [1,2,3,4,5,6,7,8,9]
newl = list(map(lambda x: x**3,l))
print(newl)
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

#reduce function:
#by using lambda function 
from functools import reduce
l = [1,2,3,4]
product = reduce(lambda x,y: x*y , l)
print(product)

#by using defined function
from functools import reduce
l = [1,2,3,4]
def mysum(x,y):
    return x+y
sum = reduce(mysum,l)
print(sum)