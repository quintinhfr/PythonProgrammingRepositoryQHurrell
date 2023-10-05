import sys
import math
import stdio

c = (sys).argv[1]
g = (sys).argv[2]
l = (sys).argv[3]

x = (l-c)

y = (log(.5) * (1 + sin(l)) / (1 - sin(l)))

al = x

all = x

stdio.writeln("x = ")
stdio.write(al)
stdio.writeln("y = ")
stdio.write(all)

# I kept getting a message saying that I couldn't use the (-) sign to subtract c from l, and I couldn't fix it.