import GameState
import Entities
import visual
import random
import time
import Turns as turns
from asciimatics.screen import *

def main():
    game = GameState.GameState()
    debug = False
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
            for item in actor.inventory:
                if item.applied == False:
                    if item.icon == 'P':
                        pass
                    elif item.icon == 'T':
                        pass
                    elif item.icon == 'G':
                        pass
                    elif item.icon == 'S':
                        pass
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
if __name__ == '__main__':
    main()