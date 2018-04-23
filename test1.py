from asciimatics.effects import Cycle, Stars, Julia
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
import time
def intro(screen):
    text = "The Revengnce of the Bears"
    tmp = FigletText(text,"doom")
    hcounter = 0
    wcounter = 0
    for row in tmp.rendered_text[0]:
        #for char in row:
        screen.paint(row,int((screen.width/2)-(tmp.max_width/2))+
        wcounter,int(screen.height/2)-8+hcounter)
        wcounter += 0
        hcounter += 1
        screen.refresh()
    #screen.paint(tmp.rendered_text,10,15)
    None
    time.sleep(1)





#screen = Screen.open()

