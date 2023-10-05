


# sigmoid.py
# Quintin Hurrell
# CISC 120

import math
import sys
import stdio



def signum(a):

    if a < 0:
        return -1

    if a == 0:
        return 0
  
    if a > 0:
        return 1


x = float(sys.argv[1])


Answer = signum(x)

stdio.writeln(Answer)
