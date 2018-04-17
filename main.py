import GameState
import Entities
import visual
from Menus import MainMenu
import maingameloop
import random
import time
import Turns as turns
from asciimatics.screen import *
from asciimatics.scene import Scene
from asciimatics.widgets import Frame
from asciimatics.screen import Screen
import copy
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def preinit():
    
    screen = Screen.open()
    junk = Frame(screen,
                                        screen.height * 2 // 3,
                                        screen.width * 2 // 3,
                                        hover_focus=True,
                                        has_border=True,
                                        title="Game Settings",
                                        reduce_cpu=False)
    oldpalette = copy.deepcopy(junk.palette)
    Scenes = []
    debug = [True]
    game = []
    data = MainMenu(game,screen,debug,oldpalette)


""" def main(game,debug):
    None
    
    
def main():
    game = GameState.GameState()
    debug = False

    while game.hero.isAlive:
        game.floor += 1
        game.world.createMap(40,40)
        game.populate()
        game.changecolorpalette()
        screen = Screen.open()

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
            # Monster(s) Turn
            visual.showmapmon(game, screen,debug)
            # Noise Cleanup and other Cleanup
            game.world.clearNoises()
       
    screen.close(restore=True)

    if game.hero.hasEscaped:
        print("Congratulations, you died!")
    else:
        print("Damn, you suck!")
 """

if __name__ == '__main__':
    preinit()