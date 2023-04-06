#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

# input("Input number between '1' and '0'. ")

heads = random.randint(0, 1)

if heads == 0:
    print("Heads")
else:
    print("Tails")
