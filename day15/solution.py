#!/usr/bin/python3

# http://adventofcode.com/2017/day/15

def genA(mulof=1):
	val = 873
	while True:
		val = (val*16807) % 2147483647
		if val % mulof == 0:
			yield val

def genB(mulof=1):
	val = 583
	while True:
		val = (val*48271) % 2147483647
		if val % mulof == 0:
			yield val

def generator_func(start, factor, divisor, mulof):
	val = (start*factor) % divisor
	while val % mulof != 0:
		val = (val*factor) % divisor
	return val

n = 0
gena = genA()
genb = genB()

for i in range(40000000):
	# & 0xFFFF extracts the lower 4*4 = 16 bits without needing
	# to convert the number to a string and then slicing it
	if (next(gena) & 0xFFFF == next(genb) & 0xFFFF):
		n += 1

print("part 1", n)

# ---------------------------------------------

n = 0
gena = genA(mulof=4)
genb = genB(mulof=8)

for i in range(5000000):
	if (next(gena) & 0xFFFF == next(genb) & 0xFFFF):
		n += 1

print("part 2", n)