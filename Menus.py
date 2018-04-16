


import asciimatics
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, CheckBox
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
#from main import preinit
from maingameloop import main
import visual
import GameState
import sys
import random

def MainMenu(game,screen,debug):
    def endmenu():
        debug[0] = False
        game = GameState.GameState()
        Mmenu.save()
        looksy = Mmenu.data
        game.seed = int(str(looksy['seedval']))
        random.seed(game.seed)
        game.name = str(looksy['nameval'])
        debug[0] = looksy['Debug']
        #visual.blackout(screen)
        main(game,debug,looksy,screen)
        DeathMenu(game,screen,debug)
        return Mmenu.data
    

    endval = True
    Mmenu = Frame(screen,
                                        screen.height * 2 // 3,
                                        screen.width * 2 // 3,
                                        hover_focus=True,
                                        has_border=True,
                                        title="Game Settings",
                                        reduce_cpu=False)

    mapping = Layout([100], fill_frame=True)

    Mmenu.add_layout(mapping)

    mapping.add_widget(Text("Seed:","seedval"))
    mapping.add_widget(Text("Adventurer Name:","nameval"))
    mapping.add_widget(CheckBox("Debug Mode:","Debug","Debug"))

    bottomrow = Layout([1, 1, 1, 1])
    Mmenu.add_layout(bottomrow)
    bottomrow.add_widget(Button("Start Level",endmenu),3)
    Mmenu.fix()

    #return Mmenu
    #Mmenu._on_pic

    Scenes = [
        Scene([Mmenu],-1)
    ]

    screen.play(Scenes)
    return Mmenu.data


def DeathMenu(game,screen,debug):
    None
    def endgame():
        screen.close()
        sys.exit(0)
        None
    def Restart():
        MainMenu(game,screen,debug)
        None
    Dmenu = Frame(screen,
                                        screen.height * 2 // 3,
                                        screen.width * 2 // 3,
                                        hover_focus=True,
                                        has_border=True,
                                        title="YOU HAVE DIED",
                                        reduce_cpu=False)

    mapping = Layout([100], fill_frame=True)

    Dmenu.add_layout(mapping)
    bottomrow = Layout([1, 1, 1, 1])
    Dmenu.add_layout(bottomrow)
    bottomrow.add_widget(Button("Exit",endgame),1)
    bottomrow.add_widget(Button("Restart",Restart),3)
    Dmenu.fix()

    #return Mmenu
    #Mmenu._on_pic

    Scenes = [
        Scene([Dmenu],-1)
    ]

    screen.play(Scenes)
    return Dmenu.data








    

    
