
import GameState
import Entities
import visual
import random
import time
import Turns as turns
from asciimatics.screen import *
from asciimatics.scene import Scene




def main(game,debug,menudata):
    None
    
    

    while game.hero.isAlive:
        game.floor += 1
        game.world.createMap(24,24)
        game.populate()
        game.changecolorpalette()
        screen = Screen.open()
        visual.blackout(screen)
        while game.checkActive():
            if debug[0]:
                game.world.displayGridnorm()
            else:
                game.world.displayGridH()
            #Hero Turn
            visual.showmaphero(game, screen,debug)
            # Item Turn
            for item in game.hero.inventory:
                if item.applied == False:
                    if item.icon == 'P':
                        game.hero.actionCap += item.actionMod
                    elif item.icon == 'T':
                        game.hero.visual += item.visMod
                    elif item.icon == 'G':
                        game.score += item.scoreMod
                    elif item.icon == 'S':
                        game.hero.noise += item.noiseMod
                    item.applied = True
            # Monster Turn
            visual.showmapmon(game, screen,debug)
            # Noise Cleanup and other Cleanup
            game.world.clearNoises()
       
    screen.close(restore=True)

    if game.hero.hasEscaped:
        print("Congratulations, you died!")
    else:
        print("Damn, you suck!")
