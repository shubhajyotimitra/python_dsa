#exercise solution day-38

st= input("Enter message: ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if coding =="1" else False

if (coding):
    nwords = []
    for word in words:
     if(len(word)>=3):
        r1="dsf"
        r2="jkr"
        stnew = r1+ word[1:]+ word[0] +r2
        nwords.append(stnew)
     else:
        nwords.append(word[::-1])
    print(" ".join(nwords))
   

else:
    nwords = []
    for word in words:
     if(len(word)>=3):
        stnew = word[3:-3]
        stnew = stnew[-1]+stnew[:-1]
        nwords.append(stnew)
     else:
        nwords.append(word[::-1])
    print(" ".join(nwords))
   

#how to convert this into randow variable 
import random
import string

st = input("Enter message: ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if coding == "1" else False

# Function to generate random 3-letter strings:
def random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choices(letters, k=3))

if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = random_string()
            r2 = random_string()
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
