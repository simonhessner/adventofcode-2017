#!/usr/bin/python3

# http://adventofcode.com/2017/day/4

with open("input") as inputfile:
	count1 = 0
	count2 = 0

	for line in inputfile:
		parts = line.replace("\n", "").split(" ")
		
		# occurrances1 and valid1 are used for part 1, occurrances2 and valid2 for part 2 of day 4 task

		occurrances1 = []
		occurrances2 = []	
		
		valid1 = True
		valid2 = True

		for part in parts:
			sortedpart = ''.join(sorted(part))
			
			if part not in occurrances1:
				occurrances1.append(part)
			else:				
				valid1 = False

			if sortedpart not in occurrances2:
				occurrances2.append(sortedpart)
			else:				
				valid2 = False

		if valid1:
			count1 += 1

		if valid2:
			count2 += 1

	print("part 1", count1)
	print("part 2", count2)