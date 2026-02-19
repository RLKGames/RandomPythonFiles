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
    filePath = f"CoinFlipOutput-{dateTimeNow}.txt"
    with open(filePath, "a") as f:
        f.write(f"{output}\n")

# coin
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
            output = f"Coin number {count} landed on heads"
            printToFile(dateTimeNow, output)
            heads += 1
        elif coinFlip == 2:
            output = f"Coin number {count} landed on tails"
            printToFile(dateTimeNow, output)
            tails += 1

    output = f"{heads} coins landed on heads"
    printToFile(dateTimeNow, output)
    output = f"{tails} coins landed on tails"
    printToFile(dateTimeNow, output)

    endTime = time.perf_counter()
    output = f"Took: {endTime - startTime:.2f}s"
    printToFile(dateTimeNow, output)

    runAgain()

# run again prompt
def runAgain():
    runAgainQ = LBLInput("\n\nWould you like to flip coins again? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        coinFlip()
    else:
        quitProgram()

# main block
coinFlip()