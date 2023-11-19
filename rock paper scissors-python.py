rock="oo"
paper="O"
scissor="m"
options=[rock,paper,scissor]
import random

me=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(options[me])
computer=random.randint(0,2)
print(options[computer])

if computer==me:
    print("you are even, try again")



elif computer==0:
    if me==1:
        print("you win")
    else:
        print("you lost")
elif computer==1:
    if me==2:
        print("you win")
    else:
        print("you lost")
else:
    if me==0:
        print("you win")
    else:
        print("you lost")
        

