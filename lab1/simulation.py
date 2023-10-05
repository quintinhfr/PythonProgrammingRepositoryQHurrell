import stdio
import random
import sys

#n is the amount of units away from the origin the boundaries of the square are on any given side. m is the amount of times the process gets completed.

n = int(sys.argv[1])

m = int(sys.argv[2])

i = 0

total_steps = 0

North = 0
East = 0
South = 0 
West = 0

c = 0

#c is the variable for the step tally

#the random module picks a number in the list (1, 2, 3, 4), this number corresponds to one direction, which results in whether or not North, South, East, or West gets added or subtracted. Notice that they all start at 0, this is to simulate the origin.

while i < m:
    while (abs(North) <= n) and (abs(East) <= n) and (abs(South) <= n) and (abs(West) <= n):
        randomnumber = random.randint(1, 5)
        if randomnumber == 1: North = North + 1 
        if randomnumber == 1: South = South - 1
        if randomnumber == 2: East = East + 1 
        if randomnumber == 2: West = West - 1
        if randomnumber == 3: South = South + 1
        if randomnumber == 3: North = North - 1
        if randomnumber == 4: West = West + 1 
        if randomnumber == 4: East = East - 1
        c = c + 1
        if (abs(East) == n) or (abs(West) == n) or (abs(South) == n) or (abs(North) == n):
            break
    total_steps += c
    i += 1    

#after the repeated calculation the average amount of steps gets calculated and written in the users terminal.

average_steps = total_steps / m
stdio.write('The average number of steps was ')
stdio.writeln(average_steps)