#sets

s = {2,4,2,6}
print(s)
#sets are unordered collections of unique elements
info = {"carla",19,False,5.9,19}
print (info)

#quickquiz
#try to create an empty set.check using he type()function whether the type of the variable is a set.

harry ={}
print(type(harry))
#it is a dictionary not a set.
#it is because in python {} is used to create an empty dictionary.
#therefore the above the code will be like an empty dictionary not an empty set.

#for enpty set:
harry = set()
print(type(harry))

#accessing set elements by for loop:

for value in info:
    print (value)


