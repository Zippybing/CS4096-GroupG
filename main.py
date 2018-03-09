import GameState
import Entities
import visual
import random
import time
import Turns as turns
from asciimatics.screen import *

def main():
    game = GameState.GameState()
    game.world.createMap(20,8)
    game.hero = Entities.Hero('H',0,1,2,4,88,'Steve')
    game.monster = Entities.Monster('M',4,3,5,88,'Fred')
    game.world.placeEntity(1,2,game.hero)
    game.world.placeEntity(4,3,game.monster)
    game.world.placeEntity(3,4,Entities.Key('K',3,4))
    game.world.placeEntity(5,5,Entities.Gem('G',5,5,100))
    game.world.placeEntity(7,3,Entities.Shoes('S',7,3))
    game.world.placeEntity(10,3,Entities.Potion('P',10,3))
    game.world.placeEntity(12,5,Entities.Exit('E',12,5))

    
    screen = Screen.open()
    
    while game.checkActive():
        game.world.displayGrid()
    
        #Hero Turn
        visual.showmaphero(game, screen)
        # Item Turn
        
        # Monster Turn
        visual.showmapmon(game, screen)
        # Noise Cleanup and other Cleanup

    screen.close(restore=False) 
    
    if game.hero.hasEscaped:
        print("Congratulations, you won!")
    else:
        print("Damn, you suck!")
if __name__ == '__main__':
    main()
