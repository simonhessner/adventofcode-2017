#!/usr/bin/python3

# http://adventofcode.com/2017/day/23

import collections

registers = collections.defaultdict(int)

def getreg(reg):
	try:
		return int(reg)
	except:
		return registers[reg]

with open("input") as inputfile:
	commands = inputfile.read().splitlines()

	i = 0
	n = 0

	while i >= 0 and i < len(commands):
		command = commands[i]
		cmd, dst, src = command.split(" ")

		i += 1

		if cmd == "set":
			registers[dst]  = getreg(src)
		elif cmd == "sub":
			registers[dst] -= getreg(src)
		elif cmd == "mul":
			registers[dst] *= getreg(src)
			n += 1
		elif cmd == "jnz":
			if getreg(dst) != 0:
				i += (getreg(src) - 1) # -1 because we add 1 in all cases to save LOC
		else:
			print("error")
	
	print("part 1", n)

# Part 2 was hard: 
# Thanks to reddit: https://www.reddit.com/r/adventofcode/comments/7lms6p/2017_day_23_solutions/

n = 0
for i in range(106500, 123500 + 1, 17):
	for j in range(2,i):
		if i % j == 0:
			n += 1
			break

print("part 2", n)