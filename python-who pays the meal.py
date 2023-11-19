names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random
length=len(names)
random_number=random.randint(0,length-1)
print(f"{names[random_number]} is going to buy the meal today!")