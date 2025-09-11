#loops work in the form of iteration
#break and continue 


for i in range(12):
 if(i == 10):
  break
 print("5 *", i+1, "=" , 5 * (i+1))
print("loop ko chorkar chale jao") 


for i in range(12):
 if (i == 10):
  print("skip the iteration")
  continue
 print("5 *", i, "=", 5*i)


#to imulate while loop in python

i=0
while True:
 print(i)
 i=i+1
 if(i%100 == 0):
  break