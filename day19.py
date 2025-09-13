#fuctions arguments in python

def average(a,b):
    print("the average is ", (a+b)/2)

average(4,6) 


#there are four types of argument that we can provide in a function:
# default arguments, keyword arguments,variable length argument,required arguments

#default argument
def average(a=4,b=6):
    print("the average is ", (a+b)/2)
average()


def name(fname, mname = "john", lname= "whatson"):
    print("hello," , fname,mname,lname)

name("amy")   

#keyword argument
def average(a=9 ,b=1):
    print("the average is ", (a+b)/2)
average(b =9, a=21)    


#required argument
def average(a ,b=1):
    print("the average is ", (a+b)/2)
average(b =9, a=21) 


def average(a ,b,c=1):
    print("the average is ", (a+b)/2)
average(b =9, a=20)


#variable length argument
def average(*numbers):
    print(type(numbers))
    sum=0

    for i in numbers:
        sum= sum+i
    print("average is: ",sum / len(numbers))
average(5,6,1)    



def name(**name):
    
    print(type(name))
    print("hello", name["fname"],name["mname"], name["lname"])

name(mname= "buchaman", lname = "barnes",fname="james")



#return statement
def average(*numbers):
    # print(type(numbers))
    sum=0

    for i in numbers:
        sum= sum+i
    # print("average is: ",sum / len(numbers))
    return sum / len(numbers)
c= average(5,6,7,1)
print(c)




