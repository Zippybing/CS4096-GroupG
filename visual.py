

import Turns
from random import randint
from time import sleep
from asciimatics.screen import *
#from main import mastergrid
tmp = "YES\nYES\nYES"

def showmaphero(game, screen):
    scoreboard = "Score: "+str(game.score) + "           " + "Lives: "+str(game.lives)
    counter = 0

    actions = game.hero.speed
    while actions > 0 and game.checkActive():
        linecounter = 0
        colortracker = 0

        user_keypress = get_keypress_from_screen(screen)

        screen.print_at(game.level,
                   int(screen.width/2) - int(len(game.level)/2), (int(screen.height/2)+linecounter-6),
                    colour=randint(0, screen.colours - 1),
                    bg=randint(0, screen.colours - 1))
        for row in game.world.vizgrid[0]:
            # screen.print_at(row,
            #                 0, counter,
            #                 colour=randint(0, screen.colours - 1),
            #                 bg=randint(0, screen.colours - 1))

            screen.paint(row,
                        int(screen.width/2)-int(game.world.width*3/2),(int(screen.height/2)+linecounter-4),
                        7,2,0,
                        colour_map=game.world.vizgrid[1][colortracker])

            linecounter+= 1
            colortracker+=1
            #ev = screen.get_key()
        
        #screen.refresh()
        screen.print_at(scoreboard,
                   int(screen.width/2) - int(len(scoreboard)/2), (int(screen.height/2)+6),
                    colour=randint(0, screen.colours - 1),
                    bg=randint(0, screen.colours - 1))
        screen.print_at('Input: ',
                    0, screen.height-1,
                    colour=randint(0, screen.colours - 1),
                    bg=randint(0, screen.colours - 1))
        screen.print_at(user_keypress, 0, 0) # prints out user keyboard input
        screen.refresh()
        
        
        actions += Turns.heroTurn(game, user_keypress)
    screen.refresh()
    

        #userInput = input('Give input: ').upper()

def showmapmon(game, screen):
    scoreboard = "Score: "+str(game.score) + "           " + "Lives: "+str(game.lives)
    counter = 0
    #input('Give input: ').upper()

    actions = game.monster.speed
    while actions > 0 and game.checkActive():
        linecounter = 0
        colortracker = 0
        #for row in mastergrid: 
        screen.print_at(game.level,
                int(screen.width/2) - int(len(game.level)/2), (int(screen.height/2)+linecounter-6),
                    colour=randint(0, screen.colours - 1),
                    bg=randint(0, screen.colours - 1))
        for row in game.world.vizgrid[0]:
            # screen.print_at(row,
            #                 0, counter,
            #                 colour=randint(0, screen.colours - 1),
            #                 bg=randint(0, screen.colours - 1))

            screen.paint(row,
                        int(screen.width/2)-int(game.world.width*3/2),(int(screen.height/2)+linecounter-4),
                        7,2,0,
                        colour_map=game.world.vizgrid[1][colortracker])

            linecounter+= 1
            colortracker+=1
            #ev = screen.get_key()
        
        #screen.refresh()
        screen.print_at(scoreboard,
                int(screen.width/2) - int(len(scoreboard)/2), (int(screen.height/2)+6),
                    colour=randint(0, screen.colours - 1),
                    bg=randint(0, screen.colours - 1))
        screen.print_at('Input: ',
                    0, screen.height-1,
                    colour=randint(0, screen.colours - 1),
                    bg=randint(0, screen.colours - 1))
        screen.refresh()
        
        actions += Turns.monsterTurn(game)

        time.sleep(.25)
    screen.refresh()

'''
    Function: get_keypress_from_screen(screen)
    Description: Checks for keyboard input from user and converts it to a string
'''
def get_keypress_from_screen(screen):
    # Built-in Asciimatics function, gets most recent keyboard/mouse input
    # Note: this may be popping the 'event' from a stack
    keypress = screen.get_event()

    # Check that input exists, and is a KeyboardEvent (not MouseEvent)
    if keypress and type(keypress) == KeyboardEvent:
        # Alphanumeric key codes are greater than zero
        if keypress.key_code > 0:
            # Convert the key code to a string using Python's chr() method
            return chr(keypress.key_code).upper()
        # Special key codes will be below zero
        else:
            # Check for specific key codes against screen's key code constants
            if keypress.key_code == screen.KEY_ESCAPE:
                return "ESC"
            # If we don't know what it is, send back nothing
            else:
                return ""
    # If input does not exist, send back nothing
    else:
        return ""
