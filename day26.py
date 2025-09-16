#string formatting in python

letter= "hey my name is {} and I am from {}"
country = "india"
name = "harry"
print(letter.format(name,country))

#if i would print #print(letter.format(country,name)) then the output would be "hey my name is india and I am from harry"
#it is wrong


letter= "hey my name is {0} and I am from {1}"
country = "india"
name = "harry"
print(letter.format(name,country))

#here 0 and 1 are the index values of the arguments passed in the format function

#hence we use abstract index values to avoid confusion

letter= "hey my name is {} and i am from {}"
country = "india "
name = "shubhajyoti"
print(letter.format(name,country))
print(f"hey my name is {name} and i am from {country}")

#.2f
txt = "for only {price:.2f}dollars!"
print(txt.format(price = 49.099999))

#also we can write this code as :

price= 49.099999
txt = f"for only {price:.2f}dollars!"
print(txt)

print(f"{30*2}")

#if we want to see print(f"hey my name is {name} and i am from {country}") as it is 
#then we have to use double {{}} so that the {name},{country} will not assignes and print as it is the statement is being printed.
