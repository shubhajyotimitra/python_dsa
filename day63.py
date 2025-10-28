# Snake water gun game solution day53.py
user = int(input("Enter 0 for Snake, 1 for Water, 2 for Gun: \n"))
import random
comp = random.randint(0, 2) 
def check(comp, user):
    if comp == user:
        return None
    # Snake cases
    elif comp == 0:
        if user == 1:
            return False
        elif user == 2:
            return True
    # Water cases
    elif comp == 1:
        if user == 2:
            return False
        elif user == 0:
            return True
    # Gun cases
    elif comp == 2:
        if user == 0:
            return False
        elif user == 1:
            return True
score = check(comp, user)
print("you:" , user)
print("comp:" , comp)
if score == None:
    print("The game is a tie!")
elif score:
    print("You win!")
else:
    print("You lose!")      