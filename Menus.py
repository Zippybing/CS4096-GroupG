


import asciimatics
from asciimatics.widgets import Frame, ListBox, Layout, Divider, Text, \
    Button, TextBox, Widget, CheckBox
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication
import maingameloop
import visual

def MainMenu(game,screen,debug):
    def endmenu():
        debug[0] = False
        Mmenu.save()
        looksy = Mmenu.data
        game.seed = int(str(looksy['seedval']))
        debug[0] = looksy['Debug']
        #visual.blackout(screen)
        maingameloop.main(game,debug,looksy)
        
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










    

    
