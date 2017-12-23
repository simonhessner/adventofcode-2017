#!/usr/bin/python3

# http://adventofcode.com/2017/day/23

import collections

registers = collections.defaultdict(int)

#registers["a"] = 1

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
		cmd = commands[i]
		parts = cmd.split(" ")

		if parts[0] == "set":
			registers[parts[1]] = getreg(parts[2])
			i += 1
		elif parts[0] == "sub":
			registers[parts[1]] -= getreg(parts[2])
			i += 1
		elif parts[0] == "mul":
			registers[parts[1]] *= getreg(parts[2])
			i += 1
			n += 1
		elif parts[0] == "jnz":
			if getreg(parts[1]) != 0:
				i += getreg(parts[2])
			else:
				i += 1
		else:
			print("error")
	
	print("part 1", n)

##
## Part 2: Thanks to reddit: https://www.reddit.com/r/adventofcode/comments/7lms6p/2017_day_23_solutions/

n = 0
for i in range(106500, 123500 + 1, 17):
	for j in range(2,i):
		if i % j == 0:
			n += 1
			break

print("part 2", n)