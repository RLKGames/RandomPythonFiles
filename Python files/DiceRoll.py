import datetime
import random
import sys
import time

outputList = []

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

# print output
def printOutput(output):
    print(output)
    outputList.append(output)

# print output to file
def printToFile(dateTimeNow):
    filePath = f"DiceRollOutput-{dateTimeNow}.txt"
    with open(filePath, "a") as f:
        f.write(outputList)

# dice roller
def diceRoll():
    dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    diceSides = LBLIntInput("How many sides should the dice have? ")
    diceCount = LBLIntInput("How many dice should be rolled? ")
    count = 0
    total = 0
    startTime = time.perf_counter()
    for i in range(0, diceCount):
        diceRoll = random.randint(1, diceSides)
        count += 1
        total += diceRoll
        printOutput(f"Dice number {count} rolled {diceRoll}")
    endTime = time.perf_counter()
    printOutput(f"{count} dice rolled\nThe average dice roll was: {total/count:.3f}\nTook: {endTime - startTime:.2f}s")
    printToFile(dateTimeNow)
    mainMenu()

def mainMenu():
    LBL("""Welcome to my dice roller!
Main Menu:
P) Play
I) Info
Q) Quit\n""")
    menu = LBLInput("Chose from options P, I or Q: ").upper()
    if menu == "P":
        diceRoll()
    elif menu == "I":
        LBL("Not finished yet!")
    elif menu == "Q":
        quitProgram()
    mainMenu()

# main code
mainMenu()