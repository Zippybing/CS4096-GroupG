


import asciimatics
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, CheckBox,Label
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
import copy
import test1

def MainMenu(game,screen,debug,oldpalette):
    def endgame():
        screen.close()
        quit()
        sys.exit(0)
        None
    def endmenu():
        debug[0] = False
        game = GameState.GameState()
        Mmenu.save()
        looksy = Mmenu.data
        if looksy['seedval'] != "":
            converted = 0
            if str.isnumeric(looksy['seedval']):
                game.seed = int(looksy['seedval'])
            else:
                for char in looksy['seedval']:
                    converted += ord(char)
                game.seed = int(converted)
        random.seed(game.seed)
        if looksy['nameval'] != "":
            if len(looksy["nameval"]) >= 20:
                game.name = str(looksy['nameval'])[:21]
            else:
                game.name = str(looksy['nameval'])
        debug[0] = looksy['Debug']
        #visual.blackout(screen)
        main(game,debug,looksy,screen)
        test1.deadscreen(game,screen)
        DeathMenu(game,screen,debug,oldpalette)
        return Mmenu.data
    

    endval = True
    Mmenu = Frame(screen,
                                        screen.height * 2 // 3,
                                        screen.width * 2 // 3,
                                        hover_focus=True,
                                        has_border=True,
                                        title="Game Settings",
                                        reduce_cpu=False)

    #Mmenu.palette['background'] = (0,0,1)
    Mmenu.palette = oldpalette
    mapping = Layout([100], fill_frame=True)
    Mmenu.add_layout(mapping)
    mapping.add_widget(Text("Seed:","seedval"))
    mapping.add_widget(Text("Adventurer Name:","nameval"))
    mapping.add_widget(CheckBox("Debug Mode:","Debug","Debug"))

    bottomrow = Layout([1, 1, 1, 1])
    Mmenu.add_layout(bottomrow)
    bottomrow.add_widget(Button("Exit Game",endgame),0)
    bottomrow.add_widget(Button("Start Level",endmenu),3)
    Mmenu.fix()
    
    #Mmenu._on_pic

    Scenes = [
        Scene([Mmenu],-1)
    ]

    screen.play(Scenes)
    return Mmenu.data


def DeathMenu(game,screen,debug,oldpalette):
    None
    def endgame():
        screen.close()
        quit()
        sys.exit(0)
        None
    def Restart():
        MainMenu(game,screen,debug,oldpalette)
        None
    Dmenu = Frame(screen,
                                        screen.height * 2 // 3,
                                        screen.width * 2 // 3,
                                        hover_focus=True,
                                        has_border=True,
                                        title="YOU HAVE DIED",
                                        reduce_cpu=False)

    mapping = Layout([100], fill_frame=True)
    
    for entry in Dmenu.palette:
        if entry != "focus_button":
            Dmenu.palette[entry] = (1,1,1)
        else:
            Dmenu.palette[entry] = (0,1,5)
    Dmenu.add_layout(mapping)
    mapping.add_widget(Label(str("Your Final Score Is:  "+str(game.score)),1))
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


def IntroScreen(screen):
    text = "The Revengnce of the Bears"
    tmp = FigletText(text,"doom")
    hcounter = 0
    wcounter = 0
    for row in tmp.rendered_text[0]:
        #for char in row:
        screen.paint(row,int((screen.width/2)-(tmp.max_width/2))+
        wcounter,int(screen.height/2)-8+hcounter,)
        wcounter += 0
        hcounter += 1
    None






    

    
