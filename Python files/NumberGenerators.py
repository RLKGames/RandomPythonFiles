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

num = 0
startTime = 0

while running == True:

    LBL("""
Main Menu:
    1) Prime number generator
    2) Exponent generator
    3) Number factors generator
    4) Random number generator
    5) Quit
    """)
    mainMenu = LBLIntInput("Chose from options 1, 2, 3, 4 and 5: ")
    dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    if mainMenu == 1:
        LBL("\n\nPrime number generator:")
        filePath = "PrimeNumberGeneratorOutput-" + str(dateTimeNow) + ".txt"
        lowestNum = LBLIntInput("What is the lowest number you would like to check? ")
        highestNum = LBLIntInput("What is the highest number you would like to check? ")
        startTime = time.perf_counter()
        f = open(filePath, "a")
        num = 0
        for numChecking in range(lowestNum, highestNum + 1):
            factorCount = 0
            for numAgainst in range(1, numChecking + 1):
                if numChecking % numAgainst == 0:
                    factorCount += 1
            if factorCount == 2:
                num += 1
                print(str(numChecking) + " is prime")
                f.write(str(numChecking) + " is prime" + "\n")
        print(str(num) + " numbers have been generated")
        f.write(str(num) + " numbers have been generated")

    elif mainMenu == 2:
        LBL("\n\nExponent generator")
        LBL("(I'm gonna be honest, the phrasing of this entire exponent generator is terrible because I don't know how to phrase it properly)")
        exponentNum = LBLIntInput("Enter the exponent as a number (e.g. 2, 3, 4, etc etc) ")
        LBL("\nPower of " + str(exponentNum) + " generator:")
        filePath = "PowerOf" + str(exponentNum) + "GeneratorOutput-" + str(dateTimeNow) + ".txt"
        lowestNum = LBLIntInput("What is the lowest number in the range you would like to check? ")
        highestNum = LBLIntInput("What is the highest number in the range you would like to check? ")
        startTime = time.perf_counter()
        num = 0
        f = open(filePath, "a")
        for numChecking in range(lowestNum, highestNum + 1):
            squareRoot = numChecking ** (1/exponentNum)
            if squareRoot.is_integer() == True:
                num += 1
                print(str(numChecking) + " is an integer which can be gotten from raising another integer to the power of " + str(exponentNum))
                f.write(str(numChecking) + " is an integer which can be gotten from raising another integer to the power of " + str(exponentNum) + "\n")
        print(str(num) + " numbers have been generated")
        f.write(str(num) + " numbers have been generated")

    elif mainMenu == 3:
        LBL("\n\nNumber factor generator:")
        filePath = "NumberFactorsGeneratorOutput-" + str(dateTimeNow) + ".txt"
        numChecking = LBLIntInput("What number would you like to check? ")
        startTime = time.perf_counter()
        f = open(filePath, "a")
        for numAgainst in range(1, numChecking + 1):
            if numChecking % numAgainst == 0:
                num += 1
                print(str(numAgainst) + " is a factor of " + str(numChecking))
                f.write(str(numAgainst) + " is a factor of " + str(numChecking) + "\n")
        print(str(num) + " numbers have been generated")
        f.write(str(num) + " numbers have been generated")

    elif mainMenu == 4:
        LBL("\n\nRandom number generator:")
        filePath = "RandomNumberGeneratorOutput-" + str(dateTimeNow) + ".txt"
        lowestNum = LBLIntInput("What is the lowest number in the range? ")
        highestNum = LBLIntInput("What is the highest number in the range? ")
        f = open(filePath, "a")
        randNum = random.randint(lowestNum,highestNum)
        print("\nThe random number generated is " + str(randNum))
        f.write("The random number generated is " + str(randNum))

    elif mainMenu == 5:
        LBL("\nOk, quitting\n")
        quit()

    if startTime != 0:
        endTime = time.perf_counter()
        timeElapsed = round(endTime - startTime,2)
        LBL("\nTime taken: " + str(timeElapsed) + "s")
        f.write("Time taken: " + str(timeElapsed) + "s")

    f.close()

    runAgainQ = LBLInput("Would you like to go back to the main menu? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        running = True
        LBL("\n\n\n\n")
    else:
        running = False
        LBL("\nOk, quitting\n")