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
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    print()

# one by one character printer with input
def LBLInput(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = input()
    return output

# one by one character printer with integer input
def LBLIntInput(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = int(input())
    return output

# one by one character printer with integer input
def LBLFloatInput(printInput):
    for x in (str(printInput)):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
    output = float(input())
    return output

placeholder = 1


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
    14) Back to main menu (Not finished)
    15) Quit (Not finished)
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
    print("picometres = " + str(picometres))
    if lengthPicometreMenu == 1:
        nanometres = picometres/1000
        print(str(picometres) + " picometres = " + str(round(nanometres,3)) + " nanometres")
    elif lengthPicometreMenu == 2:
        micrometres = picometres/1000000
        print(str(picometres) + " picometres = " + str(round(micrometres,3)) + " micrometres")
    elif lengthPicometreMenu == 3:
        millimetres = picometres/1000000000
        print(str(picometres) + " picometres = " + str(round(millimetres,3)) + " millimetres")
    elif lengthPicometreMenu == 4:
        centimetres = picometres/10000000000
        print(str(picometres) + " picometres = " + str(round(centimetres,3)) + " centimetres")
    elif lengthPicometreMenu == 5:
        decimetre = picometres/100000000000
        print(str(picometres) + " picometres = " + str(round(decimetre,3)) + " decimetre")
    elif lengthPicometreMenu == 6:
        metres = picometres/1000000000000
        print(str(picometres) + " picometres = " + str(round(metres,3)) + " metres")
    elif lengthPicometreMenu == 7:
        kilometres = picometres/1000000000000000
        print(str(picometres) + " picometres = " + str(round(kilometres,3)) + " kilometres")
    elif lengthPicometreMenu == 8:
        inches = picometres/25400000000
        print(str(picometres) + " picometres = " + str(round(inches,3)) + " inches")
    elif lengthPicometreMenu == 9:
        feet = picometres/304800000000
        print(str(picometres) + " picometres = " + str(round(feet,3)) + " feet")
    elif lengthPicometreMenu == 10:
        yards = picometres/914400000000
        print(str(picometres) + " picometres = " + str(round(yards,3)) + " yards")
    elif lengthPicometreMenu == 11:
        miles = picometres/1609340000000000
        print(str(picometres) + " picometres = " + str(round(miles,3)) + " miles")
    elif lengthPicometreMenu == 12:
        nauticalMiles = picometres/1852000000000000
        print(str(picometres) + " picometres = " + str(round(nauticalMiles,3)) + " nautical miles")
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
        print(str(nanometres) + " nanometres = " + str(round(picometres,3)) + " picometres")
    elif lengthNanometreMenu == 2:
        micrometres = nanometres/1000
        print(str(nanometres) + " nanometres = " + str(round(micrometres,3)) + " micrometres")
    elif lengthNanometreMenu == 3:
        millimetres = nanometres/1000000
        print(str(nanometres) + " nanometres = " + str(round(millimetres,3)) + " millimetres")
    elif lengthNanometreMenu == 4:
        centimetres = nanometres/10000000
        print(str(nanometres) + " nanometres = " + str(round(centimetres,3)) + " centimetres")
    elif lengthNanometreMenu == 5:
        decimetre = nanometres/100000000
        print(str(nanometres) + " nanometres = " + str(round(decimetre,3)) + " decimetre")
    elif lengthNanometreMenu == 6:
        metres = nanometres/1000000000
        print(str(nanometres) + " nanometres = " + str(round(metres,3)) + " metres")
    elif lengthNanometreMenu == 7:
        kilometres = nanometres/1000000000000
        print(str(nanometres) + " nanometres = " + str(round(kilometres,3)) + " kilometres")
    elif lengthNanometreMenu == 8:
        inches = nanometres/25400000
        print(str(nanometres) + " nanometres = " + str(round(inches,3)) + " inches")
    elif lengthNanometreMenu == 9:
        feet = nanometres/304800000
        print(str(nanometres) + " nanometres = " + str(round(feet,3)) + " feet")
    elif lengthNanometreMenu == 10:
        yards = nanometres/914400000
        print(str(nanometres) + " nanometres = " + str(round(yards,3)) + " yards")
    elif lengthNanometreMenu == 11:
        miles = nanometres/1609340000000
        print(str(nanometres) + " nanometres = " + str(round(miles,3)) + " miles")
    elif lengthNanometreMenu == 12:
        nauticalMiles = nanometres/1852000000000
        print(str(nanometres) + " nanometres = " + str(round(nauticalMiles,3)) + " nautical miles")
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
        print(str(micrometres) + " micrometres = " + str(round(picometres,3)) + " picometres")
    elif lengthMicrometreMenu == 2:
        nanometres = micrometres*1000
        print(str(micrometres) + " micrometres = " + str(round(nanometres,3)) + " nanometres")
    elif lengthMicrometreMenu == 3:
        millimetres = micrometres/1000
        print(str(micrometres) + " micrometres = " + str(round(millimetres,3)) + " millimetres")
    elif lengthMicrometreMenu == 4:
        centimetres = micrometres/10000
        print(str(micrometres) + " micrometres = " + str(round(centimetres,3)) + " centimetres")
    elif lengthMicrometreMenu == 5:
        decimetre = micrometres/100000
        print(str(micrometres) + " micrometres = " + str(round(decimetre,3)) + " decimetre")
    elif lengthMicrometreMenu == 6:
        metres = micrometres/1000000
        print(str(micrometres) + " micrometres = " + str(round(metres,3)) + " metres")
    elif lengthMicrometreMenu == 7:
        kilometres = micrometres/1000000
        print(str(micrometres) + " micrometres = " + str(round(kilometres,3)) + " kilometres")
    elif lengthMicrometreMenu == 8:
        inches = micrometres/25400
        print(str(micrometres) + " micrometres = " + str(round(inches,3)) + " inches")
    elif lengthMicrometreMenu == 9:
        feet = micrometres/304800
        print(str(micrometres) + " micrometres = " + str(round(feet,3)) + " feet")
    elif lengthMicrometreMenu == 10:
        yards = micrometres/914400
        print(str(micrometres) + " micrometres = " + str(round(yards,3)) + " yards")
    elif lengthMicrometreMenu == 11:
        miles = micrometres/1609340000
        print(str(micrometres) + " micrometres = " + str(round(miles,3)) + " miles")
    elif lengthMicrometreMenu == 12:
        nauticalMiles = micrometres/1852000000
        print(str(micrometres) + " micrometres = " + str(round(nauticalMiles,3)) + " nautical miles")
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
        print(str(millimetres) + " millimetres = " + str(round(picometres,3)) + " picometres")
    elif lengthMillimetreMenu == 2:
        nanometres = millimetres*1000000
        print(str(millimetres) + " millimetres = " + str(round(nanometres,3)) + " nanometres")
    elif lengthMillimetreMenu == 3:
        micrometres = millimetres*1000
        print(str(millimetres) + " millimetres = " + str(round(micrometres,3)) + " micrometres")
    elif lengthMillimetreMenu == 4:
        centimetres = millimetres/10
        print(str(millimetres) + " millimetres = " + str(round(centimetres,3)) + " centimetres")
    elif lengthMillimetreMenu == 5:
        decimetre = millimetres/100
        print(str(millimetres) + " millimetres = " + str(round(decimetre,3)) + " decimetre")
    elif lengthMillimetreMenu == 6:
        metres = millimetres/1000
        print(str(millimetres) + " millimetres = " + str(round(metres,3)) + " metres")
    elif lengthMillimetreMenu == 7:
        kilometres = millimetres/1000000
        print(str(millimetres) + " millimetres = " + str(round(kilometres,3)) + " kilometres")
    elif lengthMillimetreMenu == 8:
        inches = millimetres/25.4
        print(str(millimetres) + " millimetres = " + str(round(inches,3)) + " inches")
    elif lengthMillimetreMenu == 9:
        feet = millimetres/304.8
        print(str(millimetres) + " millimetres = " + str(round(feet,3)) + " feet")
    elif lengthMillimetreMenu == 10:
        yards = millimetres/914.4
        print(str(millimetres) + " millimetres = " + str(round(yards,3)) + " yards")
    elif lengthMillimetreMenu == 11:
        miles = millimetres/1609340
        print(str(millimetres) + " millimetres = " + str(round(miles,3)) + " miles")
    elif lengthMillimetreMenu == 12:
        nauticalMiles = millimetres/1852000
        print(str(millimetres) + " millimetres = " + str(round(nauticalMiles,3)) + " nautical miles")
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
        print(str(centimetres) + " centimetres = " + str(round(picometres,3)) + " picometres")
    elif lengthCentimetreMenu == 2:
        nanometres = centimetres*10000000
        print(str(centimetres) + " centimetres = " + str(round(nanometres,3)) + " nanometres")
    elif lengthCentimetreMenu == 3:
        micrometres = centimetres*10000
        print(str(centimetres) + " centimetres = " + str(round(micrometres,3)) + " micrometres")
    elif lengthCentimetreMenu == 4:
        millimetres = centimetres*10
        print(str(centimetres) + " centimetres = " + str(round(millimetres,3)) + " millimetres")
    elif lengthCentimetreMenu == 5:
        decimetres = centimetres/100000
        print(str(centimetres) + " centimetres = " + str(round(decimetres,3)) + " decimetre")
    elif lengthCentimetreMenu == 6:
        metres = centimetres/100000000
        print(str(centimetres) + " centimetres = " + str(round(metres,3)) + " metres")
    elif lengthCentimetreMenu == 7:
        kilometres = centimetres/100000000000
        print(str(centimetres) + " centimetres = " + str(round(kilometres,3)) + " kilometres")
    elif lengthCentimetreMenu == 8:
        inches = centimetres/2.54
        print(str(centimetres) + " centimetres = " + str(round(inches,3)) + " inches")
    elif lengthCentimetreMenu == 9:
        feet = centimetres/30.48
        print(str(centimetres) + " centimetres = " + str(round(feet,3)) + " feet")
    elif lengthCentimetreMenu == 10:
        yards = centimetres/91.44
        print(str(centimetres) + " centimetres = " + str(round(yards,3)) + " yards")
    elif lengthCentimetreMenu == 11:
        miles = centimetres/160934
        print(str(centimetres) + " centimetres = " + str(round(miles,3)) + " miles")
    elif lengthCentimetreMenu == 12:
        nauticalMiles = centimetres/185200
        print(str(centimetres) + " centimetres = " + str(round(nauticalMiles,3)) + " nautical miles")
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
        print(str(decimetres) + " decimetres = " + str(round(picometres,3)) + " picometres")
    elif lengthDecimetreMenu == 2:
        nanometres = decimetres*100000000
        print(str(decimetres) + " decimetres = " + str(round(nanometres,3)) + " nanometres")
    elif lengthDecimetreMenu == 3:
        micrometres = decimetres*100000
        print(str(decimetres) + " decimetres = " + str(round(micrometres,3)) + " micrometres")
    elif lengthDecimetreMenu == 4:
        millimetres = decimetres*100
        print(str(decimetres) + " decimetres = " + str(round(millimetres,3)) + " millimetres")
    elif lengthDecimetreMenu == 5:
        centimetres = decimetres*10
        print(str(decimetres) + " decimetres = " + str(round(centimetres,3)) + " centimetres")
    elif lengthDecimetreMenu == 6:
        metres = decimetres/10000000
        print(str(decimetres) + " decimetres = " + str(round(metres,3)) + " metres")
    elif lengthDecimetreMenu == 7:
        kilometres = decimetres/10000000000
        print(str(decimetres) + " decimetres = " + str(round(kilometres,3)) + " kilometres")
    elif lengthDecimetreMenu == 8:
        inches = decimetres/0.254
        print(str(decimetres) + " decimetres = " + str(round(inches,3)) + " inches")
    elif lengthDecimetreMenu == 9:
        feet = decimetres/3.048
        print(str(decimetres) + " decimetres = " + str(round(feet,3)) + " feet")
    elif lengthDecimetreMenu == 10:
        yards = decimetres/9.144
        print(str(decimetres) + " decimetres = " + str(round(yards,3)) + " yards")
    elif lengthDecimetreMenu == 11:
        miles = decimetres/16093.4
        print(str(decimetres) + " decimetres = " + str(round(miles,3)) + " miles")
    elif lengthDecimetreMenu == 12:
        nauticalMiles = decimetres/18520
        print(str(decimetres) + " decimetres = " + str(round(nauticalMiles,3)) + " nautical miles")
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
        print(str(metres) + " metres = " + str(round(picometres,3)) + " picometres")
    elif lengthMetreMenu == 2:
        nanometres = metres*1000000000
        print(str(metres) + " metres = " + str(round(nanometres,3)) + " nanometres")
    elif lengthMetreMenu == 3:
        micrometres = metres*1000000
        print(str(metres) + " metres = " + str(round(micrometres,3)) + " micrometres")
    elif lengthMetreMenu == 4:
        millimetres = metres*1000
        print(str(metres) + " metres = " + str(round(millimetres,3)) + " millimetres")
    elif lengthMetreMenu == 5:
        centimetres = metres*100
        print(str(metres) + " metres = " + str(round(centimetres,3)) + " centimetres")
    elif lengthMetreMenu == 6:
        decimetres = metres*10
        print(str(metres) + " metres = " + str(round(decimetres,3)) + " decimetres")
    elif lengthMetreMenu == 7:
        kilometres = metres/1000
        print(str(metres) + " metres = " + str(round(kilometres,3)) + " kilometres")
    elif lengthMetreMenu == 8:
        inches = metres/0.0254
        print(str(metres) + " metres = " + str(round(inches,3)) + " inches")
    elif lengthMetreMenu == 9:
        feet = metres/0.3048
        print(str(metres) + " metres = " + str(round(feet,3)) + " feet")
    elif lengthMetreMenu == 10:
        yards = metres/0.9144
        print(str(metres) + " metres = " + str(round(yards,3)) + " yards")
    elif lengthMetreMenu == 11:
        miles = metres/1609.34
        print(str(metres) + " metres = " + str(round(miles,3)) + " miles")
    elif lengthMetreMenu == 12:
        nauticalMiles = metres/1852
        print(str(metres) + " metres = " + str(round(nauticalMiles,3)) + " nautical miles")
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
        print(str(kilometres) + " kilometres = " + str(round(picometres,3)) + " picometres")
    elif lengthKilometreMenu == 2:
        nanometres = kilometres*1000000000000
        print(str(kilometres) + " kilometres = " + str(round(nanometres,3)) + " nanometres")
    elif lengthKilometreMenu == 3:
        micrometres = kilometres*1000000000
        print(str(kilometres) + " kilometres = " + str(round(micrometres,3)) + " micrometres")
    elif lengthKilometreMenu == 4:
        millimetres = kilometres*1000000
        print(str(kilometres) + " kilometres = " + str(round(millimetres,3)) + " millimetres")
    elif lengthKilometreMenu == 5:
        centimetres = kilometres*100000
        print(str(kilometres) + " kilometres = " + str(round(centimetres,3)) + " centimetres")
    elif lengthKilometreMenu == 6:
        decimetres = kilometres*10000
        print(str(kilometres) + " kilometres = " + str(round(decimetres,3)) + " decimetres")
    elif lengthKilometreMenu == 7:
        metres = kilometres*1000
        print(str(kilometres) + " kilometres = " + str(round(metres,3)) + " metres")
    elif lengthKilometreMenu == 8:
        inches = kilometres/0.0000254
        print(str(kilometres) + " kilometres = " + str(round(inches,3)) + " inches")
    elif lengthKilometreMenu == 9:
        feet = kilometres/0.0003048
        print(str(kilometres) + " kilometres = " + str(round(feet,3)) + " feet")
    elif lengthKilometreMenu == 10:
        yards = kilometres/0.0009144
        print(str(kilometres) + " kilometres = " + str(round(yards,3)) + " yards")
    elif lengthKilometreMenu == 11:
        miles = kilometres/1.60934
        print(str(kilometres) + " kilometres = " + str(round(miles,3)) + " miles")
    elif lengthKilometreMenu == 12:
        nauticalMiles = kilometres/1.852
        print(str(kilometres) + " kilometres = " + str(round(nauticalMiles,3)) + " nautical miles")
    elif lengthKilometreMenu == 13:
        convertLength()
    elif lengthKilometreMenu == 14:
        mainMenu()
    elif lengthKilometreMenu == 15:
        quitProgram()



# quit program
def quitProgram():
        LBL("\nQuitting\n")
        quit()

# main menu
def mainMenu():
    LBL("""
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