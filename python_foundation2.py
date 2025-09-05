# Function with multiple return values
def arithmetic(a, b):
    return a+b, a-b, a*b

print(arithmetic(10, 5))  

# Keyword & default arguments
def greet(name, msg="Good morning"):
    print(f"Hello {name}, {msg}")

greet("Shubho")                   
greet("Shubho", "Welcome back!")  
greet(msg="How are you?", name="Shubho")  



#list 
lst = [1, 2, 3, 4, 5]
print(lst[1:4])    
print(lst[::-1])   

#strings
s = "python programming"
print(s.title())   
print(s.split())   
print("-".join(["a","b","c"]))  


#sets example 
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   
print(A & B)   
print(A - B)   
