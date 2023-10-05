#-------------
# client.py
#-------------

import integers
import stdio
import stdarray

#Counting primes

#NOTE - I wasn't really sure what question from back in the book to do,
#so I chose this one and tried my best. I use the "isprime". function for this one.
#WARNING - it takes a while to run

PrimeFinder = stdarray.create1D(10000000, 0)

i = 0
j = 1

# fill each value of the array with it's corressponding number value

for i in range(len(PrimeFinder)):
    PrimeFinder[i] = j
    j += 1
    i += 1


i = 0
j = 0

for i in range(len(PrimeFinder)):
    if integers.isprime(PrimeFinder[i]) == True:
        j += 1
    else:
        pass
    i += 1

stdio.writeln(j)
    






