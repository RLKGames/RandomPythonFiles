import datetime
import time

errorCode1 = "Error code 1: If this message appears then please report this as a bug at https://github.com/RLKGames/RandomPythonFiles/issues"
startTime = 0

print("""Main Menu:
1) Prime number generator
2) Exponent generator
3) Number factors generator
4) Quit
""")

mainMenu = int(input("Chose from options 1, 2, 3, 4 and 5: "))

dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

if mainMenu == 1:
    print("\n\nPrime number generator:")
    filePath = "PrimeNumberGeneratorOutput-" + str(dateTimeNow) + ".txt"
    lowestNum = int(input("What is the lowest number you would like to check? "))
    highestNum = int(input("What is the highest number you would like to check? "))
    startTime = time.perf_counter()
    f = open(filePath, "a")
    for numChecking in range(lowestNum, highestNum + 1):
        factorCount = 0
        for numAgainst in range(1, numChecking + 1):
            if numChecking % numAgainst == 0:
                factorCount += 1
        if factorCount == 2:
            output = str(numChecking) + " is prime"
        else:
            output = str(numChecking) + " is not prime"
        print(output)
        f.write(output + "\n")

elif mainMenu == 2:
    print("Exponent generator")
    print("\n\nI'm gonna be honest, the phrasing of this entire exponent generator is terrible because I don't know how to phrase it properly")
    exponentNum = int(input("Enter the exponent as a number (e.g. 2, 3, 4, etc etc) "))
    print("\nPower of " + str(exponentNum) + " generator:")
    filePath = "PowerOf" + str(exponentNum) + "GeneratorOutput-" + str(dateTimeNow) + ".txt"
    lowestNum = int(input("What is the lowest number you would like to check? "))
    highestNum = int(input("What is the highest number you would like to check? "))
    startTime = time.perf_counter()
    f = open(filePath, "a")
    for numChecking in range(lowestNum, highestNum + 1):
        if int(round(numChecking ** (1/exponentNum), 0)) == round(numChecking ** (1/exponentNum),2):
            output = str(numChecking) + " IS an integer which can be gotten from raising another integer to the power of " + str(exponentNum)
        else:
            output = str(numChecking) + " is NOT an integer which can be gotten from raising another integer to the power of " + str(exponentNum)
        print(output)
        f.write(output + "\n")

elif mainMenu == 3:
    print("\n\nNumber factor generator:")
    filePath = "NumberFactorsGeneratorOutput-" + str(dateTimeNow) + ".txt"
    numChecking = int(input("What number would you like to check? "))
    startTime = time.perf_counter()
    f = open(filePath, "a")
    for numAgainst in range(1, numChecking + 1):
        if numChecking % numAgainst == 0:
            output = str(numAgainst) + " is a factor of " + str(numChecking)
        else:
            output = str(numAgainst) + " is not a factor of " + str(numChecking)
        print(output)
        f.write(output + "\n")

elif mainMenu == 4:
    print("\nOk, quitting\n")
    quit()


if startTime != 0:
    endTime = time.perf_counter()
    timeElapsed = round(endTime - startTime,2)
    print("\nTime taken: " + str(timeElapsed) + "s")
    f.write("Time taken: " + str(timeElapsed) + "s")
else:
    print(errorCode1)

f.close()