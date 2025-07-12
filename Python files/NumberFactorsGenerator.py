import datetime
import time

dateTimeNow = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
filePath = "NumberFactorsGeneratorOutput-" + str(dateTimeNow) + ".txt"

with open(filePath,"a") as f:
    lowestNum = int(input("What number would you like to check? "))
    startTime = time.perf_counter()
    for numChecking in range(1,lowestNum+1):
        if lowestNum % numChecking == 0:
            output = str(numChecking) + " is a factor of " + str(lowestNum)
        else:
            output = str(numChecking) + " is not a factor of " + str(lowestNum)
        print(output)
        f.write(output + "\n")
    endTime = time.perf_counter()
    timeElapsed = round(endTime - startTime,2)
    print("Time taken: " + str(timeElapsed) + "s")
    f.write("Time taken: " + str(timeElapsed) + "s")