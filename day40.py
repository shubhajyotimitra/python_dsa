#Enumerate
marks = [12,36,32,98,12,45,1,4]

index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("osm shubh")
    index +=1
    
    
    
    
marks = [12,36,32,98,12,45,1,4]

for index, mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("osm shubh!!")

    
fruits = ['apple','banana','mango','grapes']
for index, fruits in enumerate(fruits):
    print(index, fruits)
    if(index==1):
        print("i love banana")


