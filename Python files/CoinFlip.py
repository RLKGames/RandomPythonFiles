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
    filePath = f"CoinFlipOutput-{dateTimeNow}.txt"
    with open(filePath, "a") as f:
        f.write(f"{outputList}")

# coin flipper
def coinFlip():
    dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    diceCount = LBLIntInput("How many coins should be flipped? ")
    count = 0
    heads = 0
    tails = 0
    startTime = time.perf_counter()
    for i in range(0, diceCount):
        coinFlip = random.randint(1, 2)
        count += 1
        if coinFlip == 1:
            printOutput(f"Coin number {count} landed on heads")
            heads += 1
        elif coinFlip == 2:
            printOutput(f"Coin number {count} landed on tails")
            tails += 1
    endTime = time.perf_counter()
    printOutput(f"{heads} coins landed on heads")
    printOutput(f"{tails} coins landed on tails")
    printOutput(f"Took: {endTime - startTime:.2f}s")
    printToFile(dateTimeNow)
    mainMenu()

def mainMenu():
    LBL("""Welcome to my coin flipper!
Main Menu:
P) Play
I) Info
Q) Quit\n""")
    menu = LBLInput("Chose from options P, I or Q: ").upper()
    if menu == "P":
        coinFlip()
    elif menu == "I":
        LBL("Not finished yet!")
    elif menu == "Q":
        quitProgram()
    mainMenu()

# main code
mainMenu()