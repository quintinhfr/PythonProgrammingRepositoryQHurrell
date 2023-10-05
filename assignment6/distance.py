import stdio
import sys
import math
import random

#n determines what dimension the object is in, so 
#it takes command lline arguments that consist of 1-4 
# - 1 being 1D, 2 being 2D, 3 being 3D, and 4 being 4D

n = int(sys.argv[1])

#random vector coordinate picking

vector1 = [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)]
vector2 = [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)]
Total = 0

#calculates the formula inside the square root

for i in range(n):
    Total += (vector2[i] - vector1[i])**2

#finishes the equation by adding in the square root

Final = math.sqrt(Total)

#writes the final answer in terminal

stdio.writeln(Final)
 