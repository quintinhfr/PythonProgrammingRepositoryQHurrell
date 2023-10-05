import stddraw

#copy the first small triangle file. I noticed that to center the point, all I had
#to do was add .25 to the y value of the coordinate. this means that you can
#center the triangle by simply adding .25 to every y value of every coordinate 
#from the first file.

stddraw.line(.25, .25, .75, .25)
stddraw.line(.75, .25, .5, .75)
stddraw.line(.25, .25, .5, .75)

stddraw.point(.5, .5)

stddraw.show()