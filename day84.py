# Walrus operator:
# The walrus operator (:=) allows you to assign values to variables as part of an expression.
# This can make your code more concise and readable by reducing the need for separate assignment statements.    


a = True
print(a:=False)  # Assigns False to a and prints it

# Example of walrus operator in a while loop:
numbers = [1, 2, 3, 4, 5]
while (n:=len(numbers)) > 0:
    print(numbers.pop())

# Example without walrus operator 
# foods = list()
# while True:
#     food = input ("what food do you like?:")
#     if food == "quit":
#         break
#     foods.append(food)    

# Example with walrus operator:
foods = list()
while (food := input("what food do you like?:")) != "quit":
    foods.append(food)


# Example without walrus operator:

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = []
# for n in numbers:
#     squared = n ** 2
#     squared_numbers.append(squared)
# print(squared_numbers)  

# # Example with walrus operator:

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = []        
# for n in numbers:
#     squared_numbers.append(squared := n ** 2)
# print(squared_numbers)

