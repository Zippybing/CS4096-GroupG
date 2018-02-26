import Entities

class Tile(object):
    def __init__(self, color, entity = None):
        # Initialize with tile type, entity
        # Set noise to 0 by default
        # Tile type will be string, e.g. "FLOOR", "WALL", "DOOR"
        self.entity = entity
        self.color = color
        self.noise = 0

    def clear_noise(self):
        self.noise = 0
        
    def print_icon(self):
        if self.entity == None:
            return self.icon
        return self.entity.icon
    

    def print_rep(self):
        if self.entity == None:
            return self.rep
        return self.entity.rep
    
        
class Floor(Tile):
    def __init__(self, color, entity=None):
        Tile.__init__(self, color, entity)
        self.icon = '.'
        self.rep = [(0,0,2)]


class Wall(Tile):
    def __init__(self, color, entity=None):
        Tile.__init__(self, color, entity)
        self.icon = '#'
        self.rep = [(1,0,0)]

    # TO-DO: Add copy function

# Testing example
#example_tile = Tile("floor")
#print(example_tile.type, example_tile.entity, example_tile.noise)
#> FLOOR None 0


