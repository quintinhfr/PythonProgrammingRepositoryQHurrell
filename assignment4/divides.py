import math
import sys
import stdio


a = (float(sys.argv[1]) % float(sys.argv[2]))
b = (float(sys.argv[2]) % float(sys.argv[1]))

stdio.writeln(a==0 or b==0)
