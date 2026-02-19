import datetime
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
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    print()

# one by one character printer with input
def LBLInput(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = input()
    return output

# one by one character printer with integer input
def LBLIntInput(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = int(input())
    return output

# quit program
def quitProgram():
        LBL("\nQuitting\n")
        quit()

# print output to file
def printToFile(dateTimeNow, output):
    print(output)
    filePath = f"DiceRollOutput-{dateTimeNow}.txt"
    with open(filePath, "a") as f:
        f.write(f"{output}\n")

# dice
def diceRoll():
    dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    diceSides = LBLIntInput("How many sides should the dice have? ")
    diceCount = LBLIntInput("How many dice should be rolled? ")
    count = 0
    startTime = time.perf_counter()
    for i in range(0, diceCount):
        diceRoll = random.randint(0, diceSides-1)
        count += 1
        output = f"Dice number {count} rolled {diceRoll}"
        printToFile(dateTimeNow, output)

    endTime = time.perf_counter()
    output = f"Took: {endTime - startTime:.2f}s"
    printToFile(dateTimeNow, output)

    runAgain()

# run again prompt
def runAgain():
    runAgainQ = LBLInput("\n\nWould you like to roll dice again? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        diceRoll()
    else:
        quitProgram()

# main block
diceRoll()