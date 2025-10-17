#Map, filter and reduce in python:
# def cube(x):
#     return x**3
# print(cube(3))
# l = [1,2,3,4,5]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)

def cube(x):
    return x**3
print(cube(3))
l = [1,2,3,4,5]
newl = list(map(cube,l))
print(newl)

#filter function:

