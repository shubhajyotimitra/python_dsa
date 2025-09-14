#tuples

tup = (1,2,3,4,5)
print(type(tup),tup)
# #list can be changed but tuples cant be

tup=(1,2,3,"shubha",56,78,"wow")
print(type(tup),tup)
print(tup[0])
print(tup[2])
print(tup[3])
print(tup[-1])

if 56 in tup:
    print("yes 56 is present in tup")

tup2=tup[1:4]    
print(tup2)


#also we know that tuples are immutable
