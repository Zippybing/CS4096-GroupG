class Entity(object):
    def __init__(self, icon, direction, x, y):
        self.icon = icon
        self.direction = direction
        self.x = x
        self.y = y


'''Sub-Entities of Entity'''
class Creature(Entity):
    def __init__(self, icon, direction, x, y, speed, health, name):
        Entity.__init__(self, icon, direction, x, y)
        self.speed = speed
        self.health = health
        self.name = name

    def rotate(self, direction):
        self.direction = direction

class Item(Entity):
    def __init__(self, icon, direction, x, y):
        Entity.__init__(self, icon, direction, x, y)

class Fixture(Entity):
    def __init__(self, icon, direction, x, y, state):
        Entity.__init__(self, direction)
        self.state = state


'''Sub-Entities of Creature'''
class Hero(Creature):
    def __init__(self, icon, direction, x, y, speed, health, name, inventory = []):
        Creature.__init__(self, icon, direction, x, y, speed, health, name)
        self.inventory = inventory

    def addToInventory(self, item):
        self.inventory.append(item)

    def printInventory(self):
        for i in self.inventory:
            print(i)


class Monster(Creature):
    def __init__(self, icon, direction, x, y, speed, health, name, drops = []):
        Creature.__init__(self, icon, direction, x, y, speed, health, name)
        drops = []

    def addDrop(self, drops):
        for d in drops:
            self.drops.append(d)

            
'''Sub-Entities of Fixtures'''
class Door(Fixture):
    def __init__(self, icon, direction, x, y, state, locked, key=None):
        Item.__init__(self, icon, state, direction)
        self.locked = locked
        self.key = key

    def unlockDoor(self):
        self.locked = False

    def openDoor(self):
        self.state = 'Open'

    def closeDoor(self):
        self.state = 'Closed'

'''Sub-Entities of Item'''
class Key(Item):
    def __init__(self, icon, direction, x, y, door=None):
        Item.__init__(self, icon, direction, x, y)
        self.door = door

class Potion(Item):
    pass

class Torch(Item):
    pass

class Gem(Item):
    def __init__(self, icon, direction, x, y, score):
        Item.__init__(self, icon, direction, x, y)
        self.score = score

class Rock(Item):
    def __init__(self, icon, direction, x, y):
        Item.__init__(self, icon, direction, x, y)

'''Sub-Entities of Fixture'''
class Chest(Fixture):
    def __init__(self, icon, direction, x, y, state, locked, items = [], key=None):
        Item.__init__(self, icon, state, direction)
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
