import math
import sys
import stdio
import random

#t is the amount of times you play, y is if you stayed, n is if you didn't stay

t = int(sys.argv[1])
y = 0
n = 0

#this is a list of doors for the random module to pick from

doors = [1, 2, 3]

#I created the t == t just so there was a loop. the important part of this is that the prize and the chosen door are picked at random each time. Then, if chosen == prize, y(stay) gets a + 1, if they are not =, then n(not stay) gets a + 1

while t == t:
    prize = (random.choice(doors))
    chosen = (random.choice(doors))
    if chosen == prize: y = y + 1
    else: n = n + 1
    if (n + y == t):
        break
    
#this is where the percentage gets calculated and written

stdio.write("Stay   -- ")
stdio.writeln(y / t)
stdio.write("Change -- ")
stdio.writeln(n / t)
    








