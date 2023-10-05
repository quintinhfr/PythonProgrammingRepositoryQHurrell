import sys
import random
import stdio
import stdarray

Rows = stdio.readInt()

Columns = stdio.readInt()

TotalGridPoints = (Rows * Columns)

TotalRowSize = (TotalGridPoints / Columns)

TotalColumnSize = (TotalGridPoints / Rows)

Grid = stdarray.create2D(Rows, Columns, 0)

TotalPointCounter = 0

#i is the column
i = 0 

#j is the Row
j = 0



#This loop fills the 2D array with the values
#if "i" == columns then that means you need to change
#"j" and set "i" to 0 to start the next row

while TotalPointCounter < TotalGridPoints:
    if i == (Columns):
        i = 0
        j += 1
    CurrentAltitude = stdio.readInt()
    Grid[j][i] = CurrentAltitude
    i += 1
    TotalPointCounter += 1

#i and j are essentially your coordinates, 
#you change i if you want to go East or West
#you change j if you want to go North or South

i = 0

j = 0

#new place holders for each direction

East = 0

West = 0

North = 0

South = 1

#This is a ticker that keeps track of which directions are lower than the current location

ValidDirections = 0

#reset total point counter

TotalPointCounter = 0

#Ticker that keeps track of the total numner of peaks

NumberOfPeaks = 0

#calculate whether the altitude of the direction peak is lower than the current location or not

while TotalPointCounter < TotalGridPoints:
    if i == (Columns):
        i = 0
        j += 1

    CurrentLocation = Grid[j][i]

    if East == West:
        i += 1
        if Grid[j][i] < CurrentLocation:
            ValidDirections += 1
        East += 1
        i -= 1
        
        if West == North:
            i -= 1
            if Grid[j][i] < CurrentLocation:
                ValidDirections += 1
            West += 1
            i += 1

            if North == South:
                j += 1
                if Grid[j][i] < CurrentLocation:
                    ValidDirections += 1
                North += 1
                j -= 1
    
                if South == East:
                    j -= 1
                    if Grid[j][i] < CurrentLocation:
                        ValidDirections += 1
                    South =+ 1
                    j += 1

                    if ValidDirections == 4:
                        NumberOfPeaks += 1
    
    #if Valid Directions == 4 then that means that each 
    #specific direction had a lower altitude than the current location, 
    #therefore, it is a peak

    #reset ValidDirections for next loop
    
    ValidDirections = 0

    TotalPointCounter += 1

    i += 1
    
    

stdio.writeln(Grid)
stdio.writeln(NumberOfPeaks)