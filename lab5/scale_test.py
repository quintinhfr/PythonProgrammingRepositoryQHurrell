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
    source = Picture(File)
    target = scale(source, Scale_Factor)
    stddraw.setCanvasSize(target.width(), target.height())
    stddraw.picture(target)
    stddraw.show()

if __name__ == "__main__":
    main()
    
