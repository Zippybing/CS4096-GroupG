from Config import getValue


class Entity(object):
    def __init__(self):
        pass


'''Sub-Entities of Entity'''
class Creature(Entity):
    def __init__(self, actionCap, name):
        Entity.__init__(self)
        self.actionCap = actionCap
        self.name = name

class Item(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.applied = False

class Fixture(Entity):
    def __init__(self, state):
        Entity.__init__(self)
        self.state = state


'''Sub-Entities of Creature'''
class Hero(Creature):
    def __init__(self, actionCap, name, inventory = []):
        Creature.__init__(self, actionCap, name)
        self.icon = 'H'
        self.rep = [(7,2,2)]       
        self.hasEscaped = False
        self.isAlive = True
        self.inventory = inventory
        self.noise = 5
        self.visual = 4
        
    def addToInventory(self, item):
        self.inventory.append(item)

    def printInventory(self):
        for i in self.inventory:
            print(i)

class Monster(Creature):
    def __init__(self, actionCap, name, drops = []):
        self.icon = 'M'
        self.rep = [(1,1,2)]
        Creature.__init__(self, actionCap, name)
        drops = []

    def addDrop(self, drops):
        for d in drops:
            self.drops.append(d)

            

        
'''Sub-Entities of Item'''
class Potion(Item):
    def __init__(self, actionMod):
        self.icon = 'P'
        self.rep = [(5,4,2)]
        Item.__init__(self)
        self.actionMod = actionMod

class Torch(Item):
    def __init__(self, visMod):
        self.icon = 'T'
        self.rep = [(5,4,2)]
        Item.__init__(self)
        self.visMod = visMod

class Gem(Item):
    def __init__(self, scoreMod):
        self.icon = 'G'
        Item.__init__(self)
        self.scoreMod = scoreMod
        self.rep = [(5,4,2)]

class Shoes(Item):
    def __init__(self, noiseMod):
        self.icon = 'S'
        Item.__init__(self)
        self.rep = [(5,4,2)]
        self.noiseMod = noiseMod

# Non Functional Items, Do Not Use
class Rock(Item):
    def __init__(self):
        self.icon = 'R'
        Item.__init__(self)
        self.rep = [(5,4,2)]

class Key(Item):
    def __init__(self, door=1234):
        self.icon = 'K'
        self.rep = [(5,4,2)]
        Item.__init__(self)
        self.door = door

'''Sub-Entities of Fixture'''

class Door(Fixture):
    def __init__(self, state, locked, key=None):
        Fixture.__init__(self, state)
        self.icon = 'D'
        self.locked = locked
        self.key = key

    def unlockDoor(self):
        self.locked = False

    def openDoor(self):
        self.state = 'Open'

    def closeDoor(self):
        self.state = 'Closed'

class Exit(Fixture):
    def __init__(self, state=None):
        self.icon = 'E'
        self.rep = [(5,4,2)]
        Fixture.__init__(self, state)

class Chest(Fixture):
    def __init__(self, state, locked, items = [], key=None):
        self.icon = 'C'
        Item.__init__(self, state)
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

class Wall(Fixture):
    def __init__(self):
        Fixture.__init__(self, state="Wall?")
        self.icon = '#'
        self.rep = [(5,1,2)]
