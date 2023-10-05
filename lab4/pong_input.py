import stddraw
import stdio
import math
import random


def paddle_creation():
    #the coordinates are for the bottom left hand corner
    p1_pdl_x = 10
    p1_pdl_y = 40
    p1_pdl_w = 3
    p1_pdl_h = 20
    stddraw.filledRectangle(p1_pdl_x, p1_pdl_y, p1_pdl_w, p1_pdl_h)
    
    # to get the x coordinate for the 2nd paddle, I had to subract 13 fromm 100
    #10 so that I am equally far away from the edge as p1, and the extra 3 for the width
    #of the rectangle

    p2_pdl_x = 87
    p2_pdl_y = 40
    p2_pdl_w = 3
    p2_pdl_h = 20
    stddraw.filledRectangle(p2_pdl_x, p2_pdl_y, p2_pdl_w, p2_pdl_h)

def key_detection():
    # Function prints out keyboard player movement info to terminal for debugging
    if stddraw.hasNextKeyTyped():
        CurrentKey = stddraw.nextKeyTyped()
        if CurrentKey == 'w':
            print ("p1 up")
        if CurrentKey == 's':
            print ("p1 down")
        if CurrentKey == 'i':
            print ("p2 up")
        if CurrentKey == 'k':
            print ("p2 down")
    else:
        return None
    


def ball_creation():
    stddraw.point(50, 50)

def paddle_movement():
    pass

def window_creation():
    stddraw.setCanvasSize(800, 800)
    stddraw.setXscale(0, 100)
    stddraw.setYscale(0, 100)

def collision_detection():
    pass

def main():
    window_creation()
    while True:
        stddraw.clear()
        key_detection()
        paddle_creation()
        ball_creation()
        paddle_movement()
        collision_detection()
        stddraw.show(10)
        

if __name__ == '__main__':
    main()

