#seek(), tell() and other functions
# with open('file.txt' , 'r') as f:
#     print(type(f))
#     #Move to the 10th byte in the file
#     f.seek(10)

#     #read the next 5 bytes
#     print(f.tell())
#     #the tell() functions returns the current position within the files in bytes. 
#     #This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position .

#     data = f.read(5)
#     print(data)

with open('sample.txt' , 'w') as f:
    f.write('Hello World ')
    f.truncate(5)#due to this the output is printing "hello" only.
with open('sample.txt' , 'r') as f :
        print(f.read())
    
