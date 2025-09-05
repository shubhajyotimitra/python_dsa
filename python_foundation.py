#for loop and while loop examples 
for i in range(5):  
    print(i)  # 0 to 4

n = 5
while n > 0:
    print(n)
    n -= 1
#type casting examples
a = "100"
print(int(a) + 5)   
print(float(a) + 0.5) 
print(str(123))       

#input handling example
num = int(input("Enter a number: "))
print(f"You entered {num}, its square is {num**2}")

#control flow examples
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
