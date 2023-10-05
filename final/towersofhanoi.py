#-----------------------------------------------------------------------
# towersofhanoi.py
#-----------------------------------------------------------------------

import sys
import stdio
import stddraw

TotalMoves = []



#-----------------------------------------------------------------------

# Write to standard output instructions to move n Towers of Hanoi
# disks to the left (if parameter left is True) or to the right (if
# parameter left is False).

def moves(n, left):
    if n == 0:
        return
    moves(n-1, not left)
    TotalMoves.append(n)
    if left:
        stdio.writeln(str(n) + ' left')
        TotalMoves.append('left')
    else:
        stdio.writeln(str(n) + ' right')
        TotalMoves.append('right')
    moves(n-1, not left)




def Visuals(TotalMoves, n):
    Tower1Possibilities[5, 4, 3, 2, 1]
    Tower2Possibilities[5, 4, 3, 2, 1]
    Tower3Possibilities[5, 4, 3, 2, 1]
    index = 0
    i = 0
    while i <= len(TotalMoves):
        stddraw.filledRectangle(0, 0, 1, .2)
        stddraw.filledRectangle(.15, .2, .1, .8)
        stddraw.filledRectangle(.45, .2, .1, .8)
        stddraw.filledRectangle(.75, .2, .1, .8)
        SelectedRing = TotalMoves[index]
        index += 1
        SelectedMove = TotalMoves[index]
        index += 1

        i += 1
        stddraw.show()
    

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard output
# instructions to move n Towers of Hanoi disks to the left.

def main():
    n = int(sys.argv[1])
    moves(n, True)
    Visuals(TotalMoves)
    print(TotalMoves, n)

if __name__ == '__main__':
    main()
    
#-----------------------------------------------------------------------