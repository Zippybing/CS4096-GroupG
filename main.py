import GameState
import Entities
import visual
import random
import time

def main():
    game = GameState.GameState()
    game.world.createMap(20,8)
    game.hero = Entities.Hero('H',0,1,2,4,88,'Steve')
    game.monster = Entities.Monster('M',0,4,3,5,88,'Fred')
    game.world.placeEntity(1,2,game.hero)
    game.world.placeEntity(4,3,game.monster)
    game.world.placeEntity(3,4,Entities.Key('K',0,3,4))
    game.world.placeEntity(10,3,Entities.Potion('P',0,10,3))
    game.world.placeEntity(12,5,Entities.Exit('E',0,12,5))

    
    while game.checkActive():
        game.world.displayGrid()
    
        # Hero Turn
        actions = game.hero.speed
        while actions > 0 and game.checkActive():
            userInput = visual.showmap(game)
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
                game.world.tryMoveEntity(game.hero.x,game.hero.y,game.hero.x,game.hero.y-1)
                actions -= 1
            elif userInput == 'A':
                # Hero Moves LEFT
                game.world.tryMoveEntity(game.hero.x,game.hero.y,game.hero.x-1,game.hero.y)
                actions -= 1
            elif userInput == 'S':
                # Hero Moves DOWN
                game.world.tryMoveEntity(game.hero.x,game.hero.y,game.hero.x,game.hero.y+1)
                actions -= 1
            elif userInput == 'D':
                # Hero Moves RIGHT
                game.world.tryMoveEntity(game.hero.x,game.hero.y,game.hero.x+1,game.hero.y)
                actions -= 1
            elif userInput == 'X':
                # Bad input!
                return
            game.world.displayGrid()
            print(game.hero.inventory)
        # Item Turn
        
        # Monster Turn
        actions = game.monster.speed
        while actions > 0 and game.checkActive():
            rand = random.randint(0,3)
            if rand == 0:
                # Hero Moves UP
                game.world.tryMoveEntity(game.monster.x,game.monster.y,game.monster.x,game.monster.y-1)
                actions -= 1
            elif rand == 1:
                # Hero Moves LEFT
                game.world.tryMoveEntity(game.monster.x,game.monster.y,game.monster.x-1,game.monster.y)
                actions -= 1
            elif rand == 2:
                # Hero Moves DOWN
                game.world.tryMoveEntity(game.monster.x,game.monster.y,game.monster.x,game.monster.y+1)
                actions -= 1
            elif rand == 3:
                # Hero Moves RIGHT
                game.world.tryMoveEntity(game.monster.x,game.monster.y,game.monster.x+1,game.monster.y)
                actions -= 1
            game.world.displayGrid()
            time.sleep(.25)
        # Noise Cleanup and other Cleanup
        
    if game.hero.hasEscaped:
        print("Congratulations, you won!")
    else:
        print("Damn, you suck!")
    
if __name__ == '__main__':
    main()