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
