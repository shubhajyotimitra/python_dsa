# read(), readlines() anad other methods
f=open('shubh.txt' , 'r')
while True:
    line = f.readline()
    print(line)
    if not line:
     print(line, type(line))
     break

f=open('shubh.txt' , 'r')
while True:
    line = f.readline()
    if not line:
     break
    print(line)

f=open('shubhm.txt' , 'r')
i = 0
while True:
    line = f.readline()
    i = i + 1
    if not line:
     break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in Maths is : {m1}")
    print(f"Marks of student {i} in Science is : {m2}")
    print(f"Marks of student {i} in Ssc is : {m3}")
    print(line)
    #if i have to change this into integer then we have to use typecasting method to do so 


#writelines method in python:
#The writelines() method is used to write multiple lines to a file at once. It belongs to Python's built-in file object and is used when working with files in text mode.

f = open('shubh2.txt' , 'w')
lines = ['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()
#writelines charecters doesnot add newline charecters between the strings in the sequence.
#if you want to add newlines between the strings , you can use a loop to write each string seperately.
