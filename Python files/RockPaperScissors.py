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

# quit program
def quitProgram():
    LBL("\nQuitting program!")
    quit()

# wait
def wait():
    time.sleep(0.3)

# rock paper scissors
def rps():
    com = random.randint(1,3)
    player = LBLInput("Choose rock, paper or scissors ")
    # rock
    if player == "r" or player == "rock":
        LBL("You chose rock")
        match com:
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
    # paper
    elif player == "p" or player == "paper":
        LBL("You chose paper")
        match com:
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
    # scissors
    elif player == "s" or player == "scissors":
        LBL("You chose scissors")
        match com:
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
    else:
        LBL("Please choose rock, paper or scissors!")
    mainMenu()

def mainMenu():
    LBL("""Welcome to rock paper scissors!
Main Menu:
P) Play
I) Info
Q) Quit\n""")
    menu = LBLInput("Chose from options P, I or Q: ").upper()
    if menu == "P":
        rps()
    elif menu == "I":
        LBL("Not finished yet!")
    elif menu == "Q":
        quitProgram()
    mainMenu()

# main code
mainMenu()