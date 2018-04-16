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
        self.floor = 0
        self.name = "Solid Snake"
        self.level = "Robbing The Three Little Bears Of Everything, Revengeance..." #random seed for genration or actual name
        self.world = WorldGrid.WorldGrid(self) #is a worldgrid object
        self.seed = random.randint(0,5000000)    #will have a random seed that is used to generate the worlds in a deterministic way
        self.hero = Entities.Hero(0,4,'DEFAULT_HERO')
        self.monster = Entities.Monster(5,'DEFAULT_MONSTER')
        self.exit = Entities.Exit()
    

    def checkActive(self):
        return self.hero.isAlive and not self.hero.hasEscaped
        
    # def populate(self):
    #     self.hero.hasEscaped = False
        
    #     self.world.placeEntity(4,5,Entities.Exit())
    #     self.world.placeEntity(5,4,self.hero)
    #     self.world.placeEntity(4,3,self.monster)
        
    #     # self.world.placeEntity(3,4,Entities.Key())
        # self.world.placeEntity(5,5,Entities.Gem(100))
        # self.world.placeEntity(7,3,Entities.Shoes(-1))
        # self.world.placeEntity(10,3,Entities.Potion(1))
        # self.world.placeEntity(7,4,Entities.Torch(1))

    def populate(self):
        self.hero.hasEscaped = False
        generated = []
        
        # Place Exit
        randX ,randY = self.uniqueGen(generated)
        self.world.placeEntity(randX,randY,self.exit)
        generated.append((self.exit.x,self.exit.y))

        # Place Player
        randX ,randY = self.uniqueGen(generated)
        placeAble = self.iDFS((randX,randY),(self.exit.x,self.exit.y))
        while(not placeAble):
            randX ,randY = self.uniqueGen(generated)
            placeAble = self.iDFS((randX,randY),(self.exit.x,self.exit.y))
        self.world.placeEntity(randX,randY,self.hero)
        generated.append((self.hero.x,self.hero.y))
        
        # Place Monster
        randX, randY = self.uniqueGen(generated)
        placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
        while(not placeAble):
            randX ,randY = self.uniqueGen(generated)
            placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
        self.world.placeEntity(randX,randY,self.monster)
        generated.append((self.monster.x,self.monster.y))
        print(generated)
        
        # Place Items
        # Generate Non-Gem Items
        p, t, s = 0, 0, 0
        chance = 10 # Chance of item appearing on level (10%)
        
        # Count Instances of Item in Inventory
        for item in self.hero.inventory:
            if item.icon == 'P':
                p += 1
            elif item.icon == 'T':
                t += 1
            elif item.icon == 'S':
                s += 1

        # Place Potions
        if p < 2 and random.randint(1, 100) < 10:
            randX, randY = self.uniqueGen(generated)
            placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
            while(not placeAble):
                randX ,randY = self.uniqueGen(generated)
                placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
            self.world.placeEntity(randX,randY,Entities.Potion(1))
            generated.append((randX,randY))
            print(generated)

        # Place Torches
        if t < 2 and random.randint(1, 100) < 10:
            randX, randY = self.uniqueGen(generated)
            placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
            while(not placeAble):
                randX ,randY = self.uniqueGen(generated)
                placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
            self.world.placeEntity(randX,randY,Entities.Torch(1))
            generated.append((randX,randY))
            print(generated)

        # Place Shoes
        if s < 2 and random.randint(1, 100) < 10:
            randX, randY = self.uniqueGen(generated)
            placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
            while(not placeAble):
                randX ,randY = self.uniqueGen(generated)
                placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
            self.world.placeEntity(randX,randY,Entities.Shoes(-1))
            generated.append((randX,randY))
            print(generated)

        # Place Gems
        for _ in range(5): # Places 5 Gems
            randX, randY = self.uniqueGen(generated)
            placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
            while(not placeAble):
                randX ,randY = self.uniqueGen(generated)
                placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
            self.world.placeEntity(randX,randY,Entities.Gem(100))
            generated.append((randX,randY))
            print(generated)

        '''
        self.world.placeEntity(5,5,Entities.Gem(100))
        self.world.placeEntity(7,3,Entities.Shoes(-1))
        self.world.placeEntity(10,3,Entities.Potion(1))
        self.world.placeEntity(7,4,Entities.Torch(1))
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
                    
        
        