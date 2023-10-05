import stddraw

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

#plotting Points

stddraw.point(.25, .25)

stddraw.point(.75, .75)


stddraw.show()