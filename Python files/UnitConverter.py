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

# one by one character printer with integer input
def LBLFloatInput(printInput):
    for x in str(printInput):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = float(input())
    return output

# Length Converter
def convertLength():
    LBL("""

Convert from:
    1) Picometre
    2) Nanometre
    3) Micrometre
    4) Millimetre
    5) Centimetre
    6) Decimetre
    7) Metre
    8) Kilometre
    9) Inch (Not finished)
    10) Foot (Not finished)
    11) Yard (Not finished)
    12) Mile (Not finished)
    13) Nautical mile (Not finished)
    14) Back to main menu
    15) Quit
    """)
    lengthMenu = LBLIntInput("Chose from options 1 - 15: ")
    if lengthMenu == 1:
        convertLengthPicometre()
    elif lengthMenu == 2:
        convertLengthNanometre()
    elif lengthMenu == 3:
        convertLengthMicrometre()
    elif lengthMenu == 4:
        convertLengthMillimetre()
    elif lengthMenu == 5:
        convertLengthCentimetre()
    elif lengthMenu == 6:
        convertLengthDecimetre()
    elif lengthMenu == 7:
        convertLengthMetre()
    elif lengthMenu == 8:
        convertLengthKilometre()
    elif lengthMenu == 9:
        # convertLengthInch()
        print("Not finished yet! ")
    elif lengthMenu == 10:
        # convertLengthFoot()
        print("Not finished yet! ")
    elif lengthMenu == 11:
        # convertLengthYard()
        print("Not finished yet! ")
    elif lengthMenu == 12:
        # convertLengthMile()
        print("Not finished yet! ")
    elif lengthMenu == 13:
        # convertLengthNauticalMile()
        print("Not finished yet! ")
    elif lengthMenu == 14:
        mainMenu()
    elif lengthMenu == 15:
        quitProgram()
    convertLengthAgain()

# convert length again prompt
def convertLengthAgain():
    convertLengthAgainQ = LBLInput("\n\nWould you like to convert length units again? ")
    if convertLengthAgainQ == "y" or convertLengthAgainQ == "yes" or convertLengthAgainQ == "yep" or convertLengthAgainQ == "yeah":
        convertLength()

# Length Converter - Picometre
def convertLengthPicometre():
    LBL("""

Convert to:
    1) Nanometre
    2) Micrometre
    3) Millimetre
    4) Centimetre
    5) Decimetre
    6) Metre
    7) Kilometre
    8) Inch
    9) Foot
    10) Yard
    11) Mile
    12) Nautical mile
    13) Back to length converter
    14) Back to main menu
    15) Quit
    """)
    lengthPicometreMenu = LBLIntInput("Chose from options 1 - 15: ")
    picometres = LBLFloatInput("Enter the amount of picometres: ")
    if lengthPicometreMenu == 1:
        nanometres = picometres/1000
        LBL(f"{picometres} picometres = {nanometres:.3f} nanometres")
    elif lengthPicometreMenu == 2:
        micrometres = picometres/1000000
        LBL(f"{picometres} picometres = {micrometres:.3f} micrometres")
    elif lengthPicometreMenu == 3:
        millimetres = picometres/1000000000
        LBL(f"{picometres} picometres = {millimetres:.3f} millimetres")
    elif lengthPicometreMenu == 4:
        centimetres = picometres/10000000000
        LBL(f"{picometres} picometres = {centimetres:.3f} centimetres")
    elif lengthPicometreMenu == 5:
        decimetre = picometres/100000000000
        LBL(f"{picometres} picometres = {decimetre:.3f} decimetre")
    elif lengthPicometreMenu == 6:
        metres = picometres/1000000000000
        LBL(f"{picometres} picometres = {metres:.3f} metres")
    elif lengthPicometreMenu == 7:
        kilometres = picometres/1000000000000000
        LBL(f"{picometres} picometres = {kilometres:.3f} kilometres")
    elif lengthPicometreMenu == 8:
        inches = picometres/25400000000
        LBL(f"{picometres} picometres = {inches:.3f} inches")
    elif lengthPicometreMenu == 9:
        feet = picometres/304800000000
        LBL(f"{picometres} picometres = {feet:.3f} feet")
    elif lengthPicometreMenu == 10:
        yards = picometres/914400000000
        LBL(f"{picometres} picometres = {yards:.3f} yards")
    elif lengthPicometreMenu == 11:
        miles = picometres/1609340000000000
        LBL(f"{picometres} picometres = {miles:.3f} miles")
    elif lengthPicometreMenu == 12:
        nauticalMiles = picometres/1852000000000000
        LBL(f"{picometres} picometres = {nauticalMiles:.3f} nautical miles")
    elif lengthPicometreMenu == 13:
        convertLength()
    elif lengthPicometreMenu == 14:
        mainMenu()
    elif lengthPicometreMenu == 15:
        quitProgram()

# Length Converter - Nanometre
def convertLengthNanometre():
    LBL("""

Convert to:
    1) Picometre
    2) Micrometre
    3) Millimetre
    4) Centimetre
    5) Decimetre
    6) Metre
    7) Kilometre
    8) Inch
    9) Foot
    10) Yard
    11) Mile
    12) Nautical mile
    13) Back to length converter
    14) Back to main menu
    15) Quit
    """)
    lengthNanometreMenu = LBLIntInput("Chose from options 1 - 15: ")
    nanometres = LBLFloatInput("Enter the amount of nanometres: ")
    if lengthNanometreMenu == 1:
        picometres = nanometres*1000
        LBL(f"{nanometres} nanometres = {picometres:.3f} picometres")
    elif lengthNanometreMenu == 2:
        micrometres = nanometres/1000
        LBL(f"{nanometres} nanometres = {micrometres:.3f} micrometres")
    elif lengthNanometreMenu == 3:
        millimetres = nanometres/1000000
        LBL(f"{nanometres} nanometres = {millimetres:.3f} millimetres")
    elif lengthNanometreMenu == 4:
        centimetres = nanometres/10000000
        LBL(f"{nanometres} nanometres = {centimetres:.3f} centimetres")
    elif lengthNanometreMenu == 5:
        decimetre = nanometres/100000000
        LBL(f"{nanometres} nanometres = {decimetre:.3f} decimetre")
    elif lengthNanometreMenu == 6:
        metres = nanometres/1000000000
        LBL(f"{nanometres} nanometres = {metres:.3f} metres")
    elif lengthNanometreMenu == 7:
        kilometres = nanometres/1000000000000
        LBL(f"{nanometres} nanometres = {kilometres:.3f} kilometres")
    elif lengthNanometreMenu == 8:
        inches = nanometres/25400000
        LBL(f"{nanometres} nanometres = {inches:.3f} inches")
    elif lengthNanometreMenu == 9:
        feet = nanometres/304800000
        LBL(f"{nanometres} nanometres = {feet,:.3f} feet")
    elif lengthNanometreMenu == 10:
        yards = nanometres/914400000
        LBL(f"{nanometres} nanometres = {yards:.3f} yards")
    elif lengthNanometreMenu == 11:
        miles = nanometres/1609340000000
        LBL(f"{nanometres} nanometres = {miles:.3f} miles")
    elif lengthNanometreMenu == 12:
        nauticalMiles = nanometres/1852000000000
        LBL(f"{nanometres} nanometres = {nauticalMiles:.3f} nautical miles")
    elif lengthNanometreMenu == 13:
        convertLength()
    elif lengthNanometreMenu == 14:
        mainMenu()
    elif lengthNanometreMenu == 15:
        quitProgram()

    # Length Converter - Micrometre
def convertLengthMicrometre():
    LBL("""

Convert to:
    1) Picometre
    2) Nanometre
    3) Millimetre
    4) Centimetre
    5) Decimetre
    6) Metre
    7) Kilometre
    8) Inch
    9) Foot
    10) Yard
    11) Mile
    12) Nautical mile
    13) Back to length converter
    14) Back to main menu
    15) Quit
    """)
    lengthMicrometreMenu = LBLIntInput("Chose from options 1 - 15: ")
    micrometres = LBLFloatInput("Enter the amount of micrometres: ")
    if lengthMicrometreMenu == 1:
        picometres = micrometres*1000000
        LBL(f"{micrometres} micrometres = {picometres:.3f} picometres")
    elif lengthMicrometreMenu == 2:
        nanometres = micrometres*1000
        LBL(f"{micrometres} micrometres = {nanometres:.3f} nanometres")
    elif lengthMicrometreMenu == 3:
        millimetres = micrometres/1000
        LBL(f"{micrometres} micrometres = {millimetres:.3f} millimetres")
    elif lengthMicrometreMenu == 4:
        centimetres = micrometres/10000
        LBL(f"{micrometres} micrometres = {centimetres:.3f} centimetres")
    elif lengthMicrometreMenu == 5:
        decimetre = micrometres/100000
        LBL(f"{micrometres} micrometres = {decimetre:.3f} decimetre")
    elif lengthMicrometreMenu == 6:
        metres = micrometres/1000000
        LBL(f"{micrometres} micrometres = {metres:.3f} metres")
    elif lengthMicrometreMenu == 7:
        kilometres = micrometres/1000000
        LBL(f"{micrometres} micrometres = {kilometres:.3f} kilometres")
    elif lengthMicrometreMenu == 8:
        inches = micrometres/25400
        LBL(f"{micrometres} micrometres = {inches:.3f} inches")
    elif lengthMicrometreMenu == 9:
        feet = micrometres/304800
        LBL(f"{micrometres} micrometres = {feet:.3f} feet")
    elif lengthMicrometreMenu == 10:
        yards = micrometres/914400
        LBL(f"{micrometres} micrometres = {yards:.3f} yards")
    elif lengthMicrometreMenu == 11:
        miles = micrometres/1609340000
        LBL(f"{micrometres} micrometres = {miles:.3f} miles")
    elif lengthMicrometreMenu == 12:
        nauticalMiles = micrometres/1852000000
        LBL(f"{micrometres} micrometres = {nauticalMiles:.3f} nautical miles")
    elif lengthMicrometreMenu == 13:
        convertLength()
    elif lengthMicrometreMenu == 14:
        mainMenu()
    elif lengthMicrometreMenu == 15:
        quitProgram()

    # Length Converter - Millimetre
def convertLengthMillimetre():
    LBL("""

Convert to:
    1) Picometre
    2) Nanometre
    3) Micrometre
    4) Centimetre
    5) Decimetre
    6) Metre
    7) Kilometre
    8) Inch
    9) Foot
    10) Yard
    11) Mile
    12) Nautical mile
    13) Back to length converter
    14) Back to main menu
    15) Quit
    """)
    lengthMillimetreMenu = LBLIntInput("Chose from options 1 - 15: ")
    millimetres = LBLFloatInput("Enter the amount of millimetres: ")
    if lengthMillimetreMenu == 1:
        picometres = millimetres*1000000000
        LBL(f"{millimetres} millimetres = {picometres:.3f} picometres")
    elif lengthMillimetreMenu == 2:
        nanometres = millimetres*1000000
        LBL(f"{millimetres} millimetres = {nanometres:.3f} nanometres")
    elif lengthMillimetreMenu == 3:
        micrometres = millimetres*1000
        LBL(f"{millimetres} millimetres = {micrometres:.3f} micrometres")
    elif lengthMillimetreMenu == 4:
        centimetres = millimetres/10
        LBL(f"{millimetres} millimetres = {centimetres:.3f} centimetres")
    elif lengthMillimetreMenu == 5:
        decimetre = millimetres/100
        LBL(f"{millimetres} millimetres = {decimetre:.3f} decimetre")
    elif lengthMillimetreMenu == 6:
        metres = millimetres/1000
        LBL(f"{millimetres} millimetres = {metres:.3f} metres")
    elif lengthMillimetreMenu == 7:
        kilometres = millimetres/1000000
        LBL(f"{millimetres} millimetres = {kilometres:.3f} kilometres")
    elif lengthMillimetreMenu == 8:
        inches = millimetres/25.4
        LBL(f"{millimetres} millimetres = {inches:.3f} inches")
    elif lengthMillimetreMenu == 9:
        feet = millimetres/304.8
        LBL(f"{millimetres} millimetres = {feet:.3f} feet")
    elif lengthMillimetreMenu == 10:
        yards = millimetres/914.4
        LBL(f"{millimetres} millimetres = {yards:.3f} yards")
    elif lengthMillimetreMenu == 11:
        miles = millimetres/1609340
        LBL(f"{millimetres} millimetres = {miles:.3f} miles")
    elif lengthMillimetreMenu == 12:
        nauticalMiles = millimetres/1852000
        LBL(f"{millimetres} millimetres = {nauticalMiles:.3f} nautical miles")
    elif lengthMillimetreMenu == 13:
        convertLength()
    elif lengthMillimetreMenu == 14:
        mainMenu()
    elif lengthMillimetreMenu == 15:
        quitProgram()

    # Length Converter - Centimetre
def convertLengthCentimetre():
    LBL("""

Convert to:
    1) Picometre
    2) Nanometre
    3) Micrometre
    4) Millimetre
    5) Decimetre
    6) Metre
    7) Kilometre
    8) Inch
    9) Foot
    10) Yard
    11) Mile
    12) Nautical mile
    13) Back to length converter
    14) Back to main menu
    15) Quit
    """)
    lengthCentimetreMenu = LBLIntInput("Chose from options 1 - 15: ")
    centimetres = LBLFloatInput("Enter the amount of centimetres: ")
    if lengthCentimetreMenu == 1:
        picometres = centimetres*10000000000
        LBL(f"{centimetres} centimetres = {picometres:.3f} picometres")
    elif lengthCentimetreMenu == 2:
        nanometres = centimetres*10000000
        LBL(f"{centimetres} centimetres = {nanometres:.3f} nanometres")
    elif lengthCentimetreMenu == 3:
        micrometres = centimetres*10000
        LBL(f"{centimetres} centimetres = {micrometres:.3f} micrometres")
    elif lengthCentimetreMenu == 4:
        millimetres = centimetres*10
        LBL(f"{centimetres} centimetres = {millimetres:.3f} millimetres")
    elif lengthCentimetreMenu == 5:
        decimetres = centimetres/100000
        LBL(f"{centimetres} centimetres = {decimetres:.3f} decimetre")
    elif lengthCentimetreMenu == 6:
        metres = centimetres/100000000
        LBL(f"{centimetres} centimetres = {metres:.3f} metres")
    elif lengthCentimetreMenu == 7:
        kilometres = centimetres/100000000000
        LBL(f"{centimetres} centimetres = {kilometres:.3f} kilometres")
    elif lengthCentimetreMenu == 8:
        inches = centimetres/2.54
        LBL(f"{centimetres} centimetres = {inches:.3f} inches")
    elif lengthCentimetreMenu == 9:
        feet = centimetres/30.48
        LBL(f"{centimetres} centimetres = {feet:.3f} feet")
    elif lengthCentimetreMenu == 10:
        yards = centimetres/91.44
        LBL(f"{centimetres} centimetres = {yards:.3f} yards")
    elif lengthCentimetreMenu == 11:
        miles = centimetres/160934
        LBL(f"{centimetres} centimetres = {miles:.3f} miles")
    elif lengthCentimetreMenu == 12:
        nauticalMiles = centimetres/185200
        LBL(f"{centimetres} centimetres = {nauticalMiles:.3f} nautical miles")
    elif lengthCentimetreMenu == 13:
        convertLength()
    elif lengthCentimetreMenu == 14:
        mainMenu()
    elif lengthCentimetreMenu == 15:
        quitProgram()

    # Length Converter - Decimetre
def convertLengthDecimetre():
    LBL("""

Convert to:
    1) Picometre
    2) Nanometre
    3) Micrometre
    4) Millimetre
    5) Centimetre
    6) Metre
    7) Kilometre
    8) Inch
    9) Foot
    10) Yard
    11) Mile
    12) Nautical mile
    13) Back to length converter
    14) Back to main menu
    15) Quit
    """)
    lengthDecimetreMenu = LBLIntInput("Chose from options 1 - 15: ")
    decimetres = LBLFloatInput("Enter the amount of decimetres: ")
    if lengthDecimetreMenu == 1:
        picometres = decimetres*100000000000
        LBL(f"{decimetres} decimetres = {picometres:.3} picometres")
    elif lengthDecimetreMenu == 2:
        nanometres = decimetres*100000000
        LBL(f"{decimetres} decimetres = {nanometres:.3} nanometres")
    elif lengthDecimetreMenu == 3:
        micrometres = decimetres*100000
        LBL(f"{decimetres} decimetres = {micrometres:.3} micrometres")
    elif lengthDecimetreMenu == 4:
        millimetres = decimetres*100
        LBL(f"{decimetres} decimetres = {millimetres:.3} millimetres")
    elif lengthDecimetreMenu == 5:
        centimetres = decimetres*10
        LBL(f"{decimetres} decimetres = {centimetres:.3} centimetres")
    elif lengthDecimetreMenu == 6:
        metres = decimetres/10000000
        LBL(f"{decimetres} decimetres = {metres:.3} metres")
    elif lengthDecimetreMenu == 7:
        kilometres = decimetres/10000000000
        LBL(f"{decimetres} decimetres = {kilometres:.3} kilometres")
    elif lengthDecimetreMenu == 8:
        inches = decimetres/0.254
        LBL(f"{decimetres} decimetres = {inches:.3} inches")
    elif lengthDecimetreMenu == 9:
        feet = decimetres/3.048
        LBL(f"{decimetres} decimetres = {feet:.3} feet")
    elif lengthDecimetreMenu == 10:
        yards = decimetres/9.144
        LBL(f"{decimetres} decimetres = {yards:.3} yards")
    elif lengthDecimetreMenu == 11:
        miles = decimetres/16093.4
        LBL(f"{decimetres} decimetres = {miles:.3} miles")
    elif lengthDecimetreMenu == 12:
        nauticalMiles = decimetres/18520
        LBL(f"{decimetres} decimetres = {nauticalMiles:.3} nautical miles")
    elif lengthDecimetreMenu == 13:
        convertLength()
    elif lengthDecimetreMenu == 14:
        mainMenu()
    elif lengthDecimetreMenu == 15:
        quitProgram()

    # Length Converter - Metre
def convertLengthMetre():
    LBL("""

Convert to:
    1) Picometre
    2) Nanometre
    3) Micrometre
    4) Millimetre
    5) Centimetre
    6) Decimetre
    7) Kilometre
    8) Inch
    9) Foot
    10) Yard
    11) Mile
    12) Nautical mile
    13) Back to length converter
    14) Back to main menu
    15) Quit
    """)
    lengthMetreMenu = LBLIntInput("Chose from options 1 - 15: ")
    metres = LBLFloatInput("Enter the amount of metres: ")
    if lengthMetreMenu == 1:
        picometres = metres*1000000000000
        LBL(f"{metres} metres = {picometres:.3f} picometres")
    elif lengthMetreMenu == 2:
        nanometres = metres*1000000000
        LBL(f"{metres} metres = {nanometres:.3f} nanometres")
    elif lengthMetreMenu == 3:
        micrometres = metres*1000000
        LBL(f"{metres} metres = {micrometres:.3f} micrometres")
    elif lengthMetreMenu == 4:
        millimetres = metres*1000
        LBL(f"{metres} metres = {millimetres:.3f} millimetres")
    elif lengthMetreMenu == 5:
        centimetres = metres*100
        LBL(f"{metres} metres = {centimetres:.3f} centimetres")
    elif lengthMetreMenu == 6:
        decimetres = metres*10
        LBL(f"{metres} metres = {decimetres:.3f} decimetres")
    elif lengthMetreMenu == 7:
        kilometres = metres/1000
        LBL(f"{metres} metres = {kilometres:.3f} kilometres")
    elif lengthMetreMenu == 8:
        inches = metres/0.0254
        LBL(f"{metres} metres = {inches:.3f} inches")
    elif lengthMetreMenu == 9:
        feet = metres/0.3048
        LBL(f"{metres} metres = {feet:.3f} feet")
    elif lengthMetreMenu == 10:
        yards = metres/0.9144
        LBL(f"{metres} metres = {yards:.3f} yards")
    elif lengthMetreMenu == 11:
        miles = metres/1609.34
        LBL(f"{metres} metres = {miles:.3f} miles")
    elif lengthMetreMenu == 12:
        nauticalMiles = metres/1852
        LBL(f"{metres} metres = {nauticalMiles:.3f} nautical miles")
    elif lengthMetreMenu == 13:
        convertLength()
    elif lengthMetreMenu == 14:
        mainMenu()
    elif lengthMetreMenu == 15:
        quitProgram()

    # Length Converter - Kilometre
def convertLengthKilometre():
    LBL("""

Convert to:
    1) Picometre
    2) Nanometre
    3) Micrometre
    4) Millimetre
    5) Centimetre
    6) Decimetre
    7) Metre
    8) Inch
    9) Foot
    10) Yard
    11) Mile
    12) Nautical mile
    13) Back to length converter
    14) Back to main menu
    15) Quit
    """)
    lengthKilometreMenu = LBLIntInput("Chose from options 1 - 15: ")
    kilometres = LBLFloatInput("Enter the amount of kilometres: ")
    if lengthKilometreMenu == 1:
        picometres = kilometres*1000000000000000
        LBL(f"{kilometres} kilometres = {picometres:.3f} picometres")
    elif lengthKilometreMenu == 2:
        nanometres = kilometres*1000000000000
        LBL(f"{kilometres} kilometres = {nanometres:.3f} nanometres")
    elif lengthKilometreMenu == 3:
        micrometres = kilometres*1000000000
        LBL(f"{kilometres} kilometres = {micrometres:.3f} micrometres")
    elif lengthKilometreMenu == 4:
        millimetres = kilometres*1000000
        LBL(f"{kilometres} kilometres = {millimetres:.3f} millimetres")
    elif lengthKilometreMenu == 5:
        centimetres = kilometres*100000
        LBL(f"{kilometres} kilometres = {centimetres:.3f} centimetres")
    elif lengthKilometreMenu == 6:
        decimetres = kilometres*10000
        LBL(f"{kilometres} kilometres = {decimetres:.3f} decimetres")
    elif lengthKilometreMenu == 7:
        metres = kilometres*1000
        LBL(f"{kilometres} kilometres = {metres:.3f} metres")
    elif lengthKilometreMenu == 8:
        inches = kilometres/0.0000254
        LBL(f"{kilometres} kilometres = {inches:.3f} inches")
    elif lengthKilometreMenu == 9:
        feet = kilometres/0.0003048
        LBL(f"{kilometres} kilometres = {feet:.3f} feet")
    elif lengthKilometreMenu == 10:
        yards = kilometres/0.0009144
        LBL(f"{kilometres} kilometres = {yards:.3f} yards")
    elif lengthKilometreMenu == 11:
        miles = kilometres/1.60934
        LBL(f"{kilometres} kilometres = {miles:.3f} miles")
    elif lengthKilometreMenu == 12:
        nauticalMiles = kilometres/1.852
        LBL(f"{kilometres} kilometres = {nauticalMiles:.3f} nautical miles")
    elif lengthKilometreMenu == 13:
        convertLength()
    elif lengthKilometreMenu == 14:
        mainMenu()
    elif lengthKilometreMenu == 15:
        quitProgram()


# quit program
def quitProgram():
    LBL("\nQuitting")
    quit()

# main menu
def mainMenu():
    LBL("""Welcome to unit converter!
Main menu:
    1) Length
    2) Area (Not finished)
    3) Volume (Not finished)
    4) Time (Not finished)
    5) Speed (Not finished)
    6) Acceleration (Not finished)
    7) Mass (Not finished)
    8) Pressure (Not finished)
    9) Energy (Not finished)
    10) Force (Not finished)
    11) Temperature (Not finished)
    12) Quit
    """)
    mainMenu = LBLIntInput("Chose from options 1 - 12: ")
    if mainMenu == 1:
        convertLength()

    elif mainMenu == 2:
        # convertArea()
        print("Not finished yet! ")

    elif mainMenu == 3:
        # convertVolume()
        print("Not finished yet! ")

    elif mainMenu == 4:
        # convertTime()
        print("Not finished yet! ")

    elif mainMenu == 5:
        # convertSpeed()
        print("Not finished yet! ")

    elif mainMenu == 6:
        # convertAcceleration()
        print("Not finished yet! ")

    elif mainMenu == 7:
        # convertMass()
        print("Not finished yet! ")

    elif mainMenu == 8:
        # convertPressure()
        print("Not finished yet! ")

    elif mainMenu == 9:
        # convertEnergy()
        print("Not finished yet! ")

    elif mainMenu == 10:
        # convertForce()
        print("Not finished yet! ")

    elif mainMenu == 11:
        # convertTemperature()
        print("Not finished yet! ")

    elif mainMenu == 12:
        quitProgram()

    runAgain()

# run again prompt
def runAgain():
    runAgainQ = LBLInput("\n\nWould you like to convert units again? ")
    if runAgainQ == "y" or runAgainQ == "yes" or runAgainQ == "yep" or runAgainQ == "yeah":
        mainMenu()
    else:
        quitProgram()

# main block
mainMenu()