#!/usr/bin/python3

# http://adventofcode.com/2017/day/17

steps = 343

cbuf = [0]
curpos = 0

for i in range(1,2017+1):
	curpos = (curpos+steps) % len(cbuf) + 1 # will always be >= 1 (important for part 2)
	cbuf[curpos:curpos] = [i]

print("part 1", cbuf[cbuf.index(2017)+1])


# Since every value is inserted AFTER the current position and 0 is the first element,
# we know that there will never be a value inserted before the 0. Thus, we do not need to
# apply the inserts to the buffer, we just watch for every iterations where a value at position 1 (after the 0) 
# should be inserted. The last value is the value we are looking for
# Not inserting elements to the buffer speeds up the algorithm
curpos = 0

for i in range(1,50000000+1):
	curpos = (curpos+steps) % i + 1
	if curpos == 1:
		va0 = i

print("part 2", va0)