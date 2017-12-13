#!/usr/bin/python3

# http://adventofcode.com/2017/day/12

with open("input") as inputfile:
	lines = inputfile.read().splitlines()
	layers = {int(x.split(": ")[0]) : int(x.split(": ")[1]) for x in lines}
	maxdepth = max(layers.keys())

	delay  = 0
	caught = True

	while caught:
		caught = False	
		time = delay
		severity = 0
		for depth in range(maxdepth+1):
			if depth in layers:		
				lrange = layers[depth]

				rtt = 2*(lrange-1) # round trip time (up and down)

				if time%rtt == 0:
					caught = True
					#print("caught on layer", depth, time)
					if delay == 0: # part 1 only
						severity += depth*lrange
					else: # in part 2 we do not need the severity, so we can skip the rest of the layers
						break
			
			time += 1		

		if delay == 0:
			print("part 1: ", severity)
			print("Calculating part 2...")

		if not caught:
			print("part 2", delay)
		
		delay += 1