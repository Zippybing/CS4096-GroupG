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
        
    while game.hero.isAlive:
        game.world.createMap(24,24)
        game.populate()
        
        screen = Screen.open()

        while game.checkActive():
            game.world.displayGrid()
        
            #Hero Turn
            visual.showmaphero(game, screen)
            # Item Turn
            
            # Monster Turn
            visual.showmapmon(game, screen)
            # Noise Cleanup and other Cleanup
            game.world.clearNoises()
       
    screen.close(restore=True)

    if game.hero.hasEscaped:
        print("Congratulations, you died!")
    else:
        print("Damn, you suck!")
if __name__ == '__main__':
    main()
    