class Tile:
	def __init__(self, type, entity = None):
		# Initialize with tile type, entity
		# Set noise to 0 by default
		# Tile type will be string, e.g. "FLOOR", "WALL", "DOOR"
		self.type = type.upper()
		self.entity = entity
		self.noise = 0

	def clear_noise(self):
		self.noise = 0

	# TO-DO: Add copy function

# Testing example
#example_tile = Tile("floor")
#print(example_tile.type, example_tile.entity, example_tile.noise)
#> FLOOR None 0


