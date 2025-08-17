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

ERRORCODE1 = "Error code 1: If this message appears then please report this as a bug at https://github.com/RLKGames/RandomPythonFiles/issues"

running = True

dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
filePath = "PrimeNumberGeneratorOutput-" + str(dateTimeNow) + ".txt"
f = open(filePath, "a")


while running == True:
    diceCount = LBLIntInput("How many coins should I flip? ")
    count = 0

    for i in range(0, diceCount):
        coinFlip = random.randint(0, 1)
        count += 1
        match coinFlip:
            case 1:
                print("Coin number " + str(count) + " landed on heads")
            case 2:
                print("Coin number " + str(count) + " landed on tails")
            case _:
                print(ERRORCODE1)

    runAgainQ = input("\n\nWould you like to roll dice again? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        running = True
        print("\n\n\n\n\n\n\n\n\n\n\n")
    else:
        running = False
        LBL("\nOk, quitting\n")