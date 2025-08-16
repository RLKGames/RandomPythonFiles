import random
import sys
import time

def LBL(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    print()

def LBLInput(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = input()
    return output

def LBLIntInput(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = int(input())
    return output

ERRORCODE1 = "Error code 1: If this message appears then please report this as a bug at https://github.com/RLKGames/RandomPythonFiles/issues"

correct = False
running = True
attempts = 0

while running == True:
    highestNum = int(input("What should the highest number be? "))
    if highestNum <= 1:
        print("The number has to be more than 1")
        quit()
    num = random.randint(1,highestNum)

    while correct == False:
        guess = int(input("\nEnter a guess between 1 and " + str(highestNum) + " "))
        attempts += 1
        if guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        elif guess == num:
            print("Correct!")
            print("You took " + str(attempts) + " attempts to guess a number between 1 and "+ str(highestNum))
            correct = True
        else:
            print(ERRORCODE1)

    runAgainQ = input("\n\nWould you like to play again? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        running = True
        print("\n\n\n\n")
    else:
        running = False
        print("\nOk, quitting\n")