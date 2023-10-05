
# matrix.py
#-----------

#---------------------------------------------------
# NOTE-----
# I had to reference the booksite answer a few times 
# due to a lack of understanding of this topic
# The second half of this assignment is mostly from 
# the booksite answer
#---------------------------------------------------

#------------------
import math
import stdarray
import random
import stdio
import sys
#------------------

#-----------------------------------------------------------------

#creates an m by n matrix containing random floats between 0 and 1

def rand(m, n):
    i = 0
    j = 0
    NewMatrix = stdarray.create2D(m, n, None)
    while i < m:
        j = 0
        while j < n:
            NewMatrix[i][j] = random.random()
            j += 1
        i += 1
    return NewMatrix

#------------------------------------------------------------------

def identity(n):
    
    # create an n by n identity matrix
    
    NewMatrix = stdarray.create2D(n, n, None)
    i = 0
    while i < n:
        j = 0
        while j < n:
            NewMatrix[i][j] = 1
            j += 1
        i += 1
    
    return NewMatrix

#------------------------------------------------------------------

# Gives the dot product of vectors v1 and v2

def dot(v1, v2):
    Vector1 = v1

    NewDot = 0
    i = 0

    while i < Vector1:
        NewDot += v1 * i[i] * v2 * 1[i]
        i += 1

    return NewDot

#-------------------------------------------------------------------

#I didn't understand what this one was asking, I used the book heavily

# Transpose matrix "m"

def transpose(m):
    rowCount = len(m)
    colCount = len(m)
    NewMatrix = stdarray.create2D(m, m, 0)
    for row in range(rowCount):
        for col in range(colCount):
            NewMatrix[col][row] = m[row][col]
    return NewMatrix


#-------------------------------------------------------------------

# Return the sum of Matrix 1 and 2

def add(m1, m2):
    rowCount = len(m1)
    colCount = len(m1)

    total = stdarray.create2D(rowCount, colCount, 0)
    for row in range(colCount):
        for col in range(colCount):
            total[row][col] = m1[row][col] + m2[row][col]

#--------------------------------------------------------

# Return the difference of Matrix 1 and 2

def subtract(m1, m2):
    Rows = len(m1)
    Columns = len(m1[0])
    
    different = stdarray.create2D(Rows, Columns, 0)
    for row in range(Rows):
        for col in range(Columns):
            diff[row][col] = m1[row][col] - m2[row][col]
    return different
    

#---------------------------------------------------------

# Return the product of Matric 1 and 2

def multiplyMM(m1, m2):
    m1RowCount = len(m1)
    m1ColCount = len(m1[0])
    m2RowCount = len(m2)
    m2ColCount = len(m2[0])

    NewProd = stdarray.create2D(m1RowCount, m2ColCount, 0)
    for i in range(m1RowCount):
        for J in range(m2ColCount):
            for k in range(m1ColCount):
                NewProd[i][j] += m1[i][k] * m2[k][j]
    return NewProd


#-----------------------------------------------------------

# return the vector of the product of m and v

def multiplyMV(m, v):
    mRowCount = len(m)
    mColCount = len(m[0])

    NewProd = stdarray.create1D(mRowCount, 0)
    for i in range(mRowCount):
        for j in range(mColCount):
            NewProd[i] += m[i][j] * v[j]
    return NewProd

#-----------------------------------------------------------



def multiplyVM(v, m):
    vLength = len(v)
    mRowCount = len(m)
    mColCount = len(m[0])
    

    NewProd = stdarray.create1D(mColCount, 0)
    for j in range(mColCount):
        for i in range(mRowCount):
            NewProd[j] += m[i][j] * v[i]
    return NewProd


#-----------------------------------------------------------

def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    

    # Test Cases

    Answer1 = rand(m, n)
    stdio.writeln("rand = ")
    stdio.writeln(Answer1)

    Answer2 = identity(n)
    stdio.writeln("identity = ")
    stdio.writeln(Answer2)

    Answer3 = dot(m, n)
    stdio.writeln("dot = ")
    stdio.writeln(Answer3)

    Answer4 = transpose(m)
    stdio.writeln("transpose = ")
    stdio.writeln(Answer4)

    Answer5 = add(m, n)
    stdio.writeln("add = ")
    stdio.writeln(Answer5)

    Answer6 = subtract(m, n)
    stdio.writeln("subtract = ")
    stdio.writeln(Answer6)

    Answer7 = multiplyMM(m, n)
    stdio.writeln("multiplyMM = ")
    stdio.writeln(Answer7)
        
    Answer8 = multiplyMV(m, n)
    stdio.writeln("multiplyMV = ")
    stdio.writeln(Answer8)

    Answer9 = multiplyVM(m, n)
    stdio.writeln("multiplyVM = ")
    stdio.writeln(Answer9)

    
# NOTE ---- I heavily used to booksite answer, 
# especially for the last half, Credit goes to the booksite

if __name__ == '__main__':
    main()



