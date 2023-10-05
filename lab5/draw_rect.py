
    
#----------
# Lab 5
#----------


import sys
import stddraw
from picture import Picture





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




def main():

    File = sys.argv[1]

    Scale_Factor = float(sys.argv[2])

    CenterZoomXCoord = float(sys.argv[3])
    CenterZoomYCoord = float(sys.argv[4])

    source = Picture(File)

    OriginalWidth = source.width()
    OriginalHeight = source.height()

    target = scale(source, Scale_Factor)

    stddraw.setXscale(0, target.width())
    stddraw.setYscale(0, target.height())

   
    stddraw.setCanvasSize(target.width(), target.height())
    stddraw.picture(target)




    RescaledXCenter = (CenterZoomXCoord * target.width())
    RescaledYCenter = (CenterZoomYCoord * target.height())

    NewXCoord = (RescaledXCenter - (source.width() / 2))
    NewYCoord = (RescaledYCenter - (source.height() / 2))

    stddraw.point(RescaledXCenter, RescaledYCenter)


    stddraw.rectangle(NewXCoord, NewYCoord, source.width(), source.height())


    stddraw.show()

if __name__ == "__main__":
    main()
    