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
    colorp = []
    for row in tmp.rendered_text[0]:
        #for char in row:
        screen.paint(row,int((screen.width/2)-(tmp.max_width/2))+
        wcounter,int(screen.height/2)-8+hcounter,6,1,0)
        wcounter += 0
        hcounter += 1
        screen.refresh()
    #screen.paint(tmp.rendered_text,10,15)
    None
    time.sleep(1)




def deadscreen(game,screen):
    dtext = "You Have Been Killed"
    numscore = str(game.score)
    scoretext = "Score of the Current Run: "+str(numscore)
    
    tmp = FigletText(dtext,"doom")
    hcounter = 0
    wcounter = 0
    colorp = []
    """ for row in tmp.rendered_text[0]:
        for entry in range(0,tmp.max_width+1) """
    for row in tmp.rendered_text[0]:
        #for char in row:
        screen.print_at(row,int((screen.width/2)-(tmp.max_width/2))+
        wcounter,int(screen.height/2)-8+hcounter,1,1,0)
        wcounter += 0
        hcounter += 1
    screen.print_at(scoretext,int((screen.width/2)-(len(scoretext)/2))+
        wcounter,int(screen.height/2)-8+hcounter+1,1,1,0)
    screen.refresh()
    #screen.paint(tmp.rendered_text,10,15)
    None
    time.sleep(4)
#screen = Screen.open()

