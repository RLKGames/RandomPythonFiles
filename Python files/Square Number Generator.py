import datetime
import time

highestNum = 0
numChecking = 0
numAgainst = 0
startTime = 0

dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
filePath = "SquareNumberGeneratorOutput-" + str(dateTimeNow)
filePath2 = filePath + ".txt"
filePath2 = filePath2.replace(":","-")
filePath2 = filePath2.replace(" ","-")

with open(filePath2,"a") as f:
    lowestNum = int(input("What is the lowest number you would like to check? "))
    highestNum = int(input("What is the highest number you would like to check? "))
    startTime = time.perf_counter()
    for numChecking in range(lowestNum,highestNum+1):
        numAgainst = 0
        for numAgainst in range(1,numChecking+1):
            if numChecking / numAgainst == numAgainst:
                output = str(numChecking) + " is a square number"
            else:
                output = str(numChecking) + " is not a square number"
        print(output)
        f.write(output + "\n")
    endTime = time.perf_counter()
    timeElapsed = endTime - startTime
    timeElapsed = round(timeElapsed,2)
    print("Time taken: " + str(timeElapsed) + "s")
    f.write("Time taken: " + str(timeElapsed) + "s")