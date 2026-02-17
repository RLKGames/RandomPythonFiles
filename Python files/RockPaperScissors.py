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
        time.sleep(0.01)
    print()

# one by one character printer with input
def LBLInput(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.01)
    output = input()
    return output

# quit program
def quitProgram():
        LBL("\nQuitting...")
        quit()

# wait
def wait():
    time.sleep(0.3)

# rock paper scissors
def rps():
    com1 = random.randint(1,3)
    p1 = LBLInput("Choose rock paper or scissors ")
    # rock
    if p1 == "1" or p1 == "r" or p1 == "rock":
        LBL("You chose rock")
        match com1:
            case 1:
                wait()
                LBL("The computer chose rock")
                wait()
                LBL("You drew!")
            case 2:
                wait()
                LBL("The computer chose paper")
                wait()
                LBL("You lost!")
            case 3:
                wait()
                LBL("The computer chose scissors")
                wait()
                LBL("You won!")
            case _:
                errorPrint(2)
    # paper
    elif p1 == "2" or p1 == "p" or p1 == "paper":
        LBL("You chose paper")
        match com1:
            case 1:
                wait()
                LBL("The computer chose rock")
                wait()
                LBL("You won!")
            case 2:
                wait()
                LBL("The computer chose paper")
                wait()
                LBL("You drew!")
            case 3:
                wait()
                LBL("The computer chose scissors")
                wait()
                LBL("You lost!")
            case _:
                errorPrint(2)
    # scissors
    elif p1 == "3" or p1 == "s" or p1 == "scissors":
        LBL("You chose scissors")
        match com1:
            case 1:
                wait()
                LBL("The computer chose rock")
                wait()
                LBL("You lost!")
            case 2:
                wait()
                LBL("The computer chose paper")
                wait()
                LBL("You won!")
            case 3:
                wait()
                LBL("The computer chose scissors")
                wait()
                LBL("You drew!")
            case _:
                errorPrint(2)
    else:
        errorPrint(3)

# run again prompt
def runAgain():
    runAgainQ = LBLInput("Would you like to play again? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        rps()
    else:
        quitProgram()

# main code
rps()