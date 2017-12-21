#!/usr/bin/python3

# http://adventofcode.com/2017/day/21

import numpy as np

# numpy 2D array to string representation
def get_strrep(patch):
	return "/".join("".join(patch[k]) for k in range(len(patch)))

# string representation to 2D numpy array
def get_arrrep(strrep):
	return np.array([list(x) for x in strrep.split("/")])

# Iterates over the grid, splits it into local patches of
# given size and applies the replacement rules to each patch
def do_replacement(grid, rules, amount, size):
	columns = []
	for r in range(amount):
		rows = []
		for c in range(amount):
			patch = grid[r*size:r*size+size,c*size:c*size+size]
			src = get_strrep(patch)
			
			assert src in rules,  "No rule found for '%s'" % src			
			dst = get_arrrep(rules[src])
			rows.append(dst)
			
		columns.append(np.concatenate(rows, 1))
	return np.concatenate(columns, 0)

def run(iterations):
	with open("input") as inputfile:
		lines = inputfile.read().splitlines()

		rules =  {x[0] : x[1] for x in (x.split(" => ") for x in lines)}

		for src in list(rules):
			dst = rules[src]

			srcparts = get_arrrep(src)
			
			# rotate by 0 / 90 / 180 / 270 degree and add new rule to rules
			# additionally every rotated rule is also flipped horicontally
			# and added to the rules list
			for k in range(4):
				rotatedarr = np.rot90(srcparts, k, (0,1))
				rotatedstr = get_strrep(rotatedarr)
				if rotatedstr not in rules:
					rules[rotatedstr] = dst

				flippedarr = np.flip(rotatedarr, 1)
				flippedstr = get_strrep(flippedarr)
				if flippedstr not in rules:
					rules[flippedstr] = dst


		grid = np.array([[".", "#", "."],
						 [".", ".", "#"],
						 ["#", "#", "#"]])

		for it in range(iterations):
			size = grid.shape[0]
			
			if size % 2 == 0:
				grid = do_replacement(grid, rules, size//2, 2)
			elif size % 3 == 0:
				grid = do_replacement(grid, rules, size//3, 3)

			else:
				print("size %2 and %3 not 0")

		return sum((sum(c == "#" for c in r)) for r in grid)
	
print("part 1", run(5))
print("part 1", run(18))