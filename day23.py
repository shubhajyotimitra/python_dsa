#tuples methods

countries=("spain","italy","india","england","germany")
temp=list(countries)
temp.append("russia")
temp.pop(3)
temp[2]="finland"
countries= tuple(temp)
print(countries)
#thus we can convert tuple into list and thereafter the list is again changed in to tuple and print

countries=("italy","afganistan","bangladesh","united state","russia")
countries2=("vietnam","india","china",)
southEastAsia=countries+countries2
print(southEastAsia)
# #hence we can merge tuples in this way 

tuple1=(0,1,2,3,4,1,4,5,3)
res=tuple1.count(3)
print("count of 3 in tuple1 is :", res)

tuple1=(0,1,2,3,4,1,4,5,3)
res=tuple1.index(3)
print("count of 3 in tuple1 is :", res)

tuple1=(0,1,2,3,4,1,4,5,3,3,33)
res=tuple1.index(3,2,8)
print("count of 3 in tuple1 is :", res)

#to find the lenght of the tuple
tuple1=(0,1,2,3,4,1,4,5,3,3,33)
res=len(tuple1)
print("lenght of the tuple is:",res)
