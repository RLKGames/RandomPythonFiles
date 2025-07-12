import datetime
import time
import math

dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
filePath = "CubeNumberGeneratorOutput-" + str(dateTimeNow) + ".txt"

lowestNum = int(input("What is the lowest number you would like to check? "))
highestNum = int(input("What is the highest number you would like to check? "))
startTime = time.perf_counter()

with open(filePath,"a") as f:
    for numChecking in range(lowestNum,highestNum+1):
        cuberoot = math.cbrt(numChecking)
        intcuberoot = int(cuberoot)
        if intcuberoot == cuberoot:
            output = str(numChecking) + " is a cube number"
        else:
            output = str(numChecking) + " is not a cube number"
        print(output)
        f.write(output + "\n")
    endTime = time.perf_counter()
    timeElapsed = round(endTime - startTime,2)
    print("Time taken: " + str(timeElapsed) + "s")
    f.write("Time taken: " + str(timeElapsed) + "s")