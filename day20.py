# list
# list are ordered collection of data types
# list can be changed but tuples cant be changed
# in list different data types can be stored


l = [3,5,6]
print(l)
print(type(l))


marks =[30,35,37,"shubhajyoti"]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

print(marks[-3])#negative index
print(marks[len(marks)-3])#positive index
print(marks[5-3])#positive index
print(marks[2])#positive index

if 7 in marks:
    print("yes")
else:print ("no")
if "ha" in "shubhajyoti":
    print("yes")
else:
    print("no")


print(marks) 
print(marks[1:-1])
print(marks[1:3:2])   


#question:1
name=["c","r","a","z","y","g","u","y"]
print(name)
print(type(name))
if "g" in name and "u"in name :
    print("yes")
else:
    print("no")

#question:2
name =["crazyguy"]
print(name)
if "gu" in "crazyguy":
    print("gu is present in crazyguy")
else:
    print("gu is not present") #same thing apply ffor string as well

#list comprehension

lst = [i for i in range(4)]
print(lst)

lst = [i for i in range(10)if i%2 ==0]
print(lst)

lst = [i*i for i in range(10)if i%2 ==0]
print(lst)






