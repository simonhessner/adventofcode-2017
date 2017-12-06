#!/usr/bin/python3

# http://adventofcode.com/2017/day/6

with open("input") as inputfile:
	lines =  inputfile.read().splitlines()
	blocks = [int(x) for x in lines[0].split("\t")]

	seen_blocks = []
	
	n = len(blocks)
	
	while blocks not in seen_blocks:	
		# Important: Convert to list in order to force a copy instead of a reference
		seen_blocks.append(list(blocks))

		v = max(blocks)
		i = blocks.index(v)		

		# Redistribute block value
		blocks[i] = 0
		for j in range(v):			
			blocks[(i+j+1) % n] += 1


	cycles = len(seen_blocks)	
	firstcycle = seen_blocks.index(blocks)

	print("part 1", cycles)
	print("part 2", cycles-firstcycle)