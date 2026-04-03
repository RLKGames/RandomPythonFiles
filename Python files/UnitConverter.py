import sys
import time

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
    LBL("""\nConvert from:
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
I) Info
M) Back to main menu
Q) Quit\n""")
    menu = LBLInput("Chose from options 1-13, I, M or Q: ").upper()
    if menu == "1":
        convertLengthPicometre()
    elif menu == "2":
        convertLengthNanometre()
    elif menu == "3":
        convertLengthMicrometre()
    elif menu == "4":
        convertLengthMillimetre()
    elif menu == "5":
        convertLengthCentimetre()
    elif menu == "6":
        convertLengthDecimetre()
    elif menu == "7":
        convertLengthMetre()
    elif menu == "8":
        convertLengthKilometre()
    elif menu == "9":
        # convertLengthInch()
        LBL("Not finished yet!")
    elif menu == "10":
        # convertLengthFoot()
        LBL("Not finished yet!")
    elif menu == "11":
        # convertLengthYard()
        LBL("Not finished yet!")
    elif menu == "12":
        # convertLengthMile()
        LBL("Not finished yet!")
    elif menu == "13":
        # convertLengthNauticalMile()
        LBL("Not finished yet!")
    elif menu == "I":
        LBL("Info is not finished yet!")
    elif menu == "M":
        mainMenu()
    elif menu == "Q":
        quitProgram()
    convertLength()

# Length Converter - Picometre
def convertLengthPicometre():
    LBL("""\nConvert to:
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
I) Info
L) Back to length converter
M) Back to main menu
Q) Quit\n""")
    menu = LBLInput("Chose from options 1-12, I, L, M or Q: ").upper()
    inputUnit = LBLFloatInput("Enter the number of picometres: ")
    if menu == "1":
        LBL(f"{inputUnit} picometres = {inputUnit/1000:.3f} nanometres")
    elif menu == "2":
        LBL(f"{inputUnit} picometres = {inputUnit/1000000:.3f} micrometres")
    elif menu == "3":
        LBL(f"{inputUnit} picometres = {inputUnit/1000000000:.3f} millimetres")
    elif menu == "4":
        LBL(f"{inputUnit} picometres = {inputUnit/10000000000:.3f} centimetres")
    elif menu == "5":
        LBL(f"{inputUnit} picometres = {inputUnit/100000000000:.3f} decimetre")
    elif menu == "6":
        LBL(f"{inputUnit} picometres = {inputUnit/1000000000000} metres")
    elif menu == "7":
        LBL(f"{inputUnit} picometres = {inputUnit/1000000000000000:.3f} kilometres")
    elif menu == "8":
        LBL(f"{inputUnit} picometres = {inputUnit/25400000000:.3f} inches")
    elif menu == "9":
        LBL(f"{inputUnit} picometres = {inputUnit/304800000000:.3f} feet")
    elif menu == "10":
        LBL(f"{inputUnit} picometres = {inputUnit/914400000000:.3f} yards")
    elif menu == "11":
        LBL(f"{inputUnit} picometres = {inputUnit/1609340000000000:.3f} miles")
    elif menu == "12":
        LBL(f"{inputUnit} picometres = {inputUnit/1852000000000000:.3f} nautical miles")
    elif menu == "I":
        LBL("Info is not finished yet!")
    elif menu == "L":
        convertLength()
    elif menu == "M":
        mainMenu()
    elif menu == "Q":
        quitProgram()
    convertLengthPicometre()

# Length Converter - Nanometre
def convertLengthNanometre():
    LBL("""\nConvert to:
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
I) Info
L) Back to length converter
M) Back to main menu
Q) Quit\n""")
    menu = LBLInput("Chose from options 1-12, I, L, M or Q: ").upper()
    inputUnit = LBLFloatInput("Enter the number of nanometres: ")
    if menu == "1":
        LBL(f"{inputUnit} nanometres = {inputUnit*1000:.3f} picometres")
    elif menu == "2":
        LBL(f"{inputUnit} nanometres = {inputUnit/1000:.3f} micrometres")
    elif menu == "3":
        LBL(f"{inputUnit} nanometres = {inputUnit/1000000:.3f} millimetres")
    elif menu == "4":
        LBL(f"{inputUnit} nanometres = {inputUnit/10000000:.3f} centimetres")
    elif menu == "5":
        LBL(f"{inputUnit} nanometres = {inputUnit/100000000:.3f} decimetre")
    elif menu == "6":
        LBL(f"{inputUnit} nanometres = {inputUnit/1000000000:.3f} metres")
    elif menu == "7":
        LBL(f"{inputUnit} nanometres = {inputUnit/1000000000000:.3f} kilometres")
    elif menu == "8":
        LBL(f"{inputUnit} nanometres = {inputUnit/25400000:.3f} inches")
    elif menu == "9":
        LBL(f"{inputUnit} nanometres = {inputUnit/304800000,:.3f} feet")
    elif menu == "10":
        LBL(f"{inputUnit} nanometres = {inputUnit/914400000:.3f} yards")
    elif menu == "11":
        LBL(f"{inputUnit} nanometres = {inputUnit/1609340000000:.3f} miles")
    elif menu == "12":
        LBL(f"{inputUnit} nanometres = {inputUnit/1852000000000:.3f} nautical miles")
    elif menu == "I":
        LBL("Info is not finished yet!")   
    elif menu == "L":
        convertLength()
    elif menu == "M":
        mainMenu()
    elif menu == "Q":
        quitProgram()
    convertLengthNanometre()

# Length Converter - Micrometre
def convertLengthMicrometre():
    LBL("""\nConvert to:
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
I) Info
L) Back to length converter
M) Back to main menu
Q) Quit\n""")
    menu = LBLInput("Chose from options 1-12, I, L, M or Q: ").upper()
    inputUnit = LBLFloatInput("Enter the number of micrometres: ")
    if menu == "1":
        LBL(f"{inputUnit} micrometres = {inputUnit*1000000:.3f} picometres")
    elif menu == "2":
        LBL(f"{inputUnit} micrometres = {inputUnit*1000:.3f} nanometres")
    elif menu == "3":
        LBL(f"{inputUnit} micrometres = {inputUnit/1000:.3f} millimetres")
    elif menu == "4":
        LBL(f"{inputUnit} micrometres = {inputUnit/10000:.3f} centimetres")
    elif menu == "5":
        LBL(f"{inputUnit} micrometres = {inputUnit/100000:.3f} decimetre")
    elif menu == "6":
        LBL(f"{inputUnit} micrometres = {inputUnit/1000000:.3f} metres")
    elif menu == "7":
        LBL(f"{inputUnit} micrometres = {inputUnit/1000000:.3f} kilometres")
    elif menu == "8":
        LBL(f"{inputUnit} micrometres = {inputUnit/25400:.3f} inches")
    elif menu == "9":
        LBL(f"{inputUnit} micrometres = {inputUnit/304800:.3f} feet")
    elif menu == "10":
        LBL(f"{inputUnit} micrometres = {inputUnit/914400:.3f} yards")
    elif menu == "11":
        LBL(f"{inputUnit} micrometres = {inputUnit/1609340000:.3f} miles")
    elif menu == "12":
        LBL(f"{inputUnit} micrometres = {inputUnit/1852000000:.3f} nautical miles")
    elif menu == "I":
        LBL("Info is not finished yet!")   
    elif menu == "L":
        convertLength()
    elif menu == "M":
        mainMenu()
    elif menu == "Q":
        quitProgram()
    convertLengthMicrometre()

# Length Converter - Millimetre
def convertLengthMillimetre():
    LBL("""\nConvert to:
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
I) Info
L) Back to length converter
M) Back to main menu
Q) Quit\n""")
    menu = LBLInput("Chose from options 1-12, I, L, M or Q: ").upper()
    inputUnit = LBLFloatInput("Enter the number of millimetres: ")
    if menu == "1":
        LBL(f"{inputUnit} millimetres = {inputUnit*1000000000:.3f} picometres")
    elif menu == "2":
        LBL(f"{inputUnit} millimetres = {inputUnit*1000000:.3f} nanometres")
    elif menu == "3":
        LBL(f"{inputUnit} millimetres = {inputUnit*1000:.3f} micrometres")
    elif menu == "4":
        LBL(f"{inputUnit} millimetres = {inputUnit/10:.3f} centimetres")
    elif menu == "5":
        LBL(f"{inputUnit} millimetres = {inputUnit/100:.3f} decimetre")
    elif menu == "6":
        LBL(f"{inputUnit} millimetres = {inputUnit/1000:.3f} metres")
    elif menu == "7":
        LBL(f"{inputUnit} millimetres = {inputUnit/1000000:.3f} kilometres")
    elif menu == "8":
        LBL(f"{inputUnit} millimetres = {inputUnit/25.4:.3f} inches")
    elif menu == "9":
        LBL(f"{inputUnit} millimetres = {inputUnit/304.8:.3f} feet")
    elif menu == "10":
        LBL(f"{inputUnit} millimetres = {inputUnit/914.4:.3f} yards")
    elif menu == "11":
        LBL(f"{inputUnit} millimetres = {inputUnit/1609340:.3f} miles")
    elif menu == "12":
        LBL(f"{inputUnit} millimetres = {inputUnit/1852000:.3f} nautical miles")
    elif menu == "I":
        LBL("Info is not finished yet!")   
    elif menu == "L":
        convertLength()
    elif menu == "M":
        mainMenu()
    elif menu == "Q":
        quitProgram()
    convertLengthMillimetre()

# Length Converter - Centimetre
def convertLengthCentimetre():
    LBL("""\nConvert to:
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
I) Info
L) Back to length converter
M) Back to main menu
Q) Quit\n""")
    menu = LBLInput("Chose from options 1-12, I, L, M or Q: ").upper()
    inputUnit = LBLFloatInput("Enter the number of centimetres: ")
    if menu == "1":
        LBL(f"{inputUnit} centimetres = {inputUnit*10000000000:.3f} picometres")
    elif menu == "2":
        LBL(f"{inputUnit} centimetres = {inputUnit*10000000:.3f} nanometres")
    elif menu == "3":
        LBL(f"{inputUnit} centimetres = {inputUnit*10000:.3f} micrometres")
    elif menu == "4":
        LBL(f"{inputUnit} centimetres = {inputUnit*10:.3f} millimetres")
    elif menu == "5":
        LBL(f"{inputUnit} centimetres = {inputUnit/100000:.3f} decimetre")
    elif menu == "6":
        LBL(f"{inputUnit} centimetres = {inputUnit/100000000:.3f} metres")
    elif menu == "7":
        LBL(f"{inputUnit} centimetres = {inputUnit/100000000000:.3f} kilometres")
    elif menu == "8":
        LBL(f"{inputUnit} centimetres = {inputUnit/2.54:.3f} inches")
    elif menu == "9":
        LBL(f"{inputUnit} centimetres = {inputUnit/30.48:.3f} feet")
    elif menu == "10":
        LBL(f"{inputUnit} centimetres = {inputUnit/91.44} yards")
    elif menu == "11":
        LBL(f"{inputUnit} centimetres = {inputUnit/160934:.3f} miles")
    elif menu == "12":
        LBL(f"{inputUnit} centimetres = {inputUnit/185200:.3f} nautical miles")
    elif menu == "I":
        LBL("Info is not finished yet!")   
    elif menu == "L":
        convertLength()
    elif menu == "M":
        mainMenu()
    elif menu == "Q":
        quitProgram()
    convertLengthCentimetre()

# Length Converter - Decimetre
def convertLengthDecimetre():
    LBL("""\nConvert to:
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
I) Info
L) Back to length converter
M) Back to main menu
Q) Quit\n""")
    menu = LBLInput("Chose from options 1-12, I, L, M or Q: ").upper()
    inputUnit = LBLFloatInput("Enter the number of decimetres: ")
    if menu == "1":
        LBL(f"{inputUnit} decimetres = {inputUnit*100000000000:.3} picometres")
    elif menu == "2":
        LBL(f"{inputUnit} decimetres = {inputUnit*100000000:.3} nanometres")
    elif menu == "3":
        LBL(f"{inputUnit} decimetres = {inputUnit*100000:.3} micrometres")
    elif menu == "4":
        LBL(f"{inputUnit} decimetres = {inputUnit*100:.3} millimetres")
    elif menu == "5":
        LBL(f"{inputUnit} decimetres = {inputUnit*10:.3} centimetres")
    elif menu == "6":
        LBL(f"{inputUnit} decimetres = {inputUnit/10000000:.3} metres")
    elif menu == "7":
        LBL(f"{inputUnit} decimetres = {inputUnit/10000000000:.3} kilometres")
    elif menu == "8":
        LBL(f"{inputUnit} decimetres = {inputUnit/0.254:.3} inches")
    elif menu == "9":
        LBL(f"{inputUnit} decimetres = {inputUnit/3.048:.3} feet")
    elif menu == "10":
        LBL(f"{inputUnit} decimetres = {inputUnit/9.144:.3} yards")
    elif menu == "11":
        LBL(f"{inputUnit} decimetres = {inputUnit/16093.4:.3} miles")
    elif menu == "12":
        LBL(f"{inputUnit} decimetres = {inputUnit/18520:.3} nautical miles")
    elif menu == "I":
        LBL("Info is not finished yet!")   
    elif menu == "L":
        convertLength()
    elif menu == "M":
        mainMenu()
    elif menu == "Q":
        quitProgram()
    convertLengthDecimetre()

# Length Converter - Metre
def convertLengthMetre():
    LBL("""\nConvert to:
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
I) Info
L) Back to length converter
M) Back to main menu
Q) Quit\n""")
    menu = LBLInput("Chose from options 1-12, I, L, M or Q: ").upper()
    inputUnit = LBLFloatInput("Enter the number of metres: ")
    if menu == "1":
        LBL(f"{inputUnit} metres = {inputUnit*1000000000000:.3f} picometres")
    elif menu == "2":
        LBL(f"{inputUnit} metres = {inputUnit*1000000000:.3f} nanometres")
    elif menu == "3":
        LBL(f"{inputUnit} metres = {inputUnit*1000000:.3f} micrometres")
    elif menu == "4":
        LBL(f"{inputUnit} metres = {inputUnit*1000:.3f} millimetres")
    elif menu == "5":
        LBL(f"{inputUnit} metres = {inputUnit*100:.3f} centimetres")
    elif menu == "6":
        LBL(f"{inputUnit} metres = {inputUnit*10:.3f} decimetres")
    elif menu == "7":
        LBL(f"{inputUnit} metres = {inputUnit/1000:.3f} kilometres")
    elif menu == "8":
        LBL(f"{inputUnit} metres = {inputUnit/0.0254:.3f} inches")
    elif menu == "9":
        LBL(f"{inputUnit} metres = {inputUnit/0.3048:.3f} feet")
    elif menu == "10":
        LBL(f"{inputUnit} metres = {inputUnit/0.9144:.3f} yards")
    elif menu == "11":
        LBL(f"{inputUnit} metres = {inputUnit/1609.34:.3f} miles")
    elif menu == "12":
        LBL(f"{inputUnit} metres = {inputUnit/1852:.3f} nautical miles")
    elif menu == "I":
        LBL("Info is not finished yet!")   
    elif menu == "L":
        convertLength()
    elif menu == "M":
        mainMenu()
    elif menu == "Q":
        quitProgram()
    convertLengthMetre()

# Length Converter - Kilometre
def convertLengthKilometre():
    LBL("""\nConvert to:
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
I) Info
L) Back to length converter
M) Back to main menu
Q) Quit\n""")
    menu = LBLInput("Chose from options 1-12, I, L, M or Q: ").upper()
    inputUnit = LBLFloatInput("Enter the number of kilometres: ")
    if menu == "1":
        LBL(f"{inputUnit} kilometres = {inputUnit*1000000000000000:.3f} picometres")
    elif menu == "2":
        LBL(f"{inputUnit} kilometres = {inputUnit*1000000000000:.3f} nanometres")
    elif menu == "3":
        LBL(f"{inputUnit} kilometres = {inputUnit*1000000000:.3f} micrometres")
    elif menu == "4":
        LBL(f"{inputUnit} kilometres = {inputUnit*1000000:.3f} millimetres")
    elif menu == "5":
        LBL(f"{inputUnit} kilometres = {inputUnit*100000:.3f} centimetres")
    elif menu == "6":
        LBL(f"{inputUnit} kilometres = {inputUnit*10000:.3f} decimetres")
    elif menu == "7":
        LBL(f"{inputUnit} kilometres = {inputUnit*1000:.3f} metres")
    elif menu == "8":
        LBL(f"{inputUnit} kilometres = {inputUnit/0.0000254:.3f} inches")
    elif menu == "9":
        LBL(f"{inputUnit} kilometres = {inputUnit/0.0003048:.3f} feet")
    elif menu == "10":
        LBL(f"{inputUnit} kilometres = {inputUnit/0.0009144:.3f} yards")
    elif menu == "11":
        LBL(f"{inputUnit} kilometres = {inputUnit/1.60934:.3f} miles")
    elif menu == "12":
        LBL(f"{inputUnit} kilometres = {inputUnit/1.852:.3f} nautical miles")
    elif menu == "I":
        LBL("Info is not finished yet!")
    elif menu == "L":
        convertLength()
    elif menu == "M":
        mainMenu()
    elif menu == "Q":
        quitProgram()
    convertLengthKilometre()

# quit program
def quitProgram():
    LBL("\nQuitting program!")
    quit()

# main menu
def mainMenu():
    LBL("""Welcome to my unit converter!
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
I) Info
Q) Quit\n""")
    menu = LBLInput("Chose from options 1-11, I or Q: ").upper()
    if menu == "1":
        convertLength()
    elif menu == "2":
        # convertArea()
        LBL("Not finished yet!")
    elif menu == "3":
        # convertVolume()
        LBL("Not finished yet!")
    elif menu == "4":
        # convertTime()
        LBL("Not finished yet!")
    elif menu == "5":
        # convertSpeed()
        LBL("Not finished yet!")
    elif menu == "6":
        # convertAcceleration()
        LBL("Not finished yet!")
    elif menu == "7":
        # convertMass()
        LBL("Not finished yet!")
    elif menu == "8":
        # convertPressure()
        LBL("Not finished yet!")
    elif menu == "9":
        # convertEnergy()
        LBL("Not finished yet!")
    elif menu == "10":
        # convertForce()
        LBL("Not finished yet!")
    elif menu == "11":
        # convertTemperature()
        LBL("Not finished yet!")
    elif menu == "I":
        LBL("Info is not finished yet!")
    elif menu == "Q":
        quitProgram()
    mainMenu()

# main code
mainMenu()