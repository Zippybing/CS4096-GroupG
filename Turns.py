#Turns
from random import randint

def heroTurn(game, key):
    actions = 0
    userInput = key.upper()
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
        game.world.distributeNoise(game.hero.x, game.hero.y, 5)
        actions -= 1
    elif userInput == 'A':
        # Hero Moves LEFT
        game.world.tryMoveEntity(game.hero.x,game.hero.y,game.hero.x-1,game.hero.y)
        game.world.distributeNoise(game.hero.x, game.hero.y, 5)
        actions -= 1
    elif userInput == 'S':
        # Hero Moves DOWNss
        game.world.tryMoveEntity(game.hero.x,game.hero.y,game.hero.x,game.hero.y+1)
        game.world.distributeNoise(game.hero.x, game.hero.y, 5)
        actions -= 1
    elif userInput == 'D':
        # Hero Moves RIGHT
        game.world.tryMoveEntity(game.hero.x,game.hero.y,game.hero.x+1,game.hero.y)
        game.world.distributeNoise(game.hero.x, game.hero.y, 5)
        actions -= 1
    elif userInput == 'X':
        # Bad input!
        game.hero.isAlive = False
        return -808080808
    game.world.displayGrid()
    return actions
    
    
def monsterTurn(game):
    actions = 0
    rand = randint(0,3)
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
    return actions
        