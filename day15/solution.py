#!/usr/bin/python3

# http://adventofcode.com/2017/day/15

start_a = 873
start_b = 583

factor_a = 16807
factor_b = 48271
divisor  = 2147483647

def generator_func(start, factor, divisor, mulof):
	val = (start*factor) % divisor
	while val % mulof != 0:
		val = (val*factor) % divisor
	return val

a = start_a
b = start_b
n = 0

for i in range(40000000):
	a = generator_func(a, factor_a, divisor, 1)
	b = generator_func(b, factor_b, divisor, 1)

	if ("{0:016b}".format(a)[-16:] == "{0:016b}".format(b)[-16:]):
		n += 1

print("part 1", n)

# ---------------------------------------------

a = start_a
b = start_b
n = 0

for i in range(5000000):
	a = generator_func(a, factor_a, divisor, 4)
	b = generator_func(b, factor_b, divisor, 8)

	if ("{0:016b}".format(a)[-16:] == "{0:016b}".format(b)[-16:]):
		n += 1

print("part 2", n)