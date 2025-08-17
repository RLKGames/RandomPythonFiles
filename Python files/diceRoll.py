import datetime
import random
import sys
import time

def LBL(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    print()

def LBLFast(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.0005)
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

running = True

dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
filePath = "PrimeNumberGeneratorOutput-" + str(dateTimeNow) + ".txt"
f = open(filePath, "a")


while running == True:
    diceSides = LBLIntInput("How many sides should the dice have? ")
    diceCount = LBLIntInput("How many dice should I roll? ")
    count = 0

    for i in range(0,diceCount):
        diceRoll = random.randint(0,diceSides-1)
        count += 1
        print("Dice number "+str(count)+" rolled "+str(diceRoll+1))

    runAgainQ = input("\n\nWould you like to roll dice again? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        running = True
        print("\n\n\n\n\n\n\n\n\n\n\n")
    else:
        running = False
        LBL("\nOk, quitting\n")