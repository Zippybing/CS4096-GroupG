


from random import randint
from asciimatics.screen import *
#from main import mastergrid
tmp = "YES\nYES\nYES"
def showmap(mastergrid, game):
    def demo():
        screen = Screen.open()
        scoreboard = "Score: "+str(game.score) + "           " + "Lives: "+str(game.lives)
        counter = 0
        #input('Give input: ').upper()
        while(True):
            linecounter = 0
            colortracker = 0
            #for row in mastergrid: 
            #print(row)
            screen.print_at(game.level,
                       int(screen.width/2) - int(len(game.level)/2), (int(screen.height/2)+linecounter-6),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
            for row in mastergrid[0]:
                # screen.print_at(row,
                #                 0, counter,
                #                 colour=randint(0, screen.colours - 1),
                #                 bg=randint(0, screen.colours - 1))

                screen.paint(row,
                            int(screen.width/2)-11,(int(screen.height/2)+linecounter-4),
                            7,2,0,
                            colour_map=mastergrid[1][colortracker])

                linecounter+= 1
                colortracker+=1
                #ev = screen.get_key()
            
            #screen.refresh()
            screen.print_at(scoreboard,
                       int(screen.width/2) - int(len(scoreboard)/2), (int(screen.height/2)+6),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
            screen.print_at('Input: ',
                        0, screen.height-1,
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
            screen.refresh()
            userInput = input().upper()
            return userInput
            #userInput = input('Give input: ').upper()
        screen.close(restore=False)


            
            #return
    userInput = demo()
    return userInput

    



