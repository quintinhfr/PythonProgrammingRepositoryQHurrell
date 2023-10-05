import math
import sys
import stdio

# p is the principle, t stands for the time, and r stands for the annual interest rate. Enter arguments in this order - t - p - r

t = float((sys).argv[1])
p = float((sys).argv[2])
r = float((sys).argv[3])
e = 2.7183

stdio.writeln(p * (e ** (r * t)))