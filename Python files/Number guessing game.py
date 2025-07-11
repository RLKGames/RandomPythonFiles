import random

attempts = 0
correct = False
highestNum = int(input("What should be the highest number? "))
if highestNum <= 1:
    print("The number has to be more than 1")
    quit()
num = random.randint(1,highestNum)

while correct == False:
    guess = int(input("\nEnter a guess between 1 and " + str(highestNum) + " "))
    attempts += 1
    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    elif guess == num:
        print("Correct!")
        print("You took " + str(attempts) + " attempts to guess a number between 1 and "+ str(highestNum))
        correct = True
    else:
        print("If this message appears then please report this as a bug at https://github.com/RLKGames/RandomPythonFiles/issues")