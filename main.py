import GameState
import Entities
import visual
import random
import time
import Turns as turns
from asciimatics.screen import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    game = GameState.GameState()
    debug = True

    while game.hero.isAlive:
        game.floor += 1
        game.world.createMap(14,14)
        game.populate()
        game.changecolorpalette()
        screen = Screen.open()

        while game.checkActive():
            if debug:
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
            # Monster(s) Turn
            visual.showmapmon(game, screen,debug)
            # Noise Cleanup and other Cleanup
            game.world.clearNoises()
       
    screen.close(restore=True)

    if game.hero.hasEscaped:
        print("Congratulations, you died!")
    else:
        print("Damn, you suck!")
if __name__ == '__main__':
    main()