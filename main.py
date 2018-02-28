import GameState
import Entities
import random
from asciimatics.screen import *
import visual
mastergrid = ''
def main():
    game = GameState.GameState()
    game.world.createMap(8,8)
    game.world.placeEntity(1,2,Entities.Hero('H',0,1,5,'Dickbutt'))
    game.world.placeEntity(4,3,Entities.Monster('M',0,1,5,'Fred'))
    game.world.placeEntity(3,4,Entities.Key("K",0))
    heroCoord = [1,2]
    monsterCoord = [4,3]
   
    while True:
        # Hero Turn
        mastergrid = game.world.displayGrid()
        #print(mastergrid[1])
        #for i in range(0, 1500):
            #print(i,"  ",chr(i))
        
        userInput = visual.showmap(mastergrid, game)
        if userInput == '0':
            # Hero Faces UP
            x = 0
        elif userInput == '1':
            # Hero Faces RIGHT
            x = 0
        elif userInput == '2':
            # Hero Faces DOWN
            x = 0
        elif userInput == '3':
            # Hero Faces Right
            x = 0
        elif userInput == 'W':
            # Hero Moves UP
            game.world.moveEntity(heroCoord[0],heroCoord[1],heroCoord[0],heroCoord[1]-1)
            heroCoord[1] -= 1
        elif userInput == 'A':
            # Hero Moves LEFT
            game.world.moveEntity(heroCoord[0],heroCoord[1],heroCoord[0]-1,heroCoord[1])
            heroCoord[0] -= 1
        elif userInput == 'S':
            # Hero Moves DOWN
            game.world.moveEntity(heroCoord[0],heroCoord[1],heroCoord[0],heroCoord[1]+1)
            heroCoord[1] += 1
        elif userInput == 'D':
            # Hero Moves RIGHT
            game.world.moveEntity(heroCoord[0],heroCoord[1],heroCoord[0]+1,heroCoord[1])
            heroCoord[0] += 1
        else:
            # Bad input!
            break
        # Item Turn
        
        # Monster Turn
        
        xRand = random.randint(-1,1)
        yRand = random.randint(-1,1)
        game.world.moveEntity(monsterCoord[0],monsterCoord[1],monsterCoord[0]+xRand,monsterCoord[1]+yRand)
        monsterCoord[0] += xRand
        monsterCoord[1] += yRand

        # Noise Cleanup and other Cleanup
        
       
    
if __name__ == '__main__':
    main()