#solidcolor.py

#Program takes 3 command line arguments between 0 and 255 to create a color

import stdio
import sys
import stddraw
from color import Color
from picture import Picture

# Command Line Arguments

red = int(sys.argv[1])
green = int(sys.argv[2])
blue = int(sys.argv[3])

# Error Messages and Conditions

if red < 0 or red > 255:
    stdio.writeln("Error: Number is out of Range")
    exit()


if green < 0 or green > 255:
    stdio.writeln("Error: Number is out of Range")
    exit()


if blue < 0 or blue > 255:
    stdio.writeln("Error: Number is out of Range")
    exit()


# Create Color

Color1 = Color(red, green, blue)

# Code

# set canvas size to 256 by 256 like the assignment asks

stddraw.setCanvasSize(256, 256)

# we can make 256 our width and height since the dimensions won't change

w = 256
h = 256

#Create the picture

Pic = Picture(w, h)

# Fill in Pixels with the chosen color

for tCol in range(w):
    for tRow in range(h):
        
        Pic.set(tCol, tRow, Color1)

stddraw.picture(Pic)

stddraw.show()


