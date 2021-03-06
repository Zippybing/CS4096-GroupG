import sys
import Tile
import Entities
import random
import math

from Config import getValue
from LevelGenerator import create_level

class WorldGrid:
    def __init__(self,game):
        self.grid = None
        self.width = None
        self.height = None
        self.vizgrid = None
        self.gamestate = game
        
    #Initialize a map filled with tiles.
    def createMap(self, x, y):
        self.grid = [ [Tile.Tile('White') for _ in range(y)] for _ in range(x)]
        self.width = x
        self.height = y
        # Create a base from LevelGenerator
        base = create_level(x, y)
        # Fill the game grid with entities corresponding to entries in the base
        for i in range(len(base[0])):
            for j in range(len(base)):
                if base[i][j] == 1:
                    self.placeEntity(i, j, Entities.Wall())
        

    def displayGridnorm(self):
        gridtext = [[],[]]
        for y in range(len(self.grid[0])):
            rowtext = ""
            colorrow =[]
            for x in range(len(self.grid)):
                
                rowtext += ' '+self.grid[x][y].print_icon()+' '
                #Noise Visualizer
                #rowtext += ' '+str(self.grid[x][y].noise)+' '
                colorrow += self.grid[x][y].print_rep() + self.grid[x][y].print_rep() + self.grid[x][y].print_rep()
                
            gridtext[0] += [str(rowtext)]
            gridtext[1] += [colorrow]
            sys.stdout.flush()
            self.vizgrid = gridtext
        return gridtext   


    #Print to the console ASCII representation of map
    def displayGridH(self):
        gridtext = [[],[]]
        for y in range(len(self.grid[0])):
            rowtext = ""
            colorrow =[]
            for x in range(len(self.grid)):
                inRange = False
                xdiff = self.gamestate.hero.visual
                ydiff = 2
                rng = xdiff - ydiff + 1
                for c in range(rng):
                    if x < self.gamestate.hero.x + xdiff and x > self.gamestate.hero.x - xdiff and y < self.gamestate.hero.y + ydiff and y > self.gamestate.hero.y - ydiff:
                        inRange = True
                    xdiff -= 1
                    ydiff += 1
                if inRange == True:
                    #sys.stdout.write('['+self.grid[x][y].print_icon()+']')
                    rowtext += ' '+self.grid[x][y].print_icon()+' '
                    #Noise Visualizer
                    #rowtext += ' '+str(self.grid[x][y].noise)+' '
                    colorrow += self.grid[x][y].print_rep() + self.grid[x][y].print_rep() + self.grid[x][y].print_rep()
                else :
        		    #sys.stdout.write('['+self.grid[x][y].print_icon()+']')
                    rowtext += '   '
                    #Noise Visualizer
                    #rowtext += ' '+str(self.grid[x][y].noise)+' '
                    colorrow += [(0,0,0)] + [(0,0,0)] + [(0,0,0)]
            gridtext[0] += [str(rowtext)]
            gridtext[1] += [colorrow]
            sys.stdout.flush()
            self.vizgrid = gridtext
        return gridtext


    def displayGridM(self):
        gridtext = [[],[]]
        for y in range(len(self.grid[0])):
            rowtext = ""
            colorrow =[]
            for x in range(len(self.grid)):
                #sys.stdout.write('['+self.grid[x][y].print_icon()+']')
                if( not isinstance(self.grid[x][y].entity,(Entities.Wall,Entities.Monster)) ):
                    rowtext += ' '+str(self.grid[x][y].noise)+' '
                    noiserep = self.grid[x][y].print_rep()
                    noiserep = [(3,noiserep[0][1],0)]
                else:
                    rowtext += ' '+self.grid[x][y].print_icon()+' '
                    noiserep = self.grid[x][y].print_rep()
                    noiserep = [(noiserep[0][0],noiserep[0][1],0)]
                colorrow += noiserep + noiserep + noiserep
                #sys.stdout.write('['+self.grid[x][y].print_icon()+']')
                
                #Noise Visualizer
                #rowtext += ' '+str(self.grid[x][y].noise)+' '
                
            gridtext[0] += [str(rowtext)]
            gridtext[1] += [colorrow]
            sys.stdout.flush()
            self.vizgrid = gridtext
        return gridtext

    #Used by the map generator function to place entities in specific tile
    # Now overrides the entity's location attributes w/ where it is placed
    def placeEntity(self, x, y, e):
        # Override the entity's location attributes w/ placement coordinates
        if e is not None:
            e.x = x
            e.y = y
        self.grid[x][y].entity = e
        
        
    #Used to move entities from one tile to another

    def tryMoveEntity(self, x1, y1, x2, y2):
        # MUY IMPORTANTE: issubclass(type(self.grid[x][y].entity),Entities.Entity)
        #print(x1, y1, x2, y2)
        score = 0
        # QUICK HACK: DON'T LET ENTITY MOVE ONTO ITSELF
        if x2 >= 0 and x2 < self.width and y2 >= 0 and y2 < self.height:
            if x1 == x2 and y1 == y2:
                return
            agent = self.grid[x1][y1].entity
            target = self.grid[x2][y2].entity
            
            if target is not None:
                #Creature
                if issubclass(type(agent),Entities.Creature):
                    #Hero
                    if type(agent) == Entities.Hero:
                        if type(target) == Entities.Firecracker:
                            self.moveEntity(x1, y1, x2, y2, agent, None)
                            randX = random.randint(0,5) * random.randint(-1,1)
                            randY = random.randint(0,5) * random.randint(-1,1)
                            placeAble = type(self.grid[randX][randY].entity) != Entities.Wall
                            farEnough = math.floor(math.sqrt(math.pow(randX,2) + math.pow(randY,2)))
                            while(not placeAble and farEnough < 3):
                                randX = random.randint(0,5) * random.randint(-1,1)
                                randY = random.randint(0,5) * random.randint(-1,1)
                                placeAble = type(self.grid[randX][randY].entity) != Entities.Wall
                                farEnough = math.floor(math.sqrt(math.pow(randX,2) + math.pow(randY,2)))
                            
                            self.distributeNoise(x2+randX,y2+randY,7)
                        elif issubclass(type(target),Entities.Item):
                            # print("Picked up item!") # Temporarily removed. Causes problems w/ Mac.
                            # Add item to inventory
                            #agent.addToInventory(target)
                            # agent.printInventory() # BREAKS SCREEN RENDERING LOOP
                            # Move hero to space
                            agent.inventory.append(target)
                            agent.namedinv.append(target.name)
                            self.moveEntity(x1, y1, x2, y2, agent, None)
                        elif type(target) == Entities.Monster:
                            gun = None
                            for item in agent.inventory:
                                if type(item) == Entities.Shotgun and item.ammo == True:
                                    gun = item
                                    self.gamestate.score +=500
                                    target.isAlive = False
                                    gun.ammo = False
                                    self.distributeNoise(x2,y2,9)
                                    self.moveEntity(x1, y1, x2, y2, agent, None)
                                    break
                            if gun is None:
                                # Kill Hero
                                # Do not move
                                print("YOU REALLY DIED")
                                agent.isAlive = False
                                self.placeEntity(x1,y1,None)
                                self.gamestate.score +=500
                                return
                        elif type(target) == Entities.Exit:
                            print("YOU ESCAPED THE LEVEL")
                            agent.hasEscaped = True
                            self.gamestate.score +=100*self.gamestate.floor
                            self.placeEntity(x1,y1,None)
                            return
                    #Monster
                    elif type(agent) == Entities.Monster:
                        if type(target) == Entities.Hero:
                            print("YOU DIED")
                            target.isAlive = False
                            self.moveEntity(x1, y1, x2, y2, agent, None)
                            self.gamestate.score -=1000
                        elif type(target) != Entities.Wall:
                            self.moveEntity(x1, y1, x2, y2, agent, target)
            else:
                self.moveEntity(x1, y1, x2, y2, agent, target)
    
    def moveEntity(self, x1, y1, x2, y2, agent, target):
        agent.x = x2
        agent.y = y2
        if target:
            target.x = x1
            target.y = y1
        self.grid[x2][y2].entity = agent
        self.grid[x1][y1].entity = target
        #print(self.grid[x2][y2].entity, self.grid[x1][y1].entity)
    
    #Resets all sound values to 0
    def clearNoises(self):
        for i in self.grid:
            for j in i:
                j.noise = 0
    
    #Propagates sound values from tile evenly
    def distributeNoise(self, x, y, noise):
        if (noise == 0 or x<0 or y<0 or x>len(self.grid)-1 or y>len(self.grid[0])-1) or (isinstance(self.grid[x][y].entity,Entities.Wall)):
            return
        else:
            if self.grid[x][y].noise < noise:
                self.grid[x][y].noise = noise
            self.distributeNoise(x-1, y, noise-1)    #left
            self.distributeNoise(x+1, y, noise-1)    #right
            self.distributeNoise(x, y-1, noise-1)    #up
            self.distributeNoise(x, y+1, noise-1)    #down
            return
