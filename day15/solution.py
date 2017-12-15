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
			# & 0xFFFF extracts the lower 4*4 = 16 bits without needing
			# to convert the number to a string and then slicing it
			yield val & 0xFFFF

gena = genfunc(start_a, factor_a)
genb = genfunc(start_b, factor_b)
n = sum(next(gena) == next(genb) for _ in range(40000000))
print("part 1", n)

gena = genfunc(start_a, factor_a, mulof=4)
genb = genfunc(start_b, factor_b, mulof=8)
n = sum(next(gena) == next(genb) for _ in range(5000000))
print("part 2", n)