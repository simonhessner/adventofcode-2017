#!/usr/bin/python3

# http://adventofcode.com/2017/day/5

import sys
import numpy
import math

def solve(part):
	cur_pos = 0
	steps = 0

	with open("input") as inputfile:
		instructions = [int(x) for x in inputfile.read().splitlines()]

		while cur_pos >= 0 and cur_pos < len(instructions):
			steps += 1
			instruction = instructions[cur_pos]
			instructions[cur_pos] += 1 if (instructions[cur_pos] < 3 or part == 1) else -1		
			cur_pos += instruction	

		return steps

print("part 1", solve(1))
print("part 2", solve(2))