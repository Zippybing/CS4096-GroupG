#Author: Kyle Cusack & Michael Eschbacher
#Email: kdc6w3@mst.edu
#Assignment: Game State for Python game
#Description: The Game State for the rogue-like stealth game

import WorldGrid

class GameState:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.level = "Robbing The Three Little Bears Of Everything, Revengeance..." #random seed for genration or actual name
        self.world = WorldGrid.WorldGrid() #is a worldgrid object
        self.seed = None    #will have a random seed that is used to generate the worlds in a deterministic way
    

    def scoreinc(self, value):
        self.score += value
    
    def scoredec(self,value):
        self.score -= value 

    def livesinc(self,value):
        self.lives += value

    def livesdec(self,value):
        self.lives -= value

    def levelnamegen(self):
        self.level = None   #a dict of level names or randomly generated ones

    def setworld(self,world):
        self.world = world

    def seedgen(self, input):
        self.seed = input   # plus what ever random seed generator with input as a key
    
    def newworldgen(self,seed):
        self.seed = seed + None #None is a deterministic addition to seed to create next level from prevoius
    