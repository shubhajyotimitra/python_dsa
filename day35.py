#finally keyword in python

try:
    l = [1,5,6,7]
    i = int(input("Enter the index:"))
    print(l[i])
except:
    print("Some error occured")

finally:
    print("I am always executed")

    

def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index:"))
        print(l[i])
    except:
        print("Some error occured")
        return 0 
    finally:
        print("I am always executed")

x= func1()
print(x)

#finally keyword is always executed whether exception is there or not.
#it is generally used to close the file or release the resource.