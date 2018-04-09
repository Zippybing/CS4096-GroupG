import GameState
import Entities
import visual
import random
import time
import Turns as turns
from asciimatics.screen import *

def main():
    game = GameState.GameState()
    debug = True
    while game.hero.isAlive:
        game.floor += 1
        game.world.createMap(24,24)
        game.populate()
        game.changecolorpalette()
        None
        screen = Screen.open()

        while game.checkActive():
            if debug:
                game.world.displayGridnorm()
            else:
                game.world.displayGridH()
        
            #Hero Turn
            visual.showmaphero(game, screen,debug)
            # Item Turn
            
            # Monster Turn
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