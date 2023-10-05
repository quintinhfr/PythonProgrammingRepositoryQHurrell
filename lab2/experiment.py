import sys
import stdio
import math
import random
import stdarray

n = int(sys.argv[1])

LoopCounter = 0

People = 0

NumberCheck = 0

PastNumber = 0

CurrentRumorHolder = 0

RumorSpreaders = stdarray.create1D(n, -1)

RumorSpreaders[People] = 0

if n != 2:
    while People < n:
    
        Tell = random.randrange(n)
        while Tell == PastNumber or Tell == CurrentRumorHolder:
            Tell = random.randrange(n)
        People += 1
        if Tell in RumorSpreaders:
            break
        RumorSpreaders[People] = Tell
  
        PastNumber = CurrentRumorHolder
        CurrentRumorHolder = Tell
        print(CurrentRumorHolder)

if n != 2:
    if People == n:
        stdio.writeln("The Rumor Fully Propagated")
    if People != n:
        stdio.writeln("The Rumor Did Not Fully Propagate")

    Answer = ((People / n) * 100)
    stdio.write("Percent of Propagation: ")
    stdio.write(Answer)
    stdio.writeln("%")

if n == 2:

    stdio.writeln("The Rumor Fully Propagated")
    stdio.writeln("Percent of Propagation: 100%")

    