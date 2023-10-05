python3
import stdio
import sys
import math
import random

#--------------------------------------------------------------------

RandomNumber = random.randint(1, 10)

if RandomNumber > 5:
    stdio.writeln("Greater Than 5")
if RandomNumber < 5:
    stdio.writeln("Less Than 5")
if RandomNumber == 5:
    stdio.writeln("Equals 5")
    
