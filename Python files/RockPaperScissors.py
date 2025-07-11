import random

com1 = random.randint(1,3)
p1 = input("Choose rock paper or scissors ")

if p1 == "1" or p1 == "r" or p1 == "rock":
    print("You chose rock")
    if com1 == 1:
        print("The computer chose rock")
        print("You drew!")
    elif com1 == 2:
        print("The computer chose paper")
        print("You lost!")
    elif com1 == 3:
        print("The computer chose scissors")
        print("You won!")
    else:
        print("The computer somehow didn't chose rock, paper or scissors. Please report this as a bug at https://github.com/RLKGames/RandomPythonFiles/issues")
elif p1 == "2" or p1 == "p" or p1 == "paper":
    print("You chose paper")
    if com1 == 1:
        print("The computer chose rock")
        print("You won!")
    elif com1 == 2:
        print("The computer chose paper")
        print("You drew!")
    elif com1 == 3:
        print("The computer chose scissors")
        print("You lost!")
    else:
        print("The computer somehow didn't chose rock, paper or scissors. Please report this as a bug at https://github.com/RLKGames/RandomPythonFiles/issues")
elif p1 == "3" or p1 == "s" or p1 == "scissors":
    print("You chose scissors")
    if com1 == 1:
        print("The computer chose rock")
        print("You lost!")
    elif com1 == 2:
        print("The computer chose paper")
        print("You won!")
    elif com1 == 3:
        print("The computer chose scissors")
        print("You drew!")
    else:
        print("The computer somehow didn't chose rock, paper or scissors. Please report this as a bug at https://github.com/RLKGames/RandomPythonFiles/issues")
else:
    print("You didn't chose rock, paper or scissors. If you did chose rock, paper or scissors then please report this as a bug at https://github.com/RLKGames/RandomPythonFiles/issues")