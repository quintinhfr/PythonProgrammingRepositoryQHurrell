import stddraw

# This code was a modified version of the shell code given in the lab packet

x_coord = .5
y_coord = .5

velocity = .01

while True:
    #Reset Background, switch to a new frame
    stddraw.clear()

    # This is the code for the triangle
    stddraw.line(.25, .25, .75, .25)
    stddraw.line(.75, .25, .5, .75)
    stddraw.line(.25, .25, .5, .75)

    #Point
    stddraw.point(x_coord, y_coord)

    stddraw.show(15)

    if (y_coord + velocity) >= .75 or (y_coord + velocity) <= .25:
        velocity = -velocity

    #New Ball Location
    y_coord = y_coord + velocity