#exception handling in python

a = input("Enter a number: ")
print(f"multiplication table of {a} is: ")

for i in range(1,11):
 print(f"{a} x {i} = {int(a)*i}")