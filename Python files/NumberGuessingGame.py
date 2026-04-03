import random
import sys
import time

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
    LBL("\nQuitting program!")
    quit()

# number guessing game
def numGuess():
    correct = False
    attempts = 0
    highestNum = LBLIntInput("What should the highest number be? ")
    if highestNum <= 1:
        LBL("The number has to be more than 1")
        numGuess()
    num = random.randint(1,highestNum)
    while correct == False:
        guess = LBLIntInput(f"\nEnter a guess between 1 and {highestNum} ")
        attempts += 1
        if guess > num:
            LBL("Too high")
        elif guess < num:
            LBL("Too low")
        elif guess == num:
            LBL("Correct!")
            LBL(f"You took {attempts} attempts to guess a random number between 1 and {highestNum}")
            correct = True
    mainMenu()

def mainMenu():
    LBL("""Welcome to my number guessing game!
Main Menu:
P) Play
I) Info
Q) Quit\n""")
    menu = LBLInput("Chose from options P, I or Q: ").upper()
    if menu == "P":
        numGuess()
    elif menu == "I":
        LBL("Not finished yet!")
    elif menu == "Q":
        quitProgram()
    mainMenu()

# main code
mainMenu()