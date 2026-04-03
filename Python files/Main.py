import sys
import time
import subprocess
import os

# one by one character printer
def LBL(printInput):
    for x in str(printInput):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    print()

# one by one character printer - quick
def LBLQuick(printInput):
    for x in str(printInput):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.001)
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

# run another python file
def runFile(file):
    currentDir = os.path.dirname(os.path.abspath(__file__))
    match file:
        case "NumGen":
            filePath = os.path.join(currentDir, "NumberGenerators.py")
        case "NumGuess":
            filePath = os.path.join(currentDir, "NumberGuessingGame.py")
        case "RPS":
            filePath = os.path.join(currentDir, "RockPaperScissors.py")
        case "CoinFlip":
            filePath = os.path.join(currentDir, "CoinFlip.py")
        case "DiceRoll":
            filePath = os.path.join(currentDir, "DiceRoll.py")
        case "UnitConvert":
            filePath = os.path.join(currentDir, "UnitConverter.py")
    print("\n\n\n\n")
    subprocess.run([sys.executable, filePath])

# quit program
def quitProgram():
    LBL("\nQuitting program!")
    quit()

# info print
def infoPrint():
    LBL("""\nInfo:
(1) NumberGenerators.py
- Prime number generator - generates all prime numbers in the range you specify
- Exponent of number generator - generates the number you specify multiplied by itself the specified amount of times
- Exponent number generator - generates all numbers in a range you that specify that can be gotten by raising an integer to the power that you specify
- Number factors generator - generates a list of all of the factors of a number
- Random number generator - generates a specified amount of random numbers in the range your specify

Others
- (2) NumberGuessingGame.py - guess a random number in a range you specify
- (3) RockPaperScissors.py - play rock paper scissors against a computer
- (4) CoinFlip.py - flip a specified number of coins
- (5) DiceRoll.py - roll a specified number of dice with a specified number of faces
- (6) UnitConverter.py - converts between various units (can currently only convert between metric length units, more will added soon)
- TicTacToe.py - Play tic tac toe / naughts and crosses / Xs and Os or whatever you call it against a computer (will be added soon)""")
    mainMenu()

# main menu
def mainMenu():
    LBL("""
Main Menu:
    1) NumberGenerators.py
    2) NumberGuessingGame.py
    3) RockPaperScissors.py
    4) CoinFlip.py
    5) DiceRoll.py
    6) UnitConverter.py
    I) Info
    Q) Quit
""")
    menu = LBLInput("Chose from options 1-6, I and Q: ").upper()
    if menu == "1":
        runFile("NumGen")
    elif menu == "2":
        runFile("NumGuess")
    elif menu == "3":
        runFile("RPS")
    elif menu == "4":
        runFile("CoinFlip")
    elif menu == "5":
        runFile("DiceRoll")
    elif menu == "6":
        runFile("UnitConvert")
    elif menu == "I":
        infoPrint()
    elif menu == "Q":
        quitProgram()
    mainMenu()

# main code
mainMenu()