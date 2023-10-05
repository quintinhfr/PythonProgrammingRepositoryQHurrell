import math
import sys
import stdio


x = float((sys).argv[1])
y = float((sys).argv[2])

math.atan2(y, x)

red = (((x ** 2) + (y ** 2)) ** .5)

thetas = y


stdio.writeln(red)

stdio.writeln(math.atan2(y, x))

#I couldn't get this one to work right, not sure what I was doing wrong.