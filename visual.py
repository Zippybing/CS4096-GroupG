


from random import randint
from asciimatics.screen import *
#from main import mastergrid
tmp = "YES\nYES\nYES"
def showmap(mastergrid):
    def demo(screen):
    
        counter = 0
        #input('Give input: ').upper()
        while(True):
            linecounter = 0
            colortracker = 0
            #for row in mastergrid: 
            #print(row)
            for row in mastergrid[0]:
                # screen.print_at(row,
                #                 0, counter,
                #                 colour=randint(0, screen.colours - 1),
                #                 bg=randint(0, screen.colours - 1))

                screen.paint(row,
                            0,linecounter,
                            7,2,0,
                            colour_map=mastergrid[1][colortracker])

                linecounter+= 1
                colortracker+=1
                ev = screen.get_key()
                if ev in (ord('Q'), ord('q')):
                    return
                screen.refresh()
        

    Screen.wrapper(demo)





