#!/usr/bin/python3

# http://adventofcode.com/2017/day/2

if __name__ == "__main__":
	with open("input") as inputfile:
		result1 = 0
		result2 = 0

		for line in inputfile:
			numbers = [int(x) for x in line.split("\t")]

			# Part 1
			min_nr = min(numbers)
			max_nr = max(numbers)
			result1 += max_nr - min_nr

			# Part 2
			for ia,a in enumerate(numbers):
				for ib,b in enumerate(numbers):
					if ia != ib and a % b == 0:
						result2 += int(a/b)

		print("Day 2 part 1: %d" % result1)
		print("Day 2 part 2: %d" % result2)