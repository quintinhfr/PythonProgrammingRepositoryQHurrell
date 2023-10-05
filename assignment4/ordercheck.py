import math
import sys
import stdio

x = (float(sys.argv[1]))
y = (float(sys.argv[2]))
z = (float(sys.argv[3]))

answer1 = bool(x < y < z)
answer2 = bool(x > y > z)

stdio.writeln(answer1 or answer2)