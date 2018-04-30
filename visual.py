

import Turns
from random import randint
from time import sleep
import Config
import Entities
from collections import Counter
from Config import getValue
from asciimatics.screen import *
#from main import mastergrid
tmp = "YES\nYES\nYES"

def showmaphero(game, screen, debug):
    
    counter = 0

    actions = game.hero.actionCap
    while actions > 0 and game.checkActive():
        scoreboard = ("Score: "+str(game.score)+ "              "  + "Floor: "+str(game.floor) +"              "+"Actions Remaining: "+str(actions)
                        +"       "+"Seed: "+str(game.seed))
        linecounter = 0
        colortracker = 0

        

        # Title bar
        screen.print_at(str(game.name+" is "+game.level),
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
                        int(screen.width/2)-int(game.world.width*3/2)-3,(int(screen.height/4)+linecounter-4),
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
        # Item Display
        hcounter = 0
        itemdict = Counter(game.hero.namedinv)
        screen.print_at("Inventory",int(screen.width-13),int(2+hcounter),7,4,0)
        hcounter += 1
        for item in itemdict.items():
            if item[1] == 1:
                screen.print_at(item[0],int(screen.width-13),int(2+hcounter),7,4,0)
            else:
                screen.print_at(item[0] + "X" + str(item[1]),int(screen.width-13),int(2+hcounter),7,4,0)
            hcounter += 2
        # User keypress display -- DEBUGGING PURPOSES ONLY
        screen.refresh()
        
        dumpTxt_Hero(game,actions)
        
        dump_keypresses(screen)
        while True:
            keyboardinput = get_keypress_from_screen(screen)
            if keyboardinput != "":
                screen.print_at(keyboardinput, 0, 0) # prints out user keyboard input
                break

        screen.refresh()
        
        actions += Turns.heroTurn(game, keyboardinput, debug)
    screen.refresh()
    

        #userInput = input('Give input: ').upper()

def showmapmon(game, screen, debug):
    monsterControl = Config.getValue('visual', 'monsterControl', 'bool')    
    
    if debug[0]:
        if monsterControl:
            game.world.displayGridnorm()
        else:
            game.world.displayGridM()
    else:
        if monsterControl:
            game.world.displayGridM()
        else:
            game.world.displayGridH()
    
    counter = 0
    #input('Give input: ').upper()

    for monster in game.monsters:
        actions = monster.actionCap
        while actions > 0 and game.checkActive() and monster.isAlive:
            scoreboard = ("Score: "+str(game.score)+ "              "  + "Floor: "+str(game.floor) +"              "+"Actions Remaining: "+str(actions)
                        +"       "+"Seed: "+str(game.seed))
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
            
            dumpTxt_Monster(game,actions)
            
            
            if monsterControl:
                dump_keypresses(screen)
                while True:
                    keyboardinput = get_keypress_from_screen(screen)
                    if keyboardinput != "":
                        screen.print_at(keyboardinput, 0, 0) # prints out user keyboard input
                        break
                actions += Turns.monsterTurnHuman(game,monster,debug,keyboardinput)
            else:
                actions += Turns.monsterTurnAI(game,monster,debug)
                time.sleep(.1)
            
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


def blackout(screen):
    counter = 0
    for row in range(screen.width):
        for col in range(screen.height):
            counter += 1
            screen.print_at('                  ',
                row,col,
                    colour=0,
                    bg=0)
'''
    Function: dump_keypresses(screen)
    Description: Removes all keypresses entered prior to Hero's turn
'''
def dump_keypresses(screen):
    # Get the initial keypress
    keypress = screen.get_event()
    # Continue getting/popping keypresses from queue until no more remain
    # i.e. get_event() returns a 'None' instead of a 'KeyBoardEvent'
    while keypress != None:
        keypress = screen.get_event()
    return
    
def dumpTxt_Hero(game, actions):
    filename = Config.getValue('visual', 'heroDumpFile', 'string')
    with open(filename, 'w') as heroDump:
        heroDump.write('Score: ' + str(game.score) + '\n')
        heroDump.write('Floor: ' + str(game.floor) + '\n')
        heroDump.write('Actions: ' + str(actions) + '\n')
        
        for y in range(len(game.world.grid[0])):
            rowtext = ""
            for x in range(len(game.world.grid)):
                rowtext += ' '+game.world.grid[x][y].print_icon()+' '
            heroDump.write(rowtext + '\n')
        
        heroDump.write('\n')
        
def dumpTxt_Monster(game, actions):
    filename = Config.getValue('visual', 'monsterDumpFile', 'string')
    with open(filename, 'w') as heroDump:
        heroDump.write('Score: ' + str(game.score) + '\n')
        heroDump.write('Floor: ' + str(game.floor) + '\n')
        heroDump.write('Actions: ' + str(actions) + '\n')
        
        for y in range(len(game.world.grid[0])):
            rowtext = ""
            for x in range(len(game.world.grid)):
                if type(game.world.grid[x][y].entity) == Entities.Monster:
                    rowtext += ' '+str(game.world.grid[x][y].print_icon())+' '
                elif type(game.world.grid[x][y].entity) == Entities.Wall:
                    rowtext += ' '+str(game.world.grid[x][y].print_icon())+' '
                else:
                    rowtext += ' '+str(game.world.grid[x][y].noise)+' '
            heroDump.write(rowtext + '\n')
        
        heroDump.write('\n')
