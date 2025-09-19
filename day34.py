#exception handling in python

a = input("Enter a number: ")
print(f"multiplication table of {a} is: ")

for i in range(1,11):
 print(f"{a} x {i} = {int(a)*i}")

print("some line of code")
print("end of program")

#if i enters string in the input then it will give an error 
#in an order to avoid this we use exception handling

a = input("Enter a number: ")
print(f"multiplication table of {a} is: ")
try:
  for i in range(1,11):
   print(f"{a} x {i} = {int(a)*i}")
except:
    print("Invalid input")

print("some line of code")
print("end of program")
#hence in this way if we enter any string then it will not give error 
#instead it will print invalid input and the program will run successfully.

