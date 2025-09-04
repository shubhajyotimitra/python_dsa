# Integer
x = 10
print(type(x))   # <class 'int'>

# Convert int to float
y = float(x)
print(y, type(y))   # 10.0 <class 'float'>

# Convert float to int (decimal part is removed)
z = int(10.75)
print(z, type(z))   # 10 <class 'int'>

# Convert int to complex
c = complex(x)
print(c, type(c))   # (10+0j) <class 'complex'>

# Convert int to string
s = str(x)
print(s, type(s))   # "10" <class 'str'>

# Convert string to int
num = int("123")
print(num, type(num))   # 123 <class 'int'>
