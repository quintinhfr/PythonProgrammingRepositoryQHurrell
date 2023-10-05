

import sys
import stdio
import math
import random
import stdarray

#NOTE - this program has a bug where the data exceeds the arrays capabilities
#I encountered it rarly and it did get it to happen less often

n = int(sys.argv[1])

m = int(sys.argv[2])

i = 0

People = 0

NumberCheck = 0

PastNumber = 0

CurrentRumorHolder = 0

RumorSpreaders = stdarray.create1D(n, 0)

RumorSpreaders[People] = 0

Yes = 0

TotalPeoplePercentage = 0

AllRunPeople = 0

#we know that if n is 2 or 3 there will be full propagation, 
#so we don't need to loop if this is the case

if 3 != n != 2:
    while i < m:
        i += 1
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
            

        TotalPeoplePercentage += People

        AllRunPeople = n * m

        if People == n:
            Yes += 1
        
#Calculate the percentage of times that there was full propagation

    PercentageOfFullPropagation = ((Yes / m) * 100)

    stdio.write("The Rumor Fully Propagated: ")
    stdio.write(PercentageOfFullPropagation)
    stdio.writeln("% Of The Time")

#calculate the average number of people who heard the rumor

    PercentOfPeopleWhoHeardTheRumor = ((TotalPeoplePercentage / AllRunPeople) * 100)

    stdio.write("Percentage Of People Who Heard The Rumor: ")
    stdio.write(PercentOfPeopleWhoHeardTheRumor)
    stdio.writeln("%")

#here is where we have our premade solutions if n is 2 or 3

if n == 2:
    stdio.writeln("The Rumor Fully Propagated: 100% Of The Time")
    stdio.writeln("Percentage Of People Who Heard The Rumor: 100%")

if n == 3:
    stdio.writeln("The Rumor Fully Propagated: 100% Of The Time")
    stdio.writeln("Percentage Of People Who Heard The Rumor: 100%")






    