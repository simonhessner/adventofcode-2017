#!/usr/bin/python3

# http://adventofcode.com/2017/day/14

# ----------------
# FROM DAY 10 START
# ----------------

def hash_round(string, numbers, pos=0, skip_size=0):		
	n = len(numbers)

	lengths = [int(x) for x in string.split(",")]	
	for length in lengths:
		if pos + length < n:
			numbers[pos:pos+length] = numbers[pos:pos+length][::-1]
		else: 
			endpos  = (pos + length) % n 
			reverse = (numbers[pos:] + numbers[:endpos])[::-1]
			sufflen = len(numbers[pos:])			
			numbers = reverse[sufflen:] + numbers[endpos:pos] + reverse[:sufflen]			

		pos = (pos + length + skip_size) % n
		skip_size += 1

	return (numbers[0] * numbers[1], pos, skip_size, numbers)

assert(hash_round("3,4,1,5", list(range(5)))[0] == 12)

def hash(string):
	suffix_values = "17,31,73,47,23"
	ascii_values = ""

	pos = skip_size = 0
	for c in string:		
		ascii_values += str(ord(c)) + ","
	ascii_values += suffix_values
	
	# Important!
	# Reuse the numbers array in each round! It cost me much time
	# because this isn't really stated in the task description and
	# I first used a new numbers array in each round... (makes no sense, I know)
	numbers = list(range(256))

	for i in range(64):		
		_, pos, skip_size, numbers = hash_round(ascii_values, numbers, pos, skip_size)
	
	hsh = ""
	for i in range(16):
		d = numbers[i*16]
		for j in range(1, 16):
			d ^= numbers[i*16+j]
		hsh += "%0.2x" % d

		
	return hsh

# ----------------
# FROM DAY 10 END
# ----------------

# ------------------------------------------------------------------


inputstr = "xlqgujun"

grid = []
used = 0

for i in range(128):
	h = hash(inputstr+"-"+str(i))
	row = [int(x) for x in '{:0128b}'.format(int(h, 16))] #1 = #, 0 = .
	used += sum(row)
	grid.append(row)

print("part 1:", used)

regions = 0
seen = []

def search(r, c):
	if (r,c) in seen:
		return

	if grid[r][c]:		
		seen.append((r,c))
		if r > 0:
			search(r-1, c)
		if r < 127:
			search(r+1, c)
		if c > 0:
			search(r, c-1)
		if c < 127:
			search(r, c+1)

for row in range(128):
	for column in range(128):
		if grid[row][column] and not (row, column) in seen:
			regions += 1
			search(row,column)

print("part 2:", regions)