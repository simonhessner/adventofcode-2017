#!/usr/bin/python3

# http://adventofcode.com/2017/day/15

start_a  = 873
start_b  = 583
factor_a = 16807
factor_b = 48271

def genfunc(val,factor,mulof=1):	
	while True:
		val = (val*factor) % 2147483647
		if val % mulof == 0:
			yield val

n = 0
gena = genfunc(start_a, factor_a)
genb = genfunc(start_b, factor_b)

for i in range(40000000):
	# & 0xFFFF extracts the lower 4*4 = 16 bits without needing
	# to convert the number to a string and then slicing it
	if (next(gena) & 0xFFFF == next(genb) & 0xFFFF):
		n += 1

print("part 1", n)

n = 0
gena = genfunc(start_a, factor_a, mulof=4)
genb = genfunc(start_b, factor_b, mulof=8)

for i in range(5000000):
	if (next(gena) & 0xFFFF == next(genb) & 0xFFFF):
		n += 1

print("part 2", n)