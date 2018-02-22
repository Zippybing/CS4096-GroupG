import WorldGrid

class Tile:
    def __init__(self, noise, generator):
        self.noise = noise
        self.generator = generator

def main():

    a = WorldGrid.WorldGrid()

    a.createMap(10,12)

    a.displayGrid()

    print()
    for i in a.grid:
        for j in i:
            j = '1'

    a.placeEntity(3,2,Tile(7, True))

    a.placeEntity(7,6,Tile(5, True))
    
    a.displayGrid()
    
    a.distributeNoise(3, 2, a.grid[3][2].noise)
    a.distributeNoise(7, 6, a.grid[7][6].noise)
    
    print()
    a.displayGrid()
    
    a.clearNoises()
    
    print()
    a.displayGrid()
    
if __name__ == '__main__':
    main()