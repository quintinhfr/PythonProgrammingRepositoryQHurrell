
#import proper modules

import math
import sys
import stdio

#give the argument, power, and constant a variable

n = int(sys.argv[1])
power = 1
i = 0

#print power until the break statement activates

while i <= n:
    stdio.write(power)
    stdio.write(" ")
    power = 2 * power
    i = i + 1
    if power >= n:
        break
    
   
