import math
import sys
import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

answer1 = bool(a < b + c)
answer2 = bool(b < a + c)
answer3 = bool(c < b + a)

stdio.writeln(answer1==answer2==answer3)
