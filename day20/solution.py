#!/usr/bin/python3

# http://adventofcode.com/2017/day/20

import re

def get_particles():
	with open("input", "r") as inputfile:
		lines = inputfile.read().splitlines()
			
		particles = []

		for line in lines:
			# example line: p=<-4897,3080,2133>, v=<-58,-15,-78>, a=<17,-7,0>
			matches = re.search("p\=<(\-?[0-9]+),(\-?[0-9]+),(\-?[0-9]+)\>, v\=<(\-?[0-9]+),(\-?[0-9]+),(\-?[0-9]+)\>, a\=<(\-?[0-9]+),(\-?[0-9]+),(\-?[0-9]+)\>", line)
			point = {"x" : int(matches.group(1)), "y" : int(matches.group(2)), "z" : int(matches.group(3))}
			speed = {"x" : int(matches.group(4)), "y" : int(matches.group(5)), "z" : int(matches.group(6))}
			accel = {"x" : int(matches.group(7)), "y" : int(matches.group(8)), "z" : int(matches.group(9))}
			particles.append({"position" : point, "speed" : speed, "acceleration" : accel})

		return particles

def part1(iterations=250):
	particles = get_particles()		

	particleindex = None

	for _ in range(iterations):
		for i, particle in enumerate(particles):
				manhattandist1 = sum(map(abs, particle["speed"].values()))

				particle["speed"]["x"] 	  += particle["acceleration"]["x"]
				particle["speed"]["y"] 	  += particle["acceleration"]["y"]
				particle["speed"]["z"] 	  += particle["acceleration"]["z"]
				particle["position"]["x"] += particle["speed"]["x"]
				particle["position"]["y"] += particle["speed"]["y"]
				particle["position"]["z"] += particle["speed"]["z"]

				manhattandist2 = sum(map(abs, particle["speed"].values()))

				if(manhattandist2 < manhattandist1):
					particleindex = i

	return particleindex
		
		

def part2(iterations=250):
	particles = get_particles()

	particleindex = None

	for _ in range(iterations):
		for i, particle in enumerate(particles):
			collisions = [k for k in range(len(particles)) if particle["position"] == particles[k]["position"] and k != i]				
			if len(collisions) > 0:
				collisions.append(i)
				particles = [particles[k] for k in range(len(particles)) if k not in collisions]
				break

			particle["speed"]["x"] 	  += particle["acceleration"]["x"]
			particle["speed"]["y"] 	  += particle["acceleration"]["y"]
			particle["speed"]["z"] 	  += particle["acceleration"]["z"]
			particle["position"]["x"] += particle["speed"]["x"]
			particle["position"]["y"] += particle["speed"]["y"]
			particle["position"]["z"] += particle["speed"]["z"]

	return len(particles)

print("part 1", part1())
print("part 2", part2())