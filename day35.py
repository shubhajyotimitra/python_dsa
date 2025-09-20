#finally keyword in python

try:
    l = [1,5,6,7]
    i = int(input("Enter the index:"))
    print(l[i])
except:
    print("Some error occured")

finally:
    print("I am always executed")

