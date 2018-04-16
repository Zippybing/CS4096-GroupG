

import Turns
from random import randint
from time import sleep
from asciimatics.screen import *
#from main import mastergrid
tmp = "YES\nYES\nYES"

def showmaphero(game, screen,debug):
    
    counter = 0

    actions = game.hero.actionCap
    while actions > 0 and game.checkActive():
        scoreboard = "Score: "+str(game.score)+ "              "  + "Floor: "+str(game.floor) +"              "+"Actions Remaining: "+str(actions)
        linecounter = 0
        colortracker = 0

        

        # Title bar
        screen.print_at(game.level,
                   int(screen.width/2) - int(len(game.level)/2), 1,
                    colour=7,
                    bg=0)
        # Map grid
        for row in game.world.vizgrid[0]:
            # screen.print_at(row,
            #                 0, counter,
            #                 colour=randint(0, screen.colours - 1),
            #                 bg=randint(0, screen.colours - 1))

            screen.paint(row,
                        int(screen.width/2)-int(game.world.width*3/2),(int(screen.height/4)+linecounter-4),
                        7,2,0,
                        colour_map=game.world.vizgrid[1][colortracker])

            linecounter+= 1
            colortracker+=1
            #ev = screen.get_key()
        
        # Scoreboard
        screen.print_at(scoreboard,
                   int(screen.width/2) - int(len(scoreboard)/2), (int(screen.height)-1),
                    colour=7,
                    bg=0)
        # User keypress display -- DEBUGGING PURPOSES ONLY
        screen.refresh()
        while True:
            keyboardinput = get_keypress_from_screen(screen)
            if keyboardinput != "":
                screen.print_at(keyboardinput, 0, 0) # prints out user keyboard input
                break
            time.sleep(0.25)

        screen.refresh()
        
        
        actions += Turns.heroTurn(game, keyboardinput,debug)
    screen.refresh()
    

        #userInput = input('Give input: ').upper()

def showmapmon(game, screen,debug):
    counter = 0
    #input('Give input: ').upper()

    for i in range(len(game.monsters)):
        monster = game.monsters[i]
        actions = monster.actionCap
        while actions > 0 and game.checkActive():
            scoreboard = "Score: "+str(game.score)+ "              "  + "Floor: "+str(game.floor) +"              "+"Actions Remaining: "+str(actions)
            linecounter = 0
            colortracker = 0
            #for row in mastergrid:
            # Title bar
            screen.print_at(game.level,
                    int(screen.width/2) - int(len(game.level)/2), 1,
                        colour=7,
                        bg=0)
            # Map grid
            for row in game.world.vizgrid[0]:
                # screen.print_at(row,
                #                 0, counter,
                #                 colour=randint(0, screen.colours - 1),
                #                 bg=randint(0, screen.colours - 1))

                screen.paint(row,
                            int(screen.width/2)-int(game.world.width*3/2),(int(screen.height/4)+linecounter-4),
                            7,2,0,
                            colour_map=game.world.vizgrid[1][colortracker])

                linecounter+= 1
                colortracker+=1
                #ev = screen.get_key()
            
            # Scoreboard
            screen.print_at(scoreboard,
                    int(screen.width/2) - int(len(scoreboard)/2), (int(screen.height)-1),
                        colour=7,
                        bg=0)
            screen.refresh()
            
            actions += Turns.monsterTurn(game,monster,debug)

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
