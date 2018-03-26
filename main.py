import GameState
import Entities
import visual
import random
import time
import Turns as turns
from asciimatics.screen import *

'''
import winsound
frequency = 1500
frequency2 = 2000
duration = 250
'''

def main():
    game = GameState.GameState()
    
    game.world.createMap(20,8)
    game.hero = Entities.Hero(0,4,88,'Steve')
    game.monster = Entities.Monster(5,88,'Fred')
    game.world.placeEntity(1,2,game.hero)
    game.world.placeEntity(4,3,game.monster)
    game.world.placeEntity(3,4,Entities.Key())
    game.world.placeEntity(5,5,Entities.Gem(100))
    game.world.placeEntity(7,3,Entities.Shoes())
    game.world.placeEntity(10,3,Entities.Potion())
    game.world.placeEntity(12,5,Entities.Exit())

    
    screen = Screen.open()
    '''
    winsound.Beep(frequency, duration)
    '''
    while game.checkActive():
        game.world.displayGrid()
    
        #Hero Turn
        visual.showmaphero(game, screen)
        # Item Turn
        
        # Monster Turn
        visual.showmapmon(game, screen)
        # Noise Cleanup and other Cleanup
        game.world.clearNoises()
   
    #Cool Jingle for Windows users
    '''
    winsound.Beep(frequency, duration)
    winsound.Beep(frequency2, duration)
    winsound.Beep(frequency, duration)
    winsound.Beep(frequency2, duration)
    winsound.Beep(frequency2, duration)
    '''
    
    screen.close(restore=True)

    #i = 1/0
    
    if game.hero.hasEscaped:
        print("Congratulations, you won!")
    else:
        print("Damn, you suck!")
if __name__ == '__main__':
    main()