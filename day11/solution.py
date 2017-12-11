#!/usr/bin/python3

# http://adventofcode.com/2017/day/11

import math

def calc_steps(instructions):	
	# use cube coordinates
	# https://www.redblobgames.com/grids/hexagons/#coordinates
	# x + y + z = 0 for all cells, so each move involves changing two
	# variables out of x,y,z
	x = y = z = 0
	instructions = instructions.split(",")
	
	dists = []

	for instr in instructions:		
		if instr == "n":
			y += 1
			z -= 1
		if instr == "nw":
			y += 1
			x -= 1
		if instr == "ne":
			x += 1
			z -= 1
		if instr == "s":
			y -= 1
			z += 1
		if instr == "sw":
			x -= 1
			z += 1
		if instr == "se":
			y -= 1
			x += 1
		dists.append(int((abs(x)+abs(y)+abs(z))/2))


	return (int((abs(x) + abs(y) + abs(z))/2), max(dists))

print(calc_steps("ne,ne,ne"))
assert(calc_steps("ne,ne,ne")[0] == 3)

print(calc_steps("ne,ne,sw,sw"))
assert(calc_steps("ne,ne,sw,sw")[0] == 0)

print(calc_steps("ne,ne,s,s"))
assert(calc_steps("ne,ne,s,s")[0] == 2)

print(calc_steps("se,sw,se,sw,sw"))
assert(calc_steps("se,sw,se,sw,sw")[0] == 3)

with open("input") as inputfile:
	instructions = inputfile.read().splitlines()[0]
	print("part 1", calc_steps(instructions)[0], "steps are required")
	print("part 2", calc_steps(instructions)[1], "steps is the farthest distance")


