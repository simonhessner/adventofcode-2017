#!/usr/bin/python3

# http://adventofcode.com/2017/day/9

inputstr = "189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62"

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

print("part 1:", hash_round(inputstr, list(range(256)))[0])

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

print("")
print("part 2:")
print("tests:")
for s in [("1,2,3", 	"3efbe78a8d82f29979031a4aa0b16a9d"),
		  ("", 			"a2582a3a0e66e6e86e3812dcb672a272"), 
          ("AoC 2017",  "33efeb34ea91902bb2f59c9920caa6cd"),            
          ("1,2,4", 	"63960835bcdc130f0b66d7ff4f6a5a8e")]:
	print("'%s' -> %s" % (s[0], hash(s[0])))
	assert(hash(s[0]) == s[1])

print("result:")
print(hash(inputstr))