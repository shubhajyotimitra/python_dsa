#file IO in python:

#READING A FILE 
f= open('myfile.txt','r')
print(f)
text = f.read()
print(text)
f.close()

#WRITING A FILE
f=open('myfile2.txt', 'w')
f.write('hello, world!')
f.close()

#if we open the file in the form of append then the number of times we run program , the text file will add on.
f=open('myfile2.txt', 'a')
f.write('hello, world!')
f.close()
with open('myfile2.text', 'a') as f:
    f.write("heyy i am inside with")