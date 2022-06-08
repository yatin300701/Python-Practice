#################### Game: Guess the number  ############
import random
import os

ranNum = random.randint(1, 10)
chances = 3
n = -1

# loop to check chances left
# and
# compare with random number
while (n != ranNum) and (chances != 0):
    # os.system('cls')
    n = int(input("Type the number \n"))
    if(n > ranNum):
        print(f"No is smaller than {n}")
    elif n == ranNum:
        print("You Won")
        break
    else:
        print(f"Actual no is greater than {n}")
    chances -= 1
    input("\nPress Enter to continue")


if(chances == 0):
    print("You Loose")
