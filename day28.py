#recursion
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))
print(factorial(4))
print(factorial(3))


#recursion is the process of defining something in terms of itself


#fabonacci series
#write a program to print fibonacci series
#f(0)=0
#f(1)=1
#f(2)=f(1)+f0
#f(n) =f(n-1)+f(n-2)   