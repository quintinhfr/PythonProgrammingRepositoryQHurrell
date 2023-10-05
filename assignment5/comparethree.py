#import modules

import math
import sys
import stdio

#assign arguments to variables

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

#use an "if" statement that writes "equal" or "not equal" depending on the equality of a b and c.

if a==b==c:
    stdio.writeln("equal")
else: stdio.writeln("not equal")