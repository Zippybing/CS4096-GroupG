import GameState
import Entities

def main():
    game = GameState.GameState()
    game.world.createMap(12,8)
    game.world.placeEntity(1,2,Entities.Hero('H',0,1,5,'Dickbutt'))
    heroCoord = [1,2]
    while True:
        # Hero Turn
        game.world.displayGrid()
        userInput = input('Give input: ').upper()
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
        # Noise Cleanup and other Cleanup
        
       
    
if __name__ == '__main__':
    main()