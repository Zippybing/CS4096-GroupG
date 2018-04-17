#Turns
from Config import getValue
from random import randint, choice

def heroTurn(game, key,debug):
    actions = 0

    # Receive either a string representation of user keypress, or empty string
    userInput = key

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
        game.world.distributeNoise(game.hero.x, game.hero.y, game.hero.noise)
        actions -= 1
    elif userInput == 'A':
        # Hero Moves LEFT
        game.world.tryMoveEntity(game.hero.x,game.hero.y,game.hero.x-1,game.hero.y)
        game.world.distributeNoise(game.hero.x, game.hero.y, game.hero.noise)
        actions -= 1
    elif userInput == 'S':
        # Hero Moves DOWNss
        game.world.tryMoveEntity(game.hero.x,game.hero.y,game.hero.x,game.hero.y+1)
        game.world.distributeNoise(game.hero.x, game.hero.y, game.hero.noise)
        actions -= 1
    elif userInput == 'D':
        # Hero Moves RIGHT
        game.world.tryMoveEntity(game.hero.x,game.hero.y,game.hero.x+1,game.hero.y)
        game.world.distributeNoise(game.hero.x, game.hero.y, game.hero.noise)
        actions -= 1
    elif userInput == 'X':
        # Bad input!
        game.hero.isAlive = False
        return -808080808
    if debug:
        game.world.displayGridnorm()
    else:
        game.world.displayGridH()
    
    return actions
    
    
def monsterTurn(game,monster,debug):
    actions = 0
    direction = randint(0,3)
    maxNoise = -1
    #TOP-LEFT
    if game.world.grid[monster.x-1][monster.y-1].noise > maxNoise:
        maxNoise = game.world.grid[monster.x-1][monster.y-1].noise
        direction = choice([0,1])
    #TOP-RIGHT
    if game.world.grid[monster.x+1][monster.y-1].noise > maxNoise:
        maxNoise = game.world.grid[monster.x+1][monster.y-1].noise
        direction = choice([0,3])
    #BOT-RIGHTS
    if game.world.grid[monster.x+1][monster.y+1].noise > maxNoise:
        maxNoise = game.world.grid[monster.x+1][monster.y+1].noise
        direction = choice([2,3])
    #BOT-LEFT
    if game.world.grid[monster.x-1][monster.y+1].noise > maxNoise:
        maxNoise = game.world.grid[monster.x-1][monster.y+1].noise
        direction = choice([1,2])
    #UP
    if game.world.grid[monster.x][monster.y-1].noise > maxNoise:
        maxNoise = game.world.grid[monster.x][monster.y-1].noise
        direction = 0
    #RIGHT
    if game.world.grid[monster.x+1][monster.y].noise > maxNoise:
        maxNoise = game.world.grid[monster.x+1][monster.y].noise
        direction = 3
    #DOWN
    if game.world.grid[monster.x][monster.y+1].noise > maxNoise:
        maxNoise = game.world.grid[monster.x][monster.y+1].noise
        direction = 2
    #LEFT
    if game.world.grid[monster.x-1][monster.y].noise > maxNoise:
        maxNoise = game.world.grid[monster.x-1][monster.y].noise
        direction = 1
    
    if maxNoise <= 0:
        direction = randint(0,3)
        
    if direction == 0:
        # Hero Moves UP
        game.world.tryMoveEntity(monster.x,monster.y,monster.x,monster.y-1)
        actions -= 1
    elif direction == 1:
        # Hero Moves LEFT
        game.world.tryMoveEntity(monster.x,monster.y,monster.x-1,monster.y)
        actions -= 1
    elif direction == 2:
        # Hero Moves DOWN
        game.world.tryMoveEntity(monster.x,monster.y,monster.x,monster.y+1)
        actions -= 1
    elif direction == 3:
        # Hero Moves RIGHT
        game.world.tryMoveEntity(monster.x,monster.y,monster.x+1,monster.y)
        actions -= 1
    if debug:
        game.world.displayGridM()
    else:
        pass
        #game.world.displayGridM()
    return actions
        