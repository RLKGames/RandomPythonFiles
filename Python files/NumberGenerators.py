import datetime
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

# print output to file
def printToFile(dateTimeNow, generator, output):
    print(output)
    match generator:
        case "prime":
            filePath = f"PrimeNumGenOutput-{dateTimeNow}.txt"
        case "exponentOf":
            filePath = f"ExponentOfNumGenOutput-{dateTimeNow}.txt"
        case "exponent":
            filePath = f"ExponentNumGenOutput-{dateTimeNow}.txt"
        case "factors":
            filePath = f"NumFactorGenOutput-{dateTimeNow}.txt"
        case "random":
            filePath = f"RandomNumGenOutput-{dateTimeNow}.txt"

    with open(filePath, "a") as f:
        f.write(f"{output}\n")


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
        output = "2 is prime"
        printToFile(dateTimeNow, "prime", output)
    if lowestNum <= 3 and highestNum >= 3:
        num += 1
        output = "3 is prime"
        printToFile(dateTimeNow, "prime", output)
    for numChecking in range(lowestNum, highestNum + 1, 2):
        factorCount = 2
        if numChecking % 2 != 0 and numChecking > 3:
            for numAgainst in range(2, int((numChecking+1)/2)+2):
                if numChecking % numAgainst == 0:
                    factorCount += 1
            if factorCount == 2:
                num += 1
                output = f"{numChecking} is prime"
                printToFile(dateTimeNow, "prime", output)
    endTime = time.perf_counter()
    output = f"{num} numbers have been generated\nTook: {endTime - startTime:.2f}s"
    printToFile(dateTimeNow, "prime", output)

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
        output = f"{answer} is gotten when raising {numChecking} to the power of {num}"
        printToFile(dateTimeNow, "exponentOf", output)
    endTime = time.perf_counter()
    output = f"Took: {endTime - startTime:.2f}s"
    printToFile(dateTimeNow, "exponentOf", output)

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

    for numChecking in range(lowestNum, highestNum + 1):
        # print("numChecking = " + str(numChecking)) # debug only
        root = round(numChecking ** (1/exponent), 8)
        # print("root = " + str(root)) # debug only
        if root.is_integer() == True:
            num += 1
            output = f"{numChecking} is an integer which can be gotten from raising another integer to the power of {exponent}"
            printToFile(dateTimeNow, "exponent", output)
    
    endTime = time.perf_counter()
    output = f"{num} numbers have been generated\nTook: {endTime - startTime:.2f}s"
    printToFile(dateTimeNow, "exponent", output)

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
            output = f"{numAgainst} is a factor of {numChecking}"
            printToFile(dateTimeNow, "factors", output)
    output = f"{numChecking} is a factor of {numChecking}"
    printToFile(dateTimeNow, "factors", output)
    
    endTime = time.perf_counter()
    output = f"{num} numbers have been generated\nTook: {endTime - startTime:.2f}s"
    printToFile(dateTimeNow, "factors", output)

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
        output = f"Random number {num} is {randNum}"
        printToFile(dateTimeNow, "random", output)
    endTime = time.perf_counter()
    output = f"{num} numbers have been generated\nTook: {endTime - startTime:.2f}s"
    printToFile(dateTimeNow, "random", output)

# quit program
def quitProgram():
    LBL("\nQuitting")
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
    6) Quit
""")
    mainMenu = LBLIntInput("Chose from options 1, 2, 3, 4, 5 and 6: ")
    if mainMenu == 1:
        primeNumberGen()

    elif mainMenu == 2:
        exponentOfNumGen()

    elif mainMenu == 3:
        exponentNumGen()

    elif mainMenu == 4:
        numberFactorsGen()

    elif mainMenu == 5:
        randomNumGen()

    elif mainMenu == 6:
        quitProgram()

    runAgain()

# run again prompt
def runAgain():
    runAgainQ = LBLInput("Would you like to go back to the main menu? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        mainMenu()
    else:
        quitProgram()

# main code
mainMenu()