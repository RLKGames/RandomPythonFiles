import random
import sys
import time

# error printer
def errorPrint(errorID):
    f = open("Python files/ErrorCodes.txt")
    errorPrint = f.readlines(errorID).replace("[", "").replace("]", "").replace("\\n", "").replace("'", "")
    f.readlines(errorID)

# one by one character printer
def LBL(printInput):
    for x in str(printInput):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    print()

# one by one character printer with input
def LBLInput(printInput):
    for x in str(printInput):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = input()
    return output

# one by one character printer with integer input
def LBLIntInput(printInput):
    for x in str(printInput):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = int(input())
    return output

# quit program
def quitProgram():
    LBL("\nQuitting")
    quit()

# number guessing game
def numGuess():
    correct = False
    LBL("Welcome to number guessing game!")
    highestNum = LBLIntInput("What should the highest number be? ")
    if highestNum <= 1:
        LBL("The number has to be more than 1")
        quit()
    num = random.randint(1,highestNum)

    while correct == False:
        correct = guessNum(highestNum, num)
    runAgain()

# guess numbers
def guessNum(highestNum, num):
    correct = False
    attempts = 0
    # print("num = " + str(num)) # debug only
    guess = LBLIntInput("\nEnter a guess between 1 and " + str(highestNum) + " ")
    attempts += 1

    if guess > num:
        LBL("Too high")
    elif guess < num:
        LBL("Too low")
    elif guess == num:
        LBL("Correct!")
        LBL("You took " + str(attempts) + " attempts to guess a random number between 1 and " + str(highestNum))
        correct = True
    else:
        errorPrint(1)
    return correct

# run again prompt
def runAgain():
    runAgainQ = LBLInput("Would you like to play again? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        numGuess()
    else:
        quitProgram()

# main code
numGuess()