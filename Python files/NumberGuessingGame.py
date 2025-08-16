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
    highestNum = LBLIntInput("What should the highest number be? ")
    if highestNum <= 1:
        LBL("The number has to be more than 1")
        quit()
    num = random.randint(1,highestNum)

    while correct == False:
        guess = LBLIntInput("\nEnter a guess between 1 and " + str(highestNum) + " ")
        attempts += 1
        if guess > num:
            LBL("Too high")
        elif guess < num:
            LBL("Too low")
        elif guess == num:
            LBL("Correct!")
            LBL("You took " + str(attempts) + " attempts to guess a number between 1 and "+ str(highestNum))
            correct = True
        else:
            LBL(ERRORCODE1)

    runAgainQ = LBLInput("\n\nWould you like to play again? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        running = True
        print("\n\n\n\n\n\n\n\n\n\n\n")
    else:
        running = False
        LBL("\nOk, quitting\n")