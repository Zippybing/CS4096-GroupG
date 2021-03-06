#Author: Kyle Cusack & Michael Eschbacher
#Email: kdc6w3@mst.edu
#Assignment: Game State for Python game
#Description: The Game State for the rogue-like stealth game

import WorldGrid
import Entities
import random
import math

from Config import getValue

class GameState:
    def __init__(self):
        self.seed = random.randint(0,765867586578)    #will have a random seed that is used to generate the worlds in a deterministic way
        self.score = 0
        self.floor = 0
        self.name = "Solid Snake"
        self.level = getValue('GameState', 'level', 'str') #random seed for genration or actual name
        self.world = WorldGrid.WorldGrid(self) #is a worldgrid object
        self.newseed = getValue('GameState', 'seed', 'int')    #will have a random seed that is used to generate the worlds in a deterministic way 
        self.hero = Entities.Hero(getValue('Entities', 'heroMove', 'int'), getValue('Entities', 'heroName', 'str'))
        self.monsters = []
        self.exit = Entities.Exit()
    

    def checkActive(self):
        return self.hero.isAlive and not self.hero.hasEscaped

    def populate(self):
        self.hero.hasEscaped = False
        for item in self.hero.inventory:
            if type(item) == Entities.Shotgun:
                item.ammo = True
                break
                                    
        generated = []
        numberOfMonsters = self.calculateMonsterQuantity()
        
        self.monsters.clear() 
        for i in range(numberOfMonsters): 
            self.monsters.append(Entities.Monster(getValue('Entities', 'monsterMove', 'int'), getValue('Entities', 'monsterName', 'str')))
        
        # Place Exit
        randX ,randY = self.uniqueGen(generated)
        while self.world.grid[randX][randY].entity is not None:
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
        
        # Place Monster(s)
        # Clear the list of monsters from previous levels
        for i in range(numberOfMonsters): 
            randX, randY = self.uniqueGen(generated)
            placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
            while(not placeAble):
                randX ,randY = self.uniqueGen(generated)
                placeAble = self.iDFS((randX,randY),(self.hero.x,self.hero.y))
            self.world.placeEntity(randX,randY,self.monsters[i])
            generated.append((self.monsters[i].x,self.monsters[i].y))
            print(generated)
        
        # Place Items
        # Generate Non-Gem Items
        p, t, s, u = 0, 0, 0, 0
        chance = getValue('GameState', 'chance', 'int') # Chance of item appearing on level (10%)
        chanceShotgun = getValue('GameState', 'chanceShotgun', 'int')
        
        # Count Instances of Item in Inventory
        for item in self.hero.inventory:
            if item.icon == 'P':
                p += 1
            elif item.icon == 'T':
                t += 1
            elif item.icon == 'S':
                s += 1
            elif item.icon == 'U':
                u += 1


        # Place Potions
        if p <= 2 and random.randint(1, 100) < chance:
            randX, randY = self.uniqueGen(generated)
            placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            while(not placeAble):
                randX ,randY = self.uniqueGen(generated)
                placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            self.world.placeEntity(randX,randY,Entities.Potion(getValue('Entities', 'potionMoveMod', 'int')))
            generated.append((randX,randY))
            print(generated)

        # Place Torches
        if t <= 2 and random.randint(1, 100) < chance: 
            randX, randY = self.uniqueGen(generated)
            placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            while(not placeAble):
                randX ,randY = self.uniqueGen(generated)
                placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            self.world.placeEntity(randX,randY,Entities.Torch(getValue('Entities', 'torchVisMod', 'int')))
            generated.append((randX,randY))
            print(generated)

        # Place Shoes
        if s <= 2 and random.randint(1, 100) < chance:
            randX, randY = self.uniqueGen(generated)
            placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            while(not placeAble):
                randX ,randY = self.uniqueGen(generated)
                placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            self.world.placeEntity(randX,randY,Entities.Shoes(getValue('Entities', 'shoeNoiseMod', 'int')))
            generated.append((randX,randY))
            print(generated)
            
        # Place Shotgun
        if u <= 1 and random.randint(1, 100) < chanceShotgun:
            randX, randY = self.uniqueGen(generated)
            placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            while(not placeAble):
                randX ,randY = self.uniqueGen(generated)
                placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            self.world.placeEntity(randX,randY,Entities.Shotgun())
            generated.append((randX,randY))
            print(generated)

        # Place Gems
        for _ in range(getValue('Entities', 'fireNum', 'int')): # Places Gems
            randX, randY = self.uniqueGen(generated)
            placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            while(not placeAble):
                randX ,randY = self.uniqueGen(generated)
                placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            self.world.placeEntity(randX,randY,Entities.Firecracker(getValue('Entities', 'gemWorth', 'int')))
            generated.append((randX,randY))
            print(generated)
        
        
        # Place Gems
        for _ in range(getValue('Entities', 'gemNum', 'int')): # Places Gems
            randX, randY = self.uniqueGen(generated)
            placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            while(not placeAble):
                randX ,randY = self.uniqueGen(generated)
                placeAble = type(self.world.grid[randX][randY].entity) != Entities.Wall
            self.world.placeEntity(randX,randY,Entities.Gem(getValue('Entities', 'gemWorth', 'int')))
            generated.append((randX,randY))
            print(generated)

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
                    
        
    def calculateMonsterQuantity(self):
        n = getValue('GameState', 'monstern', 'int') # Increase number of monsters spawned every 'n' number of levels 
        monstersMax = getValue('GameState', 'monsterMax', 'int')
        monsters = math.ceil(self.floor / n) # Number of monsters to spawn in level
        if monsters < 1:
            monsters = 1 # Don't allow game to not spawn any monsters
        elif monsters > monstersMax:
            monsters = monstersMax # Don't allow game to flood level with monsters
        return monsters
