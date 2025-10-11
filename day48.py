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