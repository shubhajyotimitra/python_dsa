#if else condition
a = int(input("enter you age: "))
print ("your age is : ",a)

#conditional operators >,<,>=,<=,==,!=
   
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
# print(a>18)

if (a>18):
    print("you can drive")
    print("yes")
else:
    print("you cannot drive")

#as you can see there is a space before print in line 10 and 12
#this space is called indentation
#python uses indentation to define a block of code


appleprice = 210
budget = 200
if (appleprice<=budget):
        print("buy apple")
else:
        print("do not buy apple")

#else if condition

appleprice = 90
budget = 200
if (budget-appleprice >50):
        print("buy apple")
elif (budget-appleprice > 70):
        print("buy 2 apples")
else:
        print("do not buy apple")



num = int(input("enter the value of the number:"))   
if (num>0):
    print("the number is positive")
elif (num==0):
    print("the number is zero")
else:
    print("the number is negative")    



    #nested if else condition
num = 18
if (num < 0):
    print("the number is negative")
elif (num > 0):
    if (num <= 10):
        print("the number is between 1 to 10")
    elif (num > 10 and num <= 20):
        print("the number is between 11 to 20")
    else:
        print("the number is greater than 20")
else:
    print("the number is zero")

