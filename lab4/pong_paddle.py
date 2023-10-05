import stddraw
import stdio
import math
import random



#---------------------------------------------------
# CONTROLS - 
# "W" for up and "S" for down as Player 1
# "I" for up and "K" for down as Player 2
#---------------------------------------------------


#Global Variables that we will be using for movements, These are for the 
#default settings when you start the game

#Default Player Coords are the Default Y Coords for both Rectangles
#Paddle Movements start at 0 because they are mutable variables
#that get added or subtracted to the default starting position
#Which makes the rectnagles move



Player1DefaultYCoord = 40
Player2DefaultYCoord = 40
Paddle_Movement_1 = 0
Paddle_Movement_2 = 0

def paddle_creation(a):
    global Player1DefaultYCoord
    global Player2DefaultYCoord
    global Paddle_Movement_1
    global Paddle_Movement_2

    #a = the y Coords

    #the coordinates are for the bottom left hand corner
    #this is the starting position of the first rectangle
    



    if a == 'w':
        Paddle_Movement_1 += 5

    if a == 's':
        Paddle_Movement_1 -= 5

    if a == 'i':
        Paddle_Movement_2 += 5

    if a == 'k':
        Paddle_Movement_2 -= 5

    if a == 0:
        Paddle_Movement_1 += 0
        Paddle_Movement_1 += 0

    p1_pdl_x = 10
    p1_pdl_y = Player1DefaultYCoord + Paddle_Movement_1
    p1_pdl_w = 3
    p1_pdl_h = 20

    stddraw.filledRectangle(p1_pdl_x, p1_pdl_y, p1_pdl_w, p1_pdl_h)
    
    # to get the x coordinate for the 2nd paddle, I had to subract 13 from 100
    #10 so that I am equally far away from the edge as p1, and the extra 3 for the width
    #of the rectangle
    
    #this is the starting position of the second rectangle

    p2_pdl_x = 87
    p2_pdl_y = Player2DefaultYCoord + Paddle_Movement_2
    p2_pdl_w = 3
    p2_pdl_h = 20

    stddraw.filledRectangle(p2_pdl_x, p2_pdl_y, p2_pdl_w, p2_pdl_h)

    
def key_detection():
    # Function prints out keyboard player movement info to terminal for debugging
    if stddraw.hasNextKeyTyped():
        CurrentKey = stddraw.nextKeyTyped()
        if CurrentKey == 'w':
            print ("p1 up")
            return 'w'
        if CurrentKey == 's':
            print ("p1 down")
            return 's'
        if CurrentKey == 'i':
            print ("p2 up")
            return 'i'
        if CurrentKey == 'k':
            print ("p2 down")
            return 'k'
    else:
        return 0
    


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
        KeyDetected = key_detection()
        paddle_creation(KeyDetected)
        ball_creation()
        paddle_movement()
        collision_detection()
        stddraw.show(10)
        

if __name__ == '__main__':
    main()

