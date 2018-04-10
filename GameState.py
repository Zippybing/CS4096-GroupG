#Author: Kyle Cusack & Michael Eschbacher
#Email: kdc6w3@mst.edu
#Assignment: Game State for Python game
#Description: The Game State for the rogue-like stealth game

import WorldGrid
import Entities
import random

class GameState:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.level = "Robbing The Three Little Bears Of Everything, Revengeance..." #random seed for genration or actual name
        self.world = WorldGrid.WorldGrid() #is a worldgrid object
        self.seed = None    #will have a random seed that is used to generate the worlds in a deterministic way
        self.hero = Entities.Hero(0,4,'DEFAULT_HERO')
        self.monster = Entities.Monster(5,'DEFAULT_MONSTER')
        self.exit = Entities.Exit()
    

    def checkActive(self):
        return self.hero.isAlive and not self.hero.hasEscaped
        
    def populate(self):
        self.hero.hasEscaped = False
        generated = []
        
        # Place Exit
        randX ,randY = self.uniqueGen(generated)
        self.world.placeEntity(randX,randY,self.exit)
        generated.append((self.exit.x,self.exit.y))

        # Place Hero
        randX ,randY = self.uniqueGen(generated)
        placeAble = self.iDFS((randX,randY),(self.exit.x,self.exit.y))
        while(not placeAble):
            randX ,randY = self.uniqueGen(generated)
            placeAble = self.iDFS((randX,randY),(self.exit.x,self.exit.y))
        self.world.placeEntity(randX,randY,self.hero)
        generated.append((self.hero.x,self.hero.y))
        
        # Place Monster
        randX ,randY = self.uniqueGen(generated)
        placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
        while(not placeAble):
            randX ,randY = self.uniqueGen(generated)
            placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
        self.world.placeEntity(randX,randY,self.monster)
        generated.append((self.monster.x,self.monster.y))
        print(generated)
        
        # Place Items

        '''
        self.world.placeEntity(3,4,Entities.Key())
        self.world.placeEntity(5,5,Entities.Gem(100))
        self.world.placeEntity(7,3,Entities.Shoes())
        self.world.placeEntity(10,3,Entities.Potion())
        '''
       
        print(self.iDFS((self.hero.x,self.hero.y),(self.monster.x,self.monster.y)))
    
    def uniqueGen(self, generated):
        randX = random.randint(1, self.world.width-2)
        randY = random.randint(1, self.world.height-2)
        while((randX,randY) in generated):
            randX = random.randint(1, self.world.width-2)
            randY = random.randint(1, self.world.height-2)
        return randX, randY
       
    def levelnamegen(self):
        self.level = None   #a dict of level names or randomly generated ones

    def setworld(self,world):
        self.world = world

    def seedgen(self, input):
        self.seed = input   # plus what ever random seed generator with input as a key
    
    def newworldgen(self,seed):
        self.seed = seed + None #None is a deterministic addition to seed to create next level from prevoius
    def scoreDisplay(self):
        tmp = []
        livesrep = "LIVES: "+str(self.lives)
        scorerep = "SCORE: "+str(self.score)
        totalrep = '\n'+livesrep + "    " + scorerep
        tmp += [('streak',totalrep)]
        return tmp
    def worldDisplay(self):
        tmp =[]
        Worldrep = str(self.level)
        tmp += [('streak', Worldrep)]
        return tmp
    
    #DFS
    def iDFS(self, vertex, goal):
        if vertex == goal:
            return False
        discovered = []
        stack = []
        stack.append(vertex)
        while(stack):
            vertex = stack.pop()
            if vertex == goal:
                return True
            if vertex not in discovered:
                discovered.append(vertex)
                for adjacent in self.validPoints(vertex[0], vertex[1]):
                    stack.append(adjacent)
        return False
                
    def validPoints(self, pX, pY):
        checkList = [(pX+1,pY),(pX-1,pY),(pX,pY+1),(pX,pY-1)]
        returnList = []
        for p in checkList:
            if type(self.world.grid[p[0]][p[1]].entity) != Entities.Wall:
                returnList.append(p)
        return returnList
            
    
    
    '''
    # BFS - Connecting Two Points, the Hard Way
    def dfs_wrapper(self, start_x, start_y, goal_x, goal_y):
        world = self.world.grid
        dfs_grid = [ [False for _ in range(y)] for _ in range(x)]
        
        if dfs(dfs_grid, goal_x, goal_y):
            return True
        else:
            return False
        
    def dfs(self, dfs_grid, grid_x, grid_y):
        # Check the neighboring grid tiles
        # If the neighboring grid is within range, and not a Wall, search it too
        dfs_grid[grid_x][grid_y] = True # Space has been visited
        if grid_x - 1 >= len(dfs_grid) and grid_y - 1 >= len(dfs
    '''    
        