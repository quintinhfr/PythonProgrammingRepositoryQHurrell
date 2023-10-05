# final_exam.py

# DIRECTIONS

# This game's Commands are the four Cardinal Directions
# North South East West
# In each area, one of these directions will correspond to an item 
# that you can interact with, some will just be descriptions of a view,
# others will be to open doors and enter other rooms.
#
# GAME LAYOUT
#
# The game is designed to be linear up until you reach the hallway
# The hallway allows for moving between the Office, the Hallway itself,
# and the Bathroom freely at the players will. This is until the Player
# interacts with the Picture in the bathroom, this begins the endgame sequence.
# Once you start this sequence and get to the basement, the endgame is linear
# much like the beginning of the game.


import stdio

# Array of all valid commands

ValidCommands = ['North', 'South', 'East', 'West', 'Help', 'Quit']

# Array of just the move/interact commands

MoveCommands = ['North', 'South', 'East', 'West']

i = 0

DocumentCounter = 0

#-----------------------------------------------------------------------------------

# This function will initiate the opening screen when the game first runs

def gamestart():

    """
    Function that creates the text that appears when the game first runs.
    Gives instructions as to what to do next.
    """

    stdio.writeln()
    stdio.writeln("*---------------------*")
    stdio.writeln("Wecome to Q's Adventure")
    stdio.writeln("*---------------------*")
    stdio.writeln()
    stdio.writeln()
    stdio.writeln("DIRECTIONS:")
    stdio.writeln("-----------")
    stdio.writeln("This game is based upon the 4 Cardinal Directions.")
    stdio.writeln("Therefore room interactions are based on these 4 directions.")
    stdio.writeln("The direction you type corresponds to what you interact with.")
    stdio.writeln("Some objects will just give descriptions, others can be used to enter")
    stdio.writeln("new areas.")
    stdio.writeln()
    stdio.writeln("-----------------------------------------------")
    stdio.writeln("To Move - Type 'North' 'South' 'East' or 'West'")
    stdio.writeln("For Help - Type 'Help'")
    stdio.writeln("To Quit - Type 'Quit'")
    stdio.writeln("-----------------------------------------------")
    stdio.writeln()
    stdio.writeln("COMMANDS:")
    stdio.writeln("--------")
    stdio.writeln("North")
    stdio.writeln("South")
    stdio.writeln("East")
    stdio.writeln("West")
    stdio.writeln("Help")
    stdio.writeln("Quit")
    stdio.writeln("-------")
    stdio.writeln()
    stdio.writeln()
    stdio.writeln("-----------------------")
    stdio.writeln("Type North To Begin")
    stdio.writeln("-----------------------")
    stdio.writeln()

#----------------------------------------------------------------------------------

# This function filters all player input.
# It detects what the player types, 
# - if it is 'Quit', the game prints "GAME OVER" and the program stops running.
# - if it is 'Help', the help module appears.
# - if it is one of the four Cardinal Directions then it will return that string,
# allowing for the game to continues
# if it is a string not in the help center, it will result in an Error Message.

def PlayerInput():

    """
    Function that filters user input
    Displays the help information
    Can Quit the game
    And checks to see if the commands are valid
    """

    while i == i:
        stdio.write(">>> ")
        move = stdio.readString()
        if move not in ValidCommands:
            stdio.writeln("Invalid Command")
        if move == 'Quit':
            stdio.writeln("---------")
            stdio.writeln("GAME OVER")
            stdio.writeln("---------")
            quit()
        if move == 'Help':
            stdio.writeln()
            stdio.writeln("-----------")
            stdio.writeln("HELP CENTER")
            stdio.writeln("-----------")
            stdio.writeln()
            stdio.writeln("COMMANDS")
            stdio.writeln("--------")
            stdio.writeln("North")
            stdio.writeln("South")
            stdio.writeln("East")
            stdio.writeln("West")
            stdio.writeln("Help")
            stdio.writeln("Quit")
            stdio.writeln("-------")
 
        if move in MoveCommands:
            return move
            break

#-----------------------------------------------------------------------------------

# After starting the game, this is where you "Spawn".
# This area is the front door of the house.
#
# Something to notice - Each area has a function that describes it, and a 
# function that deals with the decisions that you can make in that area.
#
# Unique area 1

def FrontDoor():

    """
    Prints information about the location: 'FrontDoor'
    """

    stdio.writeln("---------------------------------------------------------------------------")
    stdio.writeln("You find yourself at the front door of Ben McReen's (serial killer) house.")
    stdio.writeln("The LAPD has sent you to this remote location in search of items that could")
    stdio.writeln("present damning evidence in his case.")
    stdio.writeln("Your mission is to get in and get out, without a trace...")
    stdio.writeln("---------------------------------------------------------------------------")
    stdio.writeln()
    stdio.writeln("South - Door")
    stdio.writeln("North - Car")
    stdio.writeln("East - Lake")
    stdio.writeln("West - Wooded Area")
    stdio.writeln()
    stdio.writeln("---------------")
    stdio.writeln("What do you do?")
    stdio.writeln("---------------")
    

#-----------------------------------------------------------------------------------

# Lays out the decisions and their outcomes for FrontDoor.

def FrontDoorDecisions(Choice):

    """
    Prints response to the decisions made in 'FrontDoor'
    """

    if Choice == 'North':
        stdio.writeln("---------------------------------------------------------------")
        stdio.writeln("You examine your Police Car, did you forget to lock it perhaps?")
        stdio.writeln("You aren't leaving this soon.")
        stdio.writeln("---------------------------------------------------------------")
    if Choice == 'East':
        stdio.writeln("------------------------------------------------------------------------")
        stdio.writeln("You admire the beauty of the lake. You fall pray to the distraction, but")
        stdio.writeln("soon remember that you have a task to take care of.")
        stdio.writeln("------------------------------------------------------------------------")
    if Choice == 'West':
        stdio.writeln("-------------------------------------------------------------")
        stdio.writeln("The dark forest is daunting at first, for a city boy and all.")
        stdio.writeln("You suddenly remember that time is of the essence.")
        stdio.writeln("-------------------------------------------------------------")
    if Choice == 'South':
        return True

#----------------------------------------------------------------------------------

# Description of the FirstRoom of the House.
#
# Unique area 2

def FirstRoom():

    """
    Prints information about the location: 'FirstRoom'
    """

    stdio.writeln("-----------------------------------------------------------------------")
    stdio.writeln("You enter the building. The floor is damp and moldy.")
    stdio.writeln("You start to second guess yourself as to if this is worth")
    stdio.writeln("it or not. Soon, you gather yourself and start looking around the room.")
    stdio.writeln("-----------------------------------------------------------------------")
    stdio.writeln()
    stdio.writeln("South - Closet")
    stdio.writeln("North - Where you came from")
    stdio.writeln("East - Window")
    stdio.writeln("West - Door")
    stdio.writeln()
    stdio.writeln("---------------")
    stdio.writeln("What do you do?")
    stdio.writeln("---------------")

#-----------------------------------------------------------------------------------

# Decisions that are possible in the FirstRoom.

def FirstRoomDecisions(Choice):

    """
    Prints response to the decisions made in 'FirstRoom'
    """


    if Choice == 'North':
        stdio.writeln("----------------------------------------------------------------------")
        stdio.writeln("You admire the door from which you came, considering just running away")
        stdio.writeln("----------------------------------------------------------------------")
    if Choice == 'East':
        stdio.writeln("-------------------------------------------------------------------")
        stdio.writeln("The view from the cracked window is haunting.")
        stdio.writeln("The picnic table and play equiptment haven't been touched in years.")
        stdio.writeln("Was he not alone?")
        stdio.writeln("-------------------------------------------------------------------")
    if Choice == 'West':
        stdio.writeln("-----------------")
        stdio.writeln("You open the door")
        stdio.writeln("-----------------")
        return True
    if Choice == 'South':
        stdio.writeln("----------------------------------------------")
        stdio.writeln("You open the closet to see mountains of Pills.")
        stdio.writeln("'They weren't wrong about Ben abusing drugs'")
        stdio.writeln("But back to work, no papers in here.")
        stdio.writeln("----------------------------------------------")

#-----------------------------------------------------------------------------------

# Description of the Hallway
#
# This is where the game becomes more dynamic, You can go back 
# and forth from the 2 side rooms of the Hallway, and the Hallway
# itself.
#
# Unique area 3

def Hallway():

    """
    Prints information about the location: 'Hallway'
    """

    stdio.writeln("------------------------------------------------------------------")
    stdio.writeln("You enter a hallway.")
    stdio.writeln("The rug appears to have bloodstains, and rats cover the floor.")
    stdio.writeln("You see three doors ahead, out of fear, you quickly choose a door.")
    stdio.writeln("------------------------------------------------------------------")
    stdio.writeln()
    stdio.writeln("South - Door (Right Side of Hallway)")
    stdio.writeln("North - Door (Left Side of Hallway)")
    stdio.writeln("East - Where you came from")
    stdio.writeln("West - Door (End of Hallway)")
    stdio.writeln()
    stdio.writeln("---------------")
    stdio.writeln("What do you do?")
    stdio.writeln("---------------")

#-------------------------------------------------------------------------------------------

# Decisions that are possible in the Hallway.

def HallwayDecisions(Choice):

    """
    Prints response to the decisions made in 'Hallway'
    """

    if Choice == 'North':
        stdio.writeln("-------------------")
        stdio.writeln("You Enter Left Door")
        stdio.writeln("-------------------")
        return True
    if Choice == 'East':
        stdio.writeln("----------------------------------------------------------------------")
        stdio.writeln("You glance quickly backwards as you run across the rat infested floor.")
        stdio.writeln("----------------------------------------------------------------------")
    if Choice == 'West':
        stdio.writeln("---------------------------------------------")
        stdio.writeln("This door is barricaded from the other side, ")
        stdio.writeln("looks like we can't enter this way.")
        stdio.writeln("---------------------------------------------")
    if Choice == 'South':
        stdio.writeln("--------------------")
        stdio.writeln("You Enter Right Door")
        stdio.writeln("--------------------")
        return False

#-------------------------------------------------------------------------------------------

# Description of the Office.
#
# Unique area 4

def Office():

    """
    Prints information about the location: 'Office'
    """

    stdio.writeln("-----------------------------------------------------------------------")
    stdio.writeln("You enter his office, there has to be a document here.")
    stdio.writeln("The room appears to have a bunch of waterlogged papers, even a few burn marks")
    stdio.writeln("You look around the room, hoping for a lead.")
    stdio.writeln("'This must have been where he lit the fire'")
    stdio.writeln("-----------------------------------------------------------------------")
    stdio.writeln()
    stdio.writeln("South - Where you came from")
    stdio.writeln("North - Desk")
    stdio.writeln("East - Trophy Case")
    stdio.writeln("West - Filing Cabinet")
    stdio.writeln()
    stdio.writeln("---------------")
    stdio.writeln("What do you do?")
    stdio.writeln("---------------")

#--------------------------------------------------------------------------------------------

# Decisions that can be made in the Office.

def OfficeDecisions(Choice):

    """
    Prints response to the decisions made in 'Office'
    """

    if Choice == 'North':
        stdio.writeln("-----------------------------------------------------------------------")
        stdio.writeln("You approach his desk, it seems like everything is gone. ")
        stdio.writeln("Just before giving up hope you notice a paper sticking out of a drawer.")
        stdio.writeln("To your surprise, it is a document that you need. Although torn,")
        stdio.writeln("it will do the job.")
        stdio.writeln("-----------------------------------------------------------------------")
    if Choice == 'East':
        stdio.writeln("------------------------------------")
        stdio.writeln("You examine his trophies.")
        stdio.writeln("'He must have really liked Lacross'")
        stdio.writeln("------------------------------------")
    if Choice == 'West':
        stdio.writeln("-------------------------------------------------------------------------")
        stdio.writeln("You flip over the filing cabinet only to see that the drawers are gone...")
        stdio.writeln("No files in there.")
        stdio.writeln("-------------------------------------------------------------------------")
    if Choice == 'South':
        stdio.writeln("-------------------------")
        stdio.writeln("You re-enter the hallway.")
        stdio.writeln("-------------------------")
        stdio.writeln()
        stdio.writeln("South - Door (Right Side of Hallway)")
        stdio.writeln("North - Door (Left Side of Hallway)")
        stdio.writeln("East - Where you came from")
        stdio.writeln("West - Door (End of Hallway)")
        stdio.writeln()
        stdio.writeln("---------------")
        stdio.writeln("What do you do?")
        stdio.writeln("---------------")
        return True

#--------------------------------------------------------------------------------------------

# Description of the Bathroom.
#
# Unique area 5

def Bathroom():

    """
    Prints information about the location: 'Bathroom'
    """

    stdio.writeln("-----------------------------------------------------------------------")
    stdio.writeln("You enter a bathroom.")
    stdio.writeln("You almost throw up from the immediate smell...")
    stdio.writeln("You begin to scan the room for any clues")
    stdio.writeln("-----------------------------------------------------------------------")
    stdio.writeln()
    stdio.writeln("South - Picture")
    stdio.writeln("North - Door (Where you came from)")
    stdio.writeln("East - Toilet")
    stdio.writeln("West - Bathtub")
    stdio.writeln()
    stdio.writeln("---------------")
    stdio.writeln("What do you do?")
    stdio.writeln("---------------")

#--------------------------------------------------------------------------------------------

# Decisions that can be made in the Bathroom.

def BathroomDecisions(Choice):

    """
    Prints response to the decisions made in 'Bathroom'
    """

    if Choice == 'North':
        stdio.writeln("-------------------------")
        stdio.writeln("You re-enter the hallway.")
        stdio.writeln("-------------------------")
        stdio.writeln()
        stdio.writeln("South - Door (Right Side of Hallway)")
        stdio.writeln("North - Door (Left Side of Hallway)")
        stdio.writeln("East - Where you came from")
        stdio.writeln("West - Door (End of Hallway)")
        stdio.writeln()
        stdio.writeln("---------------")
        stdio.writeln("What do you do?")
        stdio.writeln("---------------")

    if Choice == 'East':
        stdio.writeln("------------------------------------------------")
        stdio.writeln("You turn green from the sight of the toilet,")
        stdio.writeln("you don't want to know what's actually in there.")
        stdio.writeln("------------------------------------------------")
    if Choice == 'West':
        stdio.writeln("------------------------------------------------")
        stdio.writeln("The Bathtub is green and filled with rodents,")
        stdio.writeln("along with a bag that appears to contain a body.")
        stdio.writeln("------------------------------------------------")
    if Choice == 'South':
        return False
    
#------------------------------------------------------------------------------------

# Description of the Basement.
#
# Unique area 6

def Basement():

    """
    Prints information about the location: 'Basement'
    """

    stdio.writeln("-----------------------------------------------------------------------")
    stdio.writeln("You approach the picture, something seems... off about it.")
    stdio.writeln("You start to take the picture off the wall, but the floorboards begin to crack.")
    stdio.writeln("Soon, the floor gives out and you fall into the basement.")
    stdio.writeln("After a period of time you wake up to realize that you had been knocked out cold.")
    stdio.writeln("Suddenly, you scream and get to your feet as you realize that you have been laying in a pool of blood.")
    stdio.writeln("You begin to look around for possible exits.")
    stdio.writeln("-----------------------------------------------------------------------")
    stdio.writeln()
    stdio.writeln("South - Pile of unkown substance")
    stdio.writeln("North - Coffin")
    stdio.writeln("East - Tool Chest")
    stdio.writeln("West - Basement Window")
    stdio.writeln()
    stdio.writeln("---------------")
    stdio.writeln("What do you do?")
    stdio.writeln("---------------")

#------------------------------------------------------------------------------------------

# Decisions that can be made in the Basement.

def BasementDecisions(Choice):

    """
    Prints response to the decisions made in 'Basement'
    """

    if Choice == 'North':
        stdio.writeln("----------------------------------------------")
        stdio.writeln("You examine the coffin, then begin to open it.")
        stdio.writeln("There is a skeleton inside wearing a necklace.")
        stdio.writeln("You take the necklace just in case.")
        stdio.writeln("----------------------------------------------")
    if Choice == 'East':
        stdio.writeln("-----------------------------------------------------------------")
        stdio.writeln("You search the tool chest for anything useful, you find a hammer.")
        stdio.writeln("'This could come in handy'")
        stdio.writeln("-----------------------------------------------------------------")
    if Choice == 'West':
        stdio.writeln("--------------------------------------------------------------")
        stdio.writeln("You approach the window as the moonlight shines upon your face.")
        stdio.writeln("Desperate to leave, you begin smashing the window.")
        stdio.writeln("After smashing the window, you crawl out, but not without harm.")
        stdio.writeln("--------------------------------------------------------------")
    if Choice == 'South':
        stdio.writeln("----------------------------------------------------")
        stdio.writeln("You approach the pile, rethinking your life choices.")
        stdio.writeln("After reaching the pile, you begin to look through")
        stdio.writeln("the pockets of an old straight jacket.")
        stdio.writeln("You find an ID card for one of Ben's victims.")
        stdio.writeln("----------------------------------------------------")

#-----------------------------------------------------------------------------------------

# Description of Outside (last accessible area).
#
# Unique area 7

def Outside():

    """
    Prints information about the location: 'Outside'
    """
    
    stdio.writeln("-----------------------------------------------------------------------")
    stdio.writeln("You have escaped the house")
    stdio.writeln("You try to calm down your breathing.")
    stdio.writeln("Soon, you collect your thoughts and look around.")
    stdio.writeln("'Is it really over?'")
    stdio.writeln("-----------------------------------------------------------------------")
    stdio.writeln()
    stdio.writeln("South - Garden")
    stdio.writeln("North - Car")
    stdio.writeln("East - Window (Where you came from)")
    stdio.writeln("West - Woods")
    stdio.writeln()
    stdio.writeln("---------------")
    stdio.writeln("What do you do?")
    stdio.writeln("---------------")
    
#-----------------------------------------------------------------------------------------

# Decisions that can be made Outside.

def OutsideDecisions(Choice):

    """
    Prints response to the decisions made in 'Outside'
    """

    if Choice == 'North':
        stdio.writeln("----------------------------------------------------------------------------")
        stdio.writeln("You walk to your car.")
        stdio.writeln("You think about what just happened, but happily enter the vehicle to escape.")
        stdio.writeln("----------------------------------------------------------------------------")
    if Choice == 'East':
        stdio.writeln("------------------------------------------------")
        stdio.writeln("You look back at the window from which you came.")
        stdio.writeln("'I'd have to be a madman to go back in there'")
        stdio.writeln("------------------------------------------------")
    if Choice == 'West':
        stdio.writeln("---------------------------------------------------")
        stdio.writeln("You take one last look into the lifeless/dark woods")
        stdio.writeln("'Why would anybody want to live here?")
        stdio.writeln("---------------------------------------------------")
    if Choice == 'South':
        stdio.writeln("------------------------------------------------------")
        stdio.writeln("You look at the garden that ben had outback.")
        stdio.writeln("The Scarecrow in the middle resembled that of a demon.")
        stdio.writeln("'I'd better just leave'")
        stdio.writeln("------------------------------------------------------")

#-----------------------------------------------------------------------------------------

# Once the car interacted with "Outside", the EndingCredits function is called.

def EndingCredits():

    """
    Prints the ending credits of the game
    """

    stdio.writeln()
    stdio.writeln("#-------------------------------------------#")
    stdio.writeln("CONGRATULATIONS")
    stdio.writeln("#-------------------------------------------#")
    stdio.writeln()
    stdio.writeln("You escaped Ben's House and collected evidence to get him convicted in court.")
    stdio.writeln()
    stdio.writeln("-----------------")
    stdio.writeln("NOTE FROM CREATOR")
    stdio.writeln("-----------------")
    stdio.writeln("Thanks for playing, I hope you all enjoyed it!")
    stdio.writeln("----------------------------------------------")
    stdio.writeln()
    stdio.writeln()
    stdio.writeln("---------")
    stdio.writeln("GAME OVER")
    stdio.writeln("---------")
    quit()

    
#-------------------------------------------------------------------------------------


def main():

    global DocumentCounter
    gamestart()
    StartGame = PlayerInput()

    # Pressing Norths initiates "Spawning" into the first area.

    if StartGame == 'North':
        FrontDoor()

        # The While loops are the way that I chose to repeat the scenerio
        # if a player just interacts with an item, but doesn't leave the room

        while i == i:
            Choice1 = PlayerInput()
            FrontDoorDecisions(Choice1)
            if Choice1 == 'South':
                stdio.writeln("You open the door")
                break

        FirstRoom()
        while i == i:
            Choice2 = PlayerInput()
            FirstRoomDecisions(Choice2)
            if Choice2 == 'West':
                break

        # At this point, you can access 3 rooms, and choose to move between them at your
        # leizure. The key is that when you interact with "Picture" in the Bathroom
        # You can put into the basement, which starts the endgame.
        # I implimented this by having a main while loop for the Hallway, but
        # nested while loops for the side rooms. These nested loops end if the player
        # chooses to leave a room or go back, or if the picture is interacted with
        # Which initiates the endgame.

        Hallway()
        while i == i:

            Choice3 = PlayerInput()
            Decision1 = HallwayDecisions(Choice3)

            if Decision1 == True:
                Office()
                while i == i:
                    Choice4 = PlayerInput()
                    OfficeDecisions(Choice4)
                    if Choice4 == 'North':
                        DocumentCounter += 1
                    if Choice4 == 'South':                   
                        break
       

            if Decision1 == False:
                Bathroom()

                while i == i:
                    Choice5 = PlayerInput()
                    BathroomDecisions(Choice5)
                    if Choice5 == 'North':
                        break

                    # If the player chooses "South" in the bathroom 
                    # (Which is interacting with the picture)
                    # The linear endgame begins by placing you
                    # in the basement.

                    if Choice5 == 'South':
                        Basement()
                        while i == i:
                            Choice6 = PlayerInput()
                            BasementDecisions(Choice6)
                            if Choice6 == 'West':
                                Outside()

                                while i == i:
                                    Choice7 = PlayerInput()
                                    OutsideDecisions(Choice7)
                                    if Choice7 == 'North':
                                        EndingCredits()
                                    # When the player interacts with the car, this ends
                                    # the game and makes the "EndingCredits" roll.

      
#--------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
    

    
    