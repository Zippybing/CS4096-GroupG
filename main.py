import GameState
import Entities
import random

def main():
    game = GameState.GameState()
    game.world.createMap(20,8)
    game.hero = Entities.Hero('H',0,1,2,1,5,'Steve')
    game.monster = Entities.Monster('M',0,4,3,1,5,'Fred')
    game.world.placeEntity(1,2,game.hero)
    game.world.placeEntity(4,3,game.monster)
    game.world.placeEntity(3,4,Entities.Key('K',0,3,4))
    game.world.placeEntity(5,5,Entities.Gem('G',0,5,5,100))
    monsterCoord = [4,3]
    while True:
        game.world.displayGrid()
    
        # Hero Turn
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
            game.world.moveEntity(game.hero.x,game.hero.y,game.hero.x,game.hero.y-1)
        elif userInput == 'A':
            # Hero Moves LEFT
            game.world.moveEntity(game.hero.x,game.hero.y,game.hero.x-1,game.hero.y)
        elif userInput == 'S':
            # Hero Moves DOWN
            game.world.moveEntity(game.hero.x,game.hero.y,game.hero.x,game.hero.y+1)
        elif userInput == 'D':
            # Hero Moves RIGHT
            game.world.moveEntity(game.hero.x,game.hero.y,game.hero.x+1,game.hero.y)
        else:
            # Bad input!
            break
        # Item Turn
        
        # Monster Turn
        
        xRand = random.randint(-1,1)
        yRand = random.randint(-1,1)
        game.world.moveEntity(game.monster.x,game.monster.y,game.monster.x+xRand,game.monster.y+yRand)

        # Noise Cleanup and other Cleanup
        
       
    
if __name__ == '__main__':
    main()