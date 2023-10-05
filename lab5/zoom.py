
    
#----------
# Lab 5
#----------

#import modules

import sys
import stddraw
from picture import Picture



# define the function that greates a scaled version of the file

def scale(source, scale_factor):
    

    w = round((source.width() * scale_factor))
    h = round((source.width() * scale_factor))
    target = Picture(w, h)

    for tCol in range(w):
        for tRow in range(h):
            sCol = tCol * source.width() // w
            sRow = tRow * source.height() // h
            target.set(tCol, tRow, source.get(sCol, sRow))
    return target

#define a function that takes the zoomed image from the scaled function

def extract_image(scaled_image, XCoord, YCoord, w, h):


    ZoomImage = Picture(w, h)

    for XCoord in range(w):
        for YCoord in range(h):
            ZoomImage.set(XCoord, YCoord, scaled_image.get(XCoord, YCoord))
    return ZoomImage
    

#define main


def main():

    # Original Picture File

    File = sys.argv[1]

    # Command Line Scale Factor

    Scale_Factor = float(sys.argv[2])

    # Coordinates of point that the image will zoom to

    CenterZoomXCoord = float(sys.argv[3])
    CenterZoomYCoord = float(sys.argv[4])


    source = Picture(File)

    OriginalWidth = source.width()
    OriginalHeight = source.height()

    # Create Scaled image

    target = scale(source, Scale_Factor)

    stddraw.setXscale(0, target.width())
    stddraw.setYscale(0, target.height())

   
    stddraw.setCanvasSize(target.width(), target.height())
    stddraw.picture(target)


    #rescale center Coord to target rescale values

    RescaledXCenter = (CenterZoomXCoord * target.width())
    RescaledYCenter = (CenterZoomYCoord * target.height())

    NewXCoord = (RescaledXCenter - (source.width() / 2))
    NewYCoord = (RescaledYCenter - (source.height() / 2))

    #draw the center point

    stddraw.point(RescaledXCenter, RescaledYCenter)

    #draw the rectangle


    stddraw.rectangle(NewXCoord, NewYCoord, source.width(), source.height())

    stddraw.setXscale(0, 1)
    stddraw.setYscale(0, 1)


    SW = source.width()
    SH = source.height()

    #create zoomed image

    ZoomedImage = extract_image(target, NewXCoord, NewYCoord, SW, SH)

    #draw zoomed image

    stddraw.picture(ZoomedImage)

    


    stddraw.show()

if __name__ == "__main__":
    main()
    