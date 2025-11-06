# Clear clutter problem solving day-66
import os 

files = os.listdir("cluttered")
i = 1
for file in files:
    if file.endswith(".png"):
     print(file)
os.rename(f"cluttered/{file}" , f"cluttered/{i}.png")
i = i+1