import os
folders = os.listdir("data")
print(folders)

#this will tell how many folders it is consisting
# for folders in folders:
#     print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))

# print(os.getcwd()) displays the current working directory, i.e., the folder path where your Python program is being executed.
# also os.chdir("/users") changes the program’s current working directory to the specified path (/users) — allowing your code to read, write, or create files in that location.
#the program will look like this:

# import os
# print("Before:", os.getcwd())
# os.chdir("/users")
# print("After:", os.getcwd())



