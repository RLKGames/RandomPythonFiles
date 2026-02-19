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

# quit program
def quitProgram():
    LBL("\nQuitting")
    quit()

# main menu
def counter():
    count = 0
    input = ""
    while input == "":
        input = input("Press enter to increment counter, type anything to finish ")
        if input == "":
            count += 1
            print(f"Counter: {count}")
    LBL(f"Final counter: {count}\n")
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