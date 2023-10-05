import math
import sys
import stdio

#w is the number the you are trying to find the amount of prime numbers too, y keeps track of numbers that are divisble by 1. n keeps tack of numbers that are divisble by 2. p keeps track of what number the program is checking at any given moment. i is the loopholder. a b and c all represent the division to check if the numbers are prime or not.

w = int(sys.argv[1])
y = 0
n = 0
p = 0
i = 0
a = 1
b = 2
c = 3

#this is my loop, it is made to keep track of how many numbers are divisible by 1, and how many are divisible by 2 and 3. The break statement is what tells the program that you have checked every number in the given range (w). 

while i == i:
    p + 1
    if p / a == int: y = y + 1
    if (p / b) or (p / c) == int: n = n + 1
    i =+ i
    if p >= w:
        break

#this is used to take the difference of the two numbers, giving you the amount of prime numbers in the set. This calulates the numbers that were only divisible by one out of the data set.

answer = y - n
stdio.writeln(answer)

