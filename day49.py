#seek(), tell() and other functions
with open('file.txt' , 'r') as f:
    print(type(f))
    #Move to the 10th byte in the file
    f.seek(10)

    #read the next 5 bytes
    data = f.read(5)
    print(data)
