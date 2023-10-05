import math
import sys
import stdio

# enter temp. then miles per hour

t = float((sys).argv[1])
v = float((sys).argv[2])

answer = (35.74 + (0.6215 * t) + (((0.4275 * t) - 35.75) * (v ** .16)))

stdio.writeln(answer)