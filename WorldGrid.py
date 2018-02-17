#import Tile

import Tile

class WorldGrid:
    def __init__(self):
        self.grid = None
    #Initialize a map filled with tiles.
    def createMap(self, x,y):
        self.grid = [ [Tile.Floor('White') for _ in range(y)] for _ in range(x)]
        
    #Print to the console ASCII representation of map
    def displayGrid(self):
        for i in self.grid:
            for j in i:
                print('['+str(j.print_icon())+']', end='')
            print()
            
    #Used by the map generator function to place entities in specific tile  
    def placeEntity(self, x, y, e):
        self.grid[x][y].entity = e
        
    #Used to move entities from one tile to another
    def moveEntity(self, x1, y1, x2, y2):
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
