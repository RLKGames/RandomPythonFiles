# v1.0
### Additions
- Prime number generator
- Square number generator


# v1.1
### Additions
- Rock paper scissors
### Changes
- Removed unnecessary lines of code from PrimeNumberGenerator.py
- Removed unnecessary lines of code from SquareNumberGenerator.py
- Renamed "Square Number Generator.py" to "SquareNumberGenerator.py"
- Renamed "Prime Number Generator.py" to "PrimeNumberGenerator.py"


# v1.1.1
### Changes
- Made the rock paper scissors code slightly more efficient
### Bug fixes
- Removed test code


# v1.2
### Additions
- Number guessing game


# v1.3
### Additions
- Number factors generator
### Changes
- Made prime number generator and square number generator code slightly more efficient


# v1.4
### Additions
- Added cube number generator
### Bug fixes
- Rewritten the square number generator to fix it, as a side effect it is also faster


# v1.4.1
### Changes
- Made prime number generator file saving code better
- Made number factor generator file saving code better
### Bug fixes
- Fixed number factor generator saving to files named "PrimeNumberGeneratorOutput" 🤦


# v2.0
### Additions
- Added Random Number Generator to NumberGenerators.py to generate random numbers within a user-specified range
- Added Exponent of Number Generator to NumberGenerators.py to generate result of multiplying a number by itself a specified number of times
### Changes
- Renamed Number guessing game.py to NumberGuessingGame.py
- Merged PrimeNumberGenerator.py and NumberFactorsGenerator.py into one file called NumberGenerators.py
- Changed almost all text to print letter by letter rather than line by line because it looks better
- Moved everything into functions because 1) easier to maintain and 2) apparently it runs faster
- Added Exponent Generator to NumberGenerators.py to serve the purpose of SquareNumberGenerator.py and CubeNumberGenerator.py but with more options
- Improved file saving and printing code
- Improved error code handling
**Improvements made to prime number generator in NNumberGenerators.py:**
- Runs approx 7x faster (Tested with 50,000: takes 5.72s instead of 41.54s)
- Lists how many numbers are generated after it has been run
**Improvements made in the switch to exponent number generator in NumberGenerators.py:**
- Can now generate numbers based on any exponent
- Fixed cube number generator
- Square gen runs approx 12x faster (Tested with 5,000,000: takes 1.12s instead of 14.02s) (The old one froze VSCode during the first test LOL)
- Cube gen runs (Tested with 5,000,000: takes 1.07s instead of not working...)
- Lists how many numbers are generated after it has been run
- KNOWN ISSUE: Will become inaccurate at some point due to floating point inaccuracies. I'll try to find a fix but idk how. I tested it up to 1 billion and it was still accurate
- Note: If a mathematician could help me with phrasing for this thing, that'd be much appreciated
**Improvements made to number factors generator in NumberGenerators.py:**
- Runs approx 150x faster (Tested with 5,000,000: takes 0.1s instead of 15.55s)
- Lists how many numbers are generated after it has been run
**Improvements made to RockPaperScissors.py:**
- Changed if statement to switch statement (it's called a match statement in python for some reason)
- Improved error code handling
- Added prompt asking if the user wants to play again
**Improvements made to NumberGuessingGame.py:**
- Improved error code handling
- Added prompt asking if the user wants to play again
### Bug fixes
- All previous bugs should be fixed (hopefully)


# v2.1
### Additions
- Created DiceRoll.py
- Created CoinFlip.py
- Created UnitConverter.py (can currently only convert between metric length units)
### Bug Fixes
- Fix time output in prime number generator
- Removed un-needed functions from rockPaperScissors.py


# v3.0
### Additions
- Created Main.py to be used as a way of opening the python files. The files can still be opened manually
## Changes
- UnitConverter.py now prints all conversion outputs letter by letter
- Switched to using f strings in all files for speed improvements
- Edited number factors generator in NumberGenerators.py so it doesn't calculate things that cannot be a factor of the number
- Improved output of random number generator in NumberGenerators.py
- Slightly improved prime number generator code to increase speed
## Bug fixes
- Fix exponent of number generator
- Remove unneeded debug code from UnitConverter.py
- Remove unneeded debug code from prime number generator in NumberGenerators.py
## Known Issues
- **Exponent of number generator** has a low limit because it exceeds python's string to integer conversion limit of 4300 digits. EG 2 can only be done up to 14,284
- **Exponent number generator** is still inaccurate at high numbers due floating point inaccuracies. I'll try to find a fix but idk how. I tested it up to 1 billion and it was still accurate
## Speed changes
Tested in python 3.12.3
Tested 3 times and averaged, outliers were ignored and re-tested
All numbers have been rounded to 2dp
**CoinFlip.py (tested with 1,000,000 coins)**
v2.1 - 12.17s
v3.0 - 10.04s
**DiceRoll.py (tested with 1,000,000 6-sided dice)**
v2.1 - 12.43s
v3.0 - 9.73s
### Speed changes to NumberGenerators.py 
Tested in python 3.12.3.
Tested 3 times and averaged, outliers were ignored and re-tested
All numbers have been rounded to 2dp
**Prime number generator (tested with 1-50,000)**
v1.4.1 - 39.47s
v2.0 - 5.75s
v3.0 - 5.66s
**Exponent of number generator (tested with 2 and 14,284)**
v2.0 - broken
v3.0 - 2.7s
**Exponent number generator (tested with 2 and 1-10,000,000)**
v1.4.1 - 28.26s
v2.0 - 2.25s
v3.0 - 2.24s
**Exponent number generator (tested with 3 and 1-10,000,000)**
v1.4.1 - broken
v2.0 - 2.13s
v3.0 - 2.15s
**Number factor generator (tested with 1,000,000,000)**
v1.4.1 - 31.87s
v2.0 - 19.76s
v3.0 - 9.52s
**Random number generator (tested with 1-10,000 and 1,000,000)**
v2.0 - 12.1s
v3.0 - 10.09s