import stddraw

#This program is a modified version of the shell code given in the lab packet

x_coord = .25
y_coord = .25

x_coord2 = .75
y_coord2 = .75

velocity = .01

while True:
    #Clear for next frame
    stddraw.clear()

    #bottom left square

    stddraw.line(0, 0, 0, .5)
    stddraw.line(0, .5, .5, .5)
    stddraw.line(.5, .5, .5, 0)
    stddraw.line(0, 0, .5, 0)

    #top right square

    stddraw.line(.5, .5, .5, 1)
    stddraw.line(.5, 1, 1, 1)
    stddraw.line(1, 1, 1, .5)
    stddraw.line(1, .5, .5, .5)

    #Draw both points in their respective squares
    stddraw.point(x_coord2, y_coord2)
    stddraw.point(x_coord, y_coord)

    stddraw.show(10)

    #This is for the Bottom Left Corner's Ball Movement
    if (x_coord + velocity) >= .5 or (x_coord + velocity) <= 0:
        velocity = -velocity

    # Get new coordinates for first ball
    x_coord = x_coord + velocity

    #This is for the Top Right Hand Corner's Ball Movement
    if (x_coord2 + velocity) >= 1 or (x_coord2 + velocity) <= .5:
        velocity = -velocity

    # Get new coordinates for the second ball
    x_coord2 = x_coord2 + velocity
    y_coord2 = y_coord2 + velocity
