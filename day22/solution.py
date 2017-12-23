#!/usr/bin/python3

# http://adventofcode.com/2017/day/22

from collections import defaultdict

directions = ["up", "right", "down", "left"] # clockwise

def turn_right(direction):
	return directions[(directions.index(direction)+1)%4]

def turn_left(direction):
	return directions[(directions.index(direction)-1)%4]

assert(turn_left("up") 	   == "left")
assert(turn_left("right")  == "up")
assert(turn_left("down")   == "right")
assert(turn_left("left")   == "down")

assert(turn_right("up")    == "right")
assert(turn_right("right") == "down")
assert(turn_right("down")  == "left")
assert(turn_right("left")  == "up")

def get_grid():
	with open("input", "r") as inputfile:
		startgrid = [list(x) for x in inputfile.read().splitlines()]

		x = len(startgrid)//2
		y = len(startgrid)//2

		grid = defaultdict(lambda : defaultdict(lambda: "."))

		for r in range(len(startgrid)):
			for c in range(len(startgrid[r])):
				grid[r][c] = startgrid[r][c]

	return (x,y,grid, len(startgrid), len(startgrid))

def move(x,y,direction):
	if direction == "up":
		return (x,y-1)
	if direction == "down":
		return (x,y+1)
	if direction == "left":
		return (x-1,y)
	if direction == "right":
		return (x+1,y)

def part1():
	x,y,grid,_,_ = get_grid()
	direction  = "up"

	n = 0
	for b in range(10000):
		if grid[y][x] == ".":
			direction  = turn_left(direction)
			grid[y][x] = "#"
			n += 1
		else:
			direction  = turn_right(direction)
			grid[y][x] = "."

		x,y = move(x,y,direction)

	return n

def part2():
	x,y,grid,mx,my = get_grid()
	direction  = "up"

	n = 0
	for b in range(10000000): 
		if grid[y][x] == ".": 		# clean
			direction  = turn_left(direction)
			grid[y][x] = "W"

		elif grid[y][x] == "#": 	# infected
			direction  = turn_right(direction)
			grid[y][x] = "F"
			

		elif grid[y][x] == "F":		# flagged
			grid[y][x] = "."
			# invert direction (left <-> right, up <-> down)
			direction = directions[(directions.index(direction)+2)%4]

		elif grid[y][x] == "W":		# weakened
			grid[y][x] = "#"
			n += 1

		else:
			print("ERROR")

		x,y = move(x,y,direction)

	return n

print("part 1", part1())
print("part 2", part2())