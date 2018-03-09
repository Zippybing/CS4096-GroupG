class Entity(object):
    def __init__(self, icon, x, y):
        self.icon = icon
        self.x = x
        self.y = y


'''Sub-Entities of Entity'''
class Creature(Entity):
    def __init__(self, icon, x, y, speed, health, name):
        Entity.__init__(self, icon, x, y)
        self.speed = speed
        self.health = health
        self.name = name

class Item(Entity):
    def __init__(self, icon, x, y):
        Entity.__init__(self, icon, x, y)

class Fixture(Entity):
    def __init__(self, icon, x, y, state):
        Entity.__init__(self, icon, x, y)
        self.state = state


'''Sub-Entities of Creature'''
class Hero(Creature):
    def __init__(self, icon, direction, x, y, speed, health, name, inventory = []):
        Creature.__init__(self, icon, x, y, speed, health, name)
        self.rep = [(7,2,2)]       
        self.hasEscaped = False
        self.isAlive = True
        self.inventory = inventory
        
    def addToInventory(self, item):
        self.inventory.append(item)

    def printInventory(self):
        for i in self.inventory:
            print(i)

class Monster(Creature):
    def __init__(self, icon, x, y, speed, health, name, drops = []):
        self.rep = [(1,1,2)]
        Creature.__init__(self, icon, x, y, speed, health, name)
        drops = []

    def addDrop(self, drops):
        for d in drops:
            self.drops.append(d)

            
'''Sub-Entities of Fixtures'''
class Door(Fixture):
    def __init__(self, icon, x, y, state, locked, key=None):
        Fixture.__init__(self, icon, state)
        self.locked = locked
        self.key = key

    def unlockDoor(self):
        self.locked = False

    def openDoor(self):
        self.state = 'Open'

    def closeDoor(self):
        self.state = 'Closed'

class Exit(Fixture):
    def __init__(self, icon, x, y, state=None):
        self.rep = [(5,4,2)]
        Fixture.__init__(self, icon, x, y, state)
        
'''Sub-Entities of Item'''
class Key(Item):
    def __init__(self, icon, x, y, door=1234):
        self.rep = [(5,4,2)]
        Item.__init__(self, icon, x, y)
        self.door = door

class Potion(Item):
    def __init__(self, icon, x, y, color='Red'):
        self.rep = [(5,4,2)]
        Item.__init__(self, icon, x, y)
        self.color = color

class Torch(Item):
    pass

class Gem(Item):
    def __init__(self, icon, x, y, score):
        Item.__init__(self, icon, x, y)
        self.score = score
        self.rep = [(5,4,2)]

class Rock(Item):
    def __init__(self, icon, x, y):
        Item.__init__(self, icon, x, y)
        self.rep = [(5,4,2)]

class Shoes(Item):
    def __init__(self, icon, x, y):
        Item.__init__(self, icon, x, y)
        self.rep = [(5,4,2)]

'''Sub-Entities of Fixture'''
class Chest(Fixture):
    def __init__(self, icon, x, y, state, locked, items = [], key=None):
        Item.__init__(self, icon, state)
        self.items = items
        self.locked = locked
        self.key = key

    def unlockChest(self):
        self.locked = False

    def openChest(self):
        self.state = 'Open'

    def closeChest(self):
        self.state = 'Closed'

class Trap(Fixture):
    pass
