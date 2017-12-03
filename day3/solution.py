#!/usr/bin/python3

# http://adventofcode.com/2017/day/3

import sys
import math
import numpy as np

n = int(sys.argv[1])

x = 0
y = 0

state = "right"
i = 1
cur_steps = 1

sidelength = math.ceil(math.sqrt(n))
if sidelength % 2 == 0:
	sidelength += 1
print("sidelength", sidelength)

grid = [x[:] for x in [[0]*sidelength]*sidelength]
grid[sidelength//2][sidelength//2] = 1

def incr_grid(x,y,val):
	grid[-y + sidelength//2][x + sidelength//2] += val

def get_grid(x,y):	
	return grid[-y + sidelength//2][x + sidelength//2]

def print_grid():
	for line in grid:
		print("\t".join([str(x) for x in line]))

def valid_pos(x,y):
	return x + sidelength//2 in range(sidelength) \
	   and -y + sidelength//2 in range(sidelength)

iters = 0

while i < n:	
	iters += 1
	cur_steps = min(cur_steps, n-i)
	i += cur_steps

	if state == "right":
		for j in range(cur_steps):
			x += 1
			y += 0
			incr_grid(x,y, get_grid(x-1, y))		# left
			incr_grid(x,y, get_grid(x-1, y+1))  	# left up
			incr_grid(x,y, get_grid(x, y+1))  		# up
			if valid_pos(x+1,y+1):
				incr_grid(x,y, get_grid(x+1, y+1))  # up right

		state = "up"

	elif state == "up":
		for j in range(cur_steps):
			x += 0
			y += 1
			incr_grid(x,y, get_grid(x, y-1)) 	# down
			incr_grid(x,y, get_grid(x-1, y-1))	# left down
			incr_grid(x,y, get_grid(x-1, y))	# left
			incr_grid(x,y, get_grid(x-1, y+1))	# left up

		state = "left"
		cur_steps += 1		

	elif state == "left":
		for j in range(cur_steps):
			x -= 1
			y += 0
			incr_grid(x,y, get_grid(x+1, y))	# right
			incr_grid(x,y, get_grid(x, y-1))	# down
			incr_grid(x,y, get_grid(x+1, y-1))  # right down
			if valid_pos(x-1,y-1):
				incr_grid(x,y, get_grid(x-1, y-1))  # left down
			else:
				print("invalid", x-1, y-1)
		
		state = "down"

	else: #down
		for j in range(cur_steps):
			x += 0
			y -= 1
			incr_grid(x,y, get_grid(x+1, y))	# right
			incr_grid(x,y, get_grid(x, y+1))	# up
			incr_grid(x,y, get_grid(x+1, y+1))	# right up
			if valid_pos(x+1,y-1):
				incr_grid(x,y, get_grid(x+1, y-1))	# right down

		state = "right"

		cur_steps += 1
	

print("part 1")
print(abs(x)+abs(y))

print("\npart 2")
flattened = np.array(grid).flatten() 
filtered = [x for x in flattened if x > n]
if len(filtered) > 0:
	print(min(filtered))
else:
	print(flattened)
	print("No x > %d found" % n)