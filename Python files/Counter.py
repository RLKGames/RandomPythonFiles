import sys
import time
import datetime

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
    filePath = f"CounterOutput-{dateTimeNow}.txt"
    with open(filePath, "a") as f:
        f.write(outputList)

# main menu
def counter():
    dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    count = 0
    increment = ""
    while increment == "":
        increment = input("Press enter to increment counter, type anything to finish ")
        if increment == "":
            count += 1
            printOutput(f"Counter: {count}")
    printOutput(f"Final counter: {count}")
    printToFile(dateTimeNow)
    mainMenu()

def mainMenu():
    LBL("""Welcome to my counter!
Main Menu:
P) Play
I) Info
Q) Quit\n""")
    menu = LBLInput("Chose from options P, I or Q: ").upper()
    if menu == "P":
        counter()
    elif menu == "I":
        LBL("Not finished yet!")
    elif menu == "Q":
        quitProgram()
    mainMenu()

# main code
mainMenu()