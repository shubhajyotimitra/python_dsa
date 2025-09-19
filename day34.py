#exception handling in python

# a = input("Enter a number: ")
# print(f"multiplication table of {a} is: ")

# for i in range(1,11):
#  print(f"{a} x {i} = {int(a)*i}")

# print("some line of code")
# print("end of program")

# #if i enters string in the input then it will give an error 
# #in an order to avoid this we use exception handling

# a = input("Enter a number: ")
# print(f"multiplication table of {a} is: ")
# try:
#   for i in range(1,11):
#    print(f"{a} x {i} = {int(a)*i}")
# except:
#     print("Invalid input")

# print("some line of code")
# print("end of program")
#hence in this way if we enter any string then it will not give error 
#instead it will print invalid input and the program will run successfully.

try:
  num = int(input("enter an integer:"))
  print(f"You entered {num}")
except ValueError:
  print("Number entered is not an integer.")




try:
 num = int(input("enter an integer:"))
 print(f"You entered {num}")
 a = [6,7,8,9,3,2,4]
 print(a[num])  
except ValueError:
  print("Number entered is not an integer.")
except IndexError:
  print("Index is out of range")


#this is how basic exception handling works in python.

