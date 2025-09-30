# x = 4

# match x:
#     case 0:
#         print("x is zero")
#     case 4 if x % 2 == 0:
#         print("x % 2 == 0 and case is 4")
#     case _ if x <10:
#         print("x is less than 10")



x = int(input("enter the value of x:"))

match x:
    case 0:
        print("x is zero")
    case 4 if x % 2 == 0:
        print("the value is divisible by 2")
    case _:
        print("x is less than 10")



x=int(input("enter the value of x:"))
match x:
        case 0:
            print("x is zero")
        case 4:
         print("case is 4")
        case _ if x!=90:
            print(x, "is not equal to 90")
        case _ if x!=80:
                print(x,"is not equal to 80")     

