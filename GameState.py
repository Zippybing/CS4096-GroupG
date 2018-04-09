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
        self.world = WorldGrid.WorldGrid(self) #is a worldgrid object
        self.floor = 0
        self.seed = 1   #will have a random seed that is used to generate the worlds in a deterministic way
        self.hero = Entities.Hero(0,4,'DEFAULT_HERO')
        self.monster = Entities.Monster(5,'DEFAULT_MONSTER')
    

    def checkActive(self):
        return self.hero.isAlive and not self.hero.hasEscaped
        
    def populate(self):
        self.hero.hasEscaped = False
        
        self.world.placeEntity(4,5,Entities.Exit())
        self.world.placeEntity(5,4,self.hero)
        self.world.placeEntity(4,3,self.monster)
        
        self.world.placeEntity(3,4,Entities.Key())
        self.world.placeEntity(5,5,Entities.Gem(100))
        self.world.placeEntity(7,3,Entities.Shoes())
        self.world.placeEntity(10,3,Entities.Potion())

    #Pathfinding
    """
        ???
    def dfs(self, xI, yI, visited = None):
        if visited is None:
            visited = set()
        visited.add((xI,yI))
        next = goodTiles(xI, yI)
        
    def goodTiles(self, x, y):
        ???
    """
       
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
    def changecolorpalette(self):
        None
        random.seed(self.seed+self.floor)
        val = random.randint(0,500)
        
        if(self.floor > 1):
            for row in self.world.grid:
                for piece in row:
                    if isinstance(piece.entity,Entities.Entity):
                        prep = piece.print_rep()
                        
                        prep[0] = ( prep[0][0],prep[0][1] ,(2+self.floor+val)%7)
                        if (prep[0][0] == prep[0][2]) and not isinstance(piece.entity,Entities.Wall):
                            
                            while(val == prep[0][0]):
                                val = random.randint(0,7)
                            prep[0] = ( val%7,prep[0][1] ,(2+self.floor+val)%7)
                    
                        piece.rep[0] =(piece.rep[0][0],piece.rep[0][1] ,((2+self.floor+val)%7))

                        
                    else:
                        piece.rep[0] =(piece.rep[0][0],piece.rep[0][1] ,((2+self.floor+val)%7))
                        if piece.rep[0][0] == piece.rep[0][2]:
                            piece.rep[0] = ( 4,piece.rep[0][1] ,(2+self.floor+val)%7)
                    
        