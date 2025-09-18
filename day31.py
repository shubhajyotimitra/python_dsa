#dictionaries

dic ={
    "shubh": "human being",
    "spoon":"object"
}
print(dic["shubh"])

dic ={
    344:"harry",
    56:"shubham",
    98:"rohan",
    78:"ankit"
}
print(dic[98])

info ={'name':'karan','age':21,'city':'delhi','eligible':True}
print(info['name'])
print(info.get('eligible'))
print(info.keys())

for key in info.keys():
    print(info[key])


for key in info.keys():
    print (f"The value corresponding to the key {key} is {info[key]}")


print(info.items())    
for key,value in info.items():
    print(f"the value corresponding to the key {key} is {value}")
