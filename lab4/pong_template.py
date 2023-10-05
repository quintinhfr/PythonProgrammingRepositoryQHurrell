import stddraw
import stdio
import math
import random


def paddle_creation():
    pass

def ball_creation():
    pass

def paddle_movement():
    pass

def window_creation():
    stddraw.setCanvasSize(900, 700)
    stddraw.setXscale(0, 100)
    stddraw.setYscale(0, 100)

def collision_detection():
    pass

def main():
    window_creation()
    while True:
        stddraw.clear()
        paddle_creation()
        ball_creation()
        paddle_movement()
        collision_detection()
        stddraw.show(10)
        

if __name__ == '__main__':
    main()
