import sys
import time
import datetime

# error printer
def errorPrint(errorID):
    f = open("Python files/Additional files/ErrorCodes.txt")
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

# quit program
def quitProgram():
    LBL("\nQuitting")
    quit()

# print output to file
def printToFile(dateTimeNow, output):
    print(output)
    filePath = f"incrementalCounterOutput-{dateTimeNow}.txt"
    with open(filePath, "a") as f:
        f.write(f"{output}\n")

# main menu
def counter():
    dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    count = 0
    increment = ""
    while increment == "":
        increment = input("Press enter to increment counter, type anything to finish ")
        if increment == "":
            count += 1
            print(f"Counter: {count}")
    printToFile(dateTimeNow, f"Final counter: {count}\n")
    runAgain()

# run again prompt
def runAgain():
    runAgainQ = LBLInput("Would you like to run the counter again? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        print()
        counter()
    else:
        quitProgram()

# main code
counter()