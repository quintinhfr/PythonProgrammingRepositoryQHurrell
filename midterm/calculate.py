import stdio
import stdarray
import sys
import math

#-------------------------------------------------------------------------
#NOTE----This program DOES NOT print to the terminal, it will only
#print the graph on a file called "output.txt" like the assignment asks.
#-------------------------------------------------------------------------

#Total Items is the amount of space we need in total in the array

TotalItems = 0

#the column number is the same because we have a set amount of data columns

Rows = 0

#columns are constant due to the fact that there are a set amount of headings

Columns = 11

#index for while loops

Index = 0

#i is the column index
#j is the row index

i = 0

j = 0



#This code opens the grades.txt text file and finds the number of tokens inside of it

with open("grades.txt") as file:
    FileText = file.read()

TotalItems = len(FileText.split())

#This then calculates the number of Rows in the file
#Along with adding in the "Grades" Column and the "Averages" Row
#by adding 1 to Columns and Rows

Rows = TotalItems / Columns

TotalItems = TotalItems + Rows + 12

Columns = 12

Rows += 1

TotalItems = Rows * Columns


Rows = int(Rows)

Columns = int(Columns)

TotalItems = int(TotalItems)


#Create the 2D Array using the graph dimensions that were just calculated




Chart = stdarray.create2D(Rows, Columns, 0)





#This is a variable that will carry whatever the current token is for printing the headers

CurrentToken = None

#Place Header information in Array (Chart)




while i < 11:
    Chart[j][i] = stdio.readString()
    i += 1

Chart[j][i] = "Grade"




#now to headings are done, so I used a loop to fill in the rest of the information into the array





while j < Rows - 2:
    i = 0
    j += 1
    Chart[j][i] = stdio.readString()
    
    while i < Columns - 2:
        i += 1
        Chart[j][i] = stdio.readFloat()




#Now add the "Average" Heading to the Final Row

i = 0

j = Rows - 1

Chart[j][i] = "Average"



#All Headings and .txt file data are now in the Array


#Now I need to start Calculating Averages, we 
#will start horizontally to calculate the "Grade" portion


#the first row is full of headings so we start in the second row and second column

#reset indexes

i = 0

j = 0


#for the sake of simplicity I made a single letter variable
#represent each specific assignment
#a for HW1, b for Quiz1, c for HW2, d for HW3
#e for Midterm, f for HW4, g for Quiz2, h for HW5, k for HW6
#and m for Final


while j < Rows - 2:
    i = 0
    j += 1
    i += 1
    a = Chart[j][i]
    i += 1
    b = Chart[j][i]
    i += 1
    c = Chart[j][i]
    i += 1
    d = Chart[j][i]
    i += 1
    e = Chart[j][i]
    i += 1
    f = Chart[j][i]
    i += 1
    g = Chart[j][i]
    i += 1
    h = Chart[j][i]
    i += 1
    k = Chart[j][i]
    i += 1
    m = Chart[j][i]
    i += 1
    FINAL_GRADE = ((a + b + c + d + e + f + g + h + k + m) / 10)
    Chart[j][i] = FINAL_GRADE


#now the Average grades per student have been calculated, I
#have to calculate the average in each specific assigment

#Reset Indexes

i = 0

j = 0

GradesAdded = 0



while i < Columns - 1:
    FINAL_AVERAGE = 0
    GradesAdded = 0
    i += 1
    j = 0
    while j < Rows - 1:
        j += 1
        GradesAdded = GradesAdded + Chart[j][i]
        if j == Rows - 1:
            FINAL_AVERAGE = GradesAdded / (Rows - 2)
            Chart[j][i] = FINAL_AVERAGE


#now everything is calculated and I have the data that I need
#Now I created a loop to make the organized chart

#Rest indexes, this time I don't need to offset the 0 index because we
#want to actually index the headings now


i = 0

j = 0

#First, I printed the headings 
#I did this first so that I could easily 
#figure out how I want my spacings




#NOTE ---- This Program uses the standard output redirection from the sys module
#and will does not print to the terminal, only to the file named "output.py"

sys.stdout = open("output.txt", "w")





stdio.writeln("---------------------------------------------------------------------------------")


#Student
stdio.writef('%-9s', Chart[j][i])
i += 1

#HW1
stdio.writef('%-6s', Chart[j][i])
i += 1

#Quiz1
stdio.writef('%-7s', Chart[j][i])
i += 1

#HW2
stdio.writef('%-6s', Chart[j][i])
i += 1

#HW3
stdio.writef('%-6s', Chart[j][i])
i += 1

#Midterm
stdio.writef('%-9s', Chart[j][i])
i += 1

#HW4
stdio.writef('%-6s', Chart[j][i])
i += 1

#Quiz2
stdio.writef('%-7s', Chart[j][i])
i += 1

#HW5
stdio.writef('%-6s', Chart[j][i])
i += 1

#HW6
stdio.writef('%-6s', Chart[j][i])
i += 1

#Final
stdio.writef('%-7s', Chart[j][i])
i += 1

#Grade
stdio.writef('%-7s', Chart[j][i])
i += 1    


stdio.writeln()

#Reset Indexes

i = 0

j = 0

#Each loop will be writing an entire row of the chart

while j < Rows - 1:
    j += 1
    i = 0


    #Student
    stdio.writef('%-9s', Chart[j][i])
    i += 1

    #HW1
    stdio.writef('%-6.4s', Chart[j][i])
    i += 1

    #Quiz1
    stdio.writef('%-7.4s', Chart[j][i])
    i += 1

    #HW2
    stdio.writef('%-6.4s', Chart[j][i])
    i += 1

    #HW3
    stdio.writef('%-6.4s', Chart[j][i])
    i += 1

    #Midterm
    stdio.writef('%-9.4s', Chart[j][i])
    i += 1

    #HW4
    stdio.writef('%-6.4s', Chart[j][i])
    i += 1

    #Quiz2
    stdio.writef('%-7.4s', Chart[j][i])
    i += 1

    #HW5
    stdio.writef('%-6.4s', Chart[j][i])
    i += 1
 
    #HW6
    stdio.writef('%-6.4s', Chart[j][i])
    i += 1

    #Final
    stdio.writef('%-7.4s', Chart[j][i])
    i += 1

    #Grade
    stdio.writef('%-5.5s', Chart[j][i])
    i += 1 
    
    stdio.write("%")  

    stdio.writeln()




    
stdio.writeln("---------------------------------------------------------------------------------")



sys.stdout.close()

#This ends printing to the .txt file

#End Program

    
#--------------------------------------------------------------------------------
#NOTE-----Again, the output of this program DOES NOT get printed to the terminal,
#it only gets printed in a file called "output.txt" as the assignment states
#--------------------------------------------------------------------------------



