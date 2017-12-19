#!/usr/bin/python3

# http://adventofcode.com/2017/day/19

with open("input") as inputfile:
	grid = inputfile.read().splitlines()

	y = 0
	x = grid[y].index("|")

	direction = (0,1) #(x,y)

	c = grid[y][x]

	seen = []

	steps = 0

	while c != " ":
		steps += 1
		x += direction[0]
		y += direction[1]		

		c = grid[y][x]

		if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			seen.append(c)
		elif c == "+":
			if direction in [(0,1), (0,-1)]:
				if grid[y][x+1] != " ":
					direction = (1,0)
				else:
					direction = (-1,0)
			elif direction in [(1,0), (-1,0)]:
				if y+1 < len(grid) and grid[y+1][x] != " ":
					direction = (0,1)
				else:
					direction = (0,-1)

	print("part 1", "".join(seen))
	print("part 2", steps)