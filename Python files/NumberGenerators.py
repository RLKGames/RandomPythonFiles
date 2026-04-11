import datetime
import random
import sys
import time
import math

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

# one by one character printer with integer input
def LBLIntInput(printInput):
    for x in str(printInput):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = int(input())
    return output

# print output
def printOutput(output):
    print(output)
    outputList.append(output)

# print output to file
def printToFile(dateTimeNow, generator):
    match generator:
        case "prime":
            filePath = f"PrimeNumGenOutput-{dateTimeNow}.txt"
        case "exponentof":
            filePath = f"ExponentOfNumGenOutput-{dateTimeNow}.txt"
        case "exponent":
            filePath = f"ExponentNumGenOutput-{dateTimeNow}.txt"
        case "factors":
            filePath = f"NumFactorGenOutput-{dateTimeNow}.txt"
        case "random":
            filePath = f"RandomNumGenOutput-{dateTimeNow}.txt"
    with open(filePath, "a") as f:
        f.write(f"{outputList}")

# prime number generator
def primeNumberGen():
    dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    LBL("\n\nPrime number generator:")
    lowestNum = LBLIntInput("\nWhat is the lowest number you would like to check? ")
    highestNum = LBLIntInput("What is the highest number you would like to check? ")
    num = 0
    startTime = time.perf_counter()
    if lowestNum <= 2 and highestNum >= 2:
        num += 1
        printOutput("2 is prime")
    if lowestNum <= 3 and highestNum >= 3:
        num += 1
        printOutput("3 is prime")
    for numChecking in range(max(5, lowestNum if lowestNum % 2 != 0 else lowestNum + 1), highestNum + 1, 2):
        factorCount = 0
        for numAgainst in range(2, int(math.sqrt(numChecking+1)+2)):
            if numChecking % numAgainst == 0:
                factorCount += 1
        if factorCount == 2:
            num += 1
            printOutput(f"{numChecking} is prime")
    endTime = time.perf_counter()
    printOutput(f"{num} numbers have been generated\nTook: {endTime - startTime:.2f}s")
    printToFile(dateTimeNow, "prime")

# exponent of a number generator
def exponentOfNumGen():
    dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    LBL("\n\nExponent of a number generator")
    LBL("Being honest, the phrasing of this generator is terrible. If a mathematician wants to help me, that'd be appreciated!")
    numChecking = LBLIntInput("What number would you like to check? ")
    maxExponent = LBLIntInput("What exponent would you like to go up to? ")
    num = 1
    answer = numChecking
    startTime = time.perf_counter()
    for i in range(1, maxExponent):
        answer = answer * numChecking
        num += 1
        printOutput(f"{answer} is gotten when raising {numChecking} to the power of {num}")
    endTime = time.perf_counter()
    printOutput(f"{num} numbers have been generated\nTook: {endTime - startTime:.2f}s")
    printToFile(dateTimeNow, "exponentof")

# exponent number generator
def exponentNumGen():
    dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    LBL("\n\nExponent number generator")
    LBL("Being honest, the phrasing of this generator is terrible. If a mathematician wants to help me, that'd be appreciated!")
    exponent = LBLIntInput("Enter the exponent as a number (e.g. 2, 3, 4, etc etc) ")
    LBL(f"\nPower of {exponent} generator:")
    lowestNum = LBLIntInput("What is the lowest number in the range you would like to check? ")
    highestNum = LBLIntInput("What is the highest number in the range you would like to check? ")
    num = 0
    startTime = time.perf_counter()
    for numChecking in range(lowestNum, highestNum+1):
        root = round(numChecking ** (1/exponent), 8)
        if root.is_integer() == True:
            num += 1
            printOutput(f"{numChecking} is an integer which can be gotten from raising another integer to the power of {exponent}")
    endTime = time.perf_counter()
    printOutput(f"{num} numbers have been generated\nTook: {endTime - startTime:.2f}s")
    printToFile(dateTimeNow, "exponent")

# number factors generator
def numberFactorsGen():
    dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    LBL("\n\nNumber factor generator:")
    numChecking = LBLIntInput("What number would you like to check? ")
    num = 1
    startTime = time.perf_counter()
    for numAgainst in range(1, int(round((numChecking+1)/2))+1):
        if numChecking % numAgainst == 0:
            num += 1
            printOutput(f"{numAgainst} is a factor of {numChecking}")
    endTime = time.perf_counter()
    printOutput(f"{num} numbers have been generated\nTook: {endTime - startTime:.2f}s")
    printToFile(dateTimeNow, "factors")

# random number generator
def randomNumGen():
    dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    LBL("\n\nRandom number generator:")
    lowestNum = LBLIntInput("What is the lowest number in the range? ")
    highestNum = LBLIntInput("What is the highest number in the range? ")
    genNum = LBLIntInput("How many numbers would you like to generate? ")
    num = 0
    startTime = time.perf_counter()
    for i in range(1, genNum+1):
        num += 1
        randNum = random.randint(lowestNum, highestNum)
        printOutput(f"Random number {num} is {randNum}")
    endTime = time.perf_counter()
    printOutput(f"{num} numbers have been generated\nTook: {endTime - startTime:.2f}s")
    printToFile(dateTimeNow, "random")

# quit program
def quitProgram():
    LBL("\nQuitting program!")
    quit()

# main menu
def mainMenu():
    LBL("""Welcome to number generator!
Main Menu:
1) Prime number generator
2) Exponent of number generator
3) Exponent number generator
4) Number factors generator
5) Random number generator
I) Info
Q) Quit\n""")
    menu = LBLInput("Chose from options 1-5, I or Q: ").lower()
    if menu == "1":
        primeNumberGen()
    elif menu == "2":
        exponentOfNumGen()
    elif menu == "3":
        exponentNumGen()
    elif menu == "4":
        numberFactorsGen()
    elif menu == "5":
        randomNumGen()
    elif menu == "I":
        LBL("Not finished yet!")
    elif menu == "Q":
        quitProgram()
    mainMenu()

# main code
mainMenu()