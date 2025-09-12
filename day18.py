#functon in python
#functions are of two types:
#user defines functions and built in functions 



def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)


a=9
b=8
if (a>b):
    print("first number is greater")
else:
    print("second number is greater or equal")    
calculateGmean(a,b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)

c = 8 
d = 74
if (c>d):
    print("first number is greater")
else:
    print("second number is greater or equal")    


# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c,d)


#for if condition we can also make functions though

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
def isGreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater is equal")  

def isLesser(a,b):
    if(a<b):
        print("first number is lesser")
    else:
        print("second number is lesser")    
                  

a=9
b=8
isGreater(a,b)

isLesser(a,b)

calculateGmean(a,b)

c=8
d=9
isGreater(c,d)

isLesser(c,d)

calculateGmean(c,d)

