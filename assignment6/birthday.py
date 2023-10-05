import random
import sys
import stdio
import math
import stdarray

#m is the amount of 

m = float(sys.argv[1])
p = 400
attendees = stdarray.create1D(p, -1)
birthday = random.randint(0, 364)
People = 0
i = 0
Total_People = 0

while i < m:
    i += 1
    while birthday not in attendees:
        attendees[People] = birthday
        People += 1
        birthday = random.randint(0, 364)
    Total_People += People

Answer = Total_People / m

stdio.write("Average: ")
stdio.writeln(float(Answer))
    