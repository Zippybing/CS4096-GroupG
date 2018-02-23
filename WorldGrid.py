#import Tile
import sys
import Tile
import Entities

class WorldGrid:
    def __init__(self):
        self.grid = None
    #Initialize a map filled with tiles.
    def createMap(self, x,y):
        self.grid = [ [Tile.Floor('White') for _ in range(y)] for _ in range(x)]
        
    #Print to the console ASCII representation of map
    def displayGrid(self):
        for y in range(len(self.grid[0])-1):
            for x in range(len(self.grid)-1):
                sys.stdout.write('['+self.grid[x][y].print_icon()+']')
                #sys.stdout.write('['+str(issubclass(type(self.grid[x][y].entity),Entities.Entity))+']')
            sys.stdout.write('\n')
            sys.stdout.flush()
            
    #Used by the map generator function to place entities in specific tile  
    def placeEntity(self, x, y, e):
        self.grid[x][y].entity = e
        
    #Used to move entities from one tile to another
    def moveEntity(self, x1, y1, x2, y2):
        # MUY IMPORTANTE: issubclass(type(self.grid[x][y].entity),Entities.Entity)
        agent = self.grid[x1][y1].entity
        target = self.grid[x2][y2].entity
        
        if target is not None:
            if type(agent) == Entities.Hero:
                if issubclass(type(target),Entities.Item):
                    print("Picked up item!")
                    # Add item to inventory
                    # Move hero to space
                elif type(target) == Entities.Monster:
                    # Kill Hero
                    # Do not move
                    print("YOU REALLY DIED")
            if type(agent) == Entities.Monster:
                if type(target) == Entities.Hero:
                    print("YOU DIED")
                    
        self.grid[x2][y2].entity = self.grid[x1][y1].entity
        self.grid[x1][y1].entity = None
        
    #Resets all sound values to 0
    def clearNoises(self):
        for i in self.grid:
            for j in i:
                j.noise = 0
    
    #Propagates sound values from tile evenly
    def distributeNoise(self, x, y, noise):
        if noise == 0 or x<0 or y<0 or x>len(self.grid)-1 or y>len(self.grid[0])-1:
            return
        else:
            if self.grid[x][y].noise < noise:
                self.grid[x][y].noise = noise
            self.distributeNoise(x-1, y, noise-1)    #left
            self.distributeNoise(x+1, y, noise-1)    #right
            self.distributeNoise(x, y-1, noise-1)    #up
            self.distributeNoise(x, y+1, noise-1)    #down
            return
