class Entity(object):
    def __init__(self, icon, direction):
        self.icon = icon
        self.direction = direction


'''Sub-Entities of Entity'''
class Creature(Entity):
    def __init__(self, icon, direction, speed, health, name):
        Entity.__init__(self, icon, direction)
        self.speed = speed
        self.health = health
        self.name = name

    def rotate(self, direction):
        self.direction = direction

class Item(Entity):
    def __init__(self, icon, direction):
        Entity.__init__(self, direction)

class Fixture(Entity):
    def __init__(self, icon, direction, state):
        Entity.__init__(self, direction)
        self.state = state


'''Sub-Entities of Creature'''
class Hero(Creature):
    def __init__(self, icon, direction, speed, health, name):
        Creature.__init__(self, icon, direction, speed, health, name)


class Monster(Creature):
    def __init__(self, icon, direction, speed, health, name, drops = []):
        Creature.__init__(self, direction, speed, health, name)
        drops = []

    def addDrop(self, drops):
        for d in drops:
            self.drops.append(d)

            
'''Sub-Entities of Fixtures'''
class Door(Fixture):
    def __init__(self, icon, direction, state, locked, key=None):
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
    def __init__(self, icon, direction, door=None):
        Item.__init__(self, icon, direction)
        self.door = door

class Potion(Item):
    pass

class Torch(Item):
    pass

class Chest(Fixture):
    def __init__(self, icon, direction, state, locked, items = [], key=None):
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
