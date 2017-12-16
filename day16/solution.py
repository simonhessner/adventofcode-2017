#!/usr/bin/python3

# http://adventofcode.com/2017/day/16

def run(iterations):
	programs = [chr(ord("a")+i) for i in range(16)]

	with open("input") as inputfile:
		instructions = [x.split(",") for x in inputfile.read().splitlines()][0]

		seen = []

		for i in range(iterations):
			seq = "".join(programs)
			if seq in seen:
				# As the number of iterations is too high to run in reasonable time
				# we detect cycles in the algorithm. If we generate a program order
				# that was already seen before, we know that the next iterations
				# will generate exactly the same result starting from the first
				# order in the cycle. So just calculate iterations%i to determine
				# how far to go from the first cycled program in order to get
				# the same result as with iteration one billion times
				print("cycle after %d iterations" %i)
				return "".join(seen[iterations%i])				
			seen.append(seq)

			for instruction in instructions:
				if instruction[0] == "s":
					count = int(instruction[1:])				
					programs = programs[-count:] + programs[:-count]
				elif instruction[0] == "x":
					posA,posB = map(int, instruction[1:].split("/"))
					programs[posA], programs[posB] = programs[posB], programs[posA]		
				elif instruction[0] == "p":
					progA,progB = instruction[1:].split("/")
					posA,posB = programs.index(progA),programs.index(progB)
					programs[posA], programs[posB] = programs[posB], programs[posA]					
				else:
					print("unknown instruction '%s'" % instruction)

		return "".join(programs)

print("part 1", run(1))
print("part 2", run(1000000000))