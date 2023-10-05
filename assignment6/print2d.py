import stdarray
import stdio
import sys
import math
import random

i = 0

a = 0

#I chose to use the same boolean array as the book, since 
#this program isn't supposed to accept command line arguments

bools = [[True, True, False, False],
         [False, True, False, True],
         [True, True, True, True],
         [False, False, True, False]] 


#designed to update each individual index to find the location of the corresponding symbol
#whether it is a space or "*"

while a < 4 and i < 15:
    if i == 3:
        a += 1
    if i == 7:
        a += 1
    if i == 11:
        a += 1
    if i == 15:
        a += 1
    while i < 15:
        if i == 0 and a == 0:
            bools[a][i] = '*'
        if i == 1 and a == 0:
            bools[a][i] = '*'
        if i == 2 and a == 0:
            bools[a][i] = " "
        if i == 3 and a == 0:
            bools[a][i] = " "
        if i == 4 and a == 1:
            bools[a][i] = ' '
        if i == 5 and a == 1:
            bools[a][i] = '*'
        if i == 6 and a == 1:
            bools[a][i] = " "
        if i == 7 and a == 1:
            bools[a][i] = "*"
        if i == 8 and a == 2:
            bools[a][i] = '*'
        if i == 9 and a == 2:
            bools[a][i] = '*'
        if i == 10 and a == 2:
            bools[a][i] = "*"
        if i == 11 and a == 2:
            bools[a][i] = "*"
        if i == 12 and a == 3:
            bools[a][i] = ' '
        if i == 13 and a == 3:
            bools[a][i] = ' '
        if i == 14 and a == 3:
            bools[a][i] = "*"
        if i == 15 and a == 3:
            bools[a][i] = " "
        i += 1
           

stdio.writeln(bools)