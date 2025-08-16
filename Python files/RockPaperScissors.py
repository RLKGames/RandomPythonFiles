import random
import sys
import time

def LBL(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    print()

def LBLInput(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = input()
    return output

def LBLIntInput(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = int(input())
    return output

ERRORCODE1 = "Error code 1: The computer somehow didn't chose rock, paper or scissors. Please report this as a bug at https://github.com/RLKGames/RandomPythonFiles/issues"
ERRORCODE2 = "Error code 2: You didn't chose rock, paper or scissors. If you did chose rock, paper or scissors then please report this as a bug at https://github.com/RLKGames/RandomPythonFiles/issues"

running = True

while running == True:
    com1 = random.randint(1,3)
    p1 = LBLInput("Choose rock paper or scissors ")
    if p1 == "1" or p1 == "r" or p1 == "rock":
        LBL("You chose rock")
        match com1:
            case 1:
                LBL("The computer chose rock")
                LBL("You drew!")
            case 2:
                LBL("The computer chose paper")
                LBL("You lost!")
            case 3:
                LBL("The computer chose scissors")
                LBL("You won!")
            case _:
                LBL(ERRORCODE1)

    elif p1 == "2" or p1 == "p" or p1 == "paper":
        LBL("You chose paper")
        match com1:
            case 1:
                LBL("The computer chose rock")
                LBL("You won!")
            case 2:
                LBL("The computer chose paper")
                LBL("You drew!")
            case 3:
                LBL("The computer chose scissors")
                LBL("You lost!")
            case _:
                LBL(ERRORCODE1)

    elif p1 == "3" or p1 == "s" or p1 == "scissors":
        LBL("You chose scissors")
        match com1:
            case 1:
                LBL("The computer chose rock")
                LBL("You lost!")
            case 2:
                LBL("The computer chose paper")
                LBL("You won!")
            case 3:
                LBL("The computer chose scissors")
                LBL("You drew!")
            case _:
                LBL(ERRORCODE1)

    else:
        LBL(ERRORCODE2)


    runAgainQ = LBLInput("\n\nWould you like to play again? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        running = True
        print("\n\n\n\n\n\n\n\n\n\n\n")
    else:
        running = False
        LBL("\nOk, quitting\n")