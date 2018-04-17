# cave_gen.py
# Stand-alone file
# Generates a cave using cellular automata, then prints it to console
# Uses a grid initialization and display scheme that provides for using grid[x][y] syntax

import sys
import random

from Config import getValue

# Seed random
random.seed(getValue('LevelGenerator', 'seed', 'int'))

# Proof of [x][y] concept -- 
# is actually put into grid as [y=0][x=2], but print_grid displays as [x=0][y=2]
# grid[0][2] = 1

def create_level(grid_width, grid_height):
	# Create a blank grid to give back to the WorldGrid createMap function
	grid = [[0 for i in range(grid_height)] for j in range(grid_width)]

	# Initialize the grid by randomly filling it with wall tiles
	# The first parameter is the % chance that a random cell becomes a tile
	# recommended chance %: 35-39
	initialize_grid(getValue('LevelGenerator', 'genChance', 'int'), grid, grid_width, grid_height)

	# Run the simulation steps
	for i in range(7):
		do_simulation_step(getValue('LevelGenerator', 'birthLimit', 'int'), getValue('LevelGenerator', 'deathLimit', 'int'), grid, grid_width, grid_height)

	# Fill the grid's edges with walls to prevent player exiting map's sides
	fill_grid_walls(grid, grid_width, grid_height)

	# Print the grid, for debug purposes
	#print_grid(grid, grid_width, grid_height)

	# Give the grid back to whatever called this function
	return grid

def print_grid(grid, grid_width, grid_height):
	# Normal printing of the grid
	# for y in range(grid_width):
	#		for x in range(grid_height):
	#			sys.stdout.write(str(grid[y][x]))
	#		sys.stdout.write('\n')
	#		sys.stdout.flush()
	# Revised printing of the grid
	for y in range(grid_height):
		for x in range(grid_width):
			if grid[x][y] == 0:
				sys.stdout.write('.')
			if grid[x][y] == 1:
				sys.stdout.write('#')
		sys.stdout.write('\n')
		sys.stdout.flush()

def print_numerical_grid(g):
	for y in range(grid_height):
		for x in range(grid_width):
			sys.stdout.write(str(g[x][y]))
		sys.stdout.write('\n')
		sys.stdout.flush()

def initialize_grid(chance, grid, grid_width, grid_height):
	for y in range(grid_height):
		for x in range(grid_width):
			if random.randrange(100) < chance:
				grid[x][y] = 1

def count_alive_neighbors(grid, grid_width, grid_height):
	# Create new grid
	grid_count = [[0 for i in range(grid_height)] for j in range(grid_width)]
	# Iterate through grid
	for y in range(grid_height):
		for x in range(grid_width):
			# Initialize variables
			count = 0
			# Iterate through neighbors (and corners)
			# If neighbor is 'alive' (wall) or outside of grid, add to count
			for i in range(-1,2):
				for j in range(-1,2):
					# Check for x being outside of grid
					if (x + i) < 0 or (x + i) >= grid_width:
						count += 1
					# Check for y being outside of grid
					elif (y + j) < 0 or (y + j) >= grid_height:
						count += 1
					# Ignore the space itself
					elif (x + i) == x and (y + j) == y:
						pass
					# Space is in grid, check for alive (wall) / dead (floor)
					else:
						if grid[x + i][y + j] == 1:
							count += 1
			# Set new grid to the count
			grid_count[x][y] = count
	#print_numerical_grid(grid_count)
	return grid_count

def do_simulation_step(birth_limit, death_limit, grid, grid_width, grid_height):
	grid_count = count_alive_neighbors(grid, grid_width, grid_height)
	# Iterate through grid
	for y in range(grid_height):
		for x in range(grid_width):
			# If 'alive'
			if grid[x][y] == 1:
				# If it has too few neighbors, kill it
				if grid_count[x][y] < death_limit:
					grid[x][y] = 0
			# If 'dead'
			if grid[x][y] == 0:
				# Check to see if it has enough neighbors to revive it
				if grid_count[x][y] > birth_limit:
					grid[x][y] = 1

def fill_grid_walls(grid, grid_width, grid_height):
	for x in range(grid_width):
		grid[x][0] = 1
		grid[x][grid_height - 1] = 1
	for y in range(grid_height):
		grid[0][y] = 1
		grid[grid_width - 1][y] = 1