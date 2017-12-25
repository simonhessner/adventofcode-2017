#!/usr/bin/python3

# http://adventofcode.com/2017/day/25

from collections import defaultdict

band = defaultdict(int)
pos = 0
state = "A"

for i in range(12399302):
	if state == "A":
		if band[pos] == 0:
			band[pos] = 1
			pos += 1
			state = "B"
		else:
			band[pos] = 0
			pos += 1
			state = "C"

	elif state == "B":
		if band[pos] == 0:
			pos -= 1
			state = "A"
		else:
			band[pos] = 0
			pos += 1
			state = "D"

	elif state == "C":
		if band[pos] == 0:
			band[pos] = 1
			pos += 1
			state = "D"
		else:
			band[pos] = 1
			pos += 1
			state = "A"

	elif state == "D":
		if band[pos] == 0:
			band[pos] = 1
			pos -= 1
			state = "E"
		else:
			band[pos] = 0
			pos -= 1
			state = "D"

	elif state == "E":
		if band[pos] == 0:
			band[pos] = 1
			pos += 1
			state = "F"
		else:
			band[pos] = 1
			pos -= 1
			state = "B"

	elif state == "F":
		if band[pos] == 0:
			band[pos] = 1
			pos += 1
			state = "A"
		else:
			band[pos] = 1
			pos += 1
			state = "E"
	else:
		print("Invalid State '%s'" % state)

print(sum(band.values()))