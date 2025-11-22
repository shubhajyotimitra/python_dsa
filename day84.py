# Walrus operator:
# The walrus operator (:=) allows you to assign values to variables as part of an expression.
# This can make your code more concise and readable by reducing the need for separate assignment statements.    
# Example without walrus operator:
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for n in numbers:
    squared = n ** 2
    squared_numbers.append(squared)
print(squared_numbers)      
# Example with walrus operator:
numbers = [1, 2, 3, 4, 5]
squared_numbers = []        
for n in numbers:
    squared_numbers.append(squared := n ** 2)
print(squared_numbers)