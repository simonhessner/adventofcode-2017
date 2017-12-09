#!/usr/bin/python3

# http://adventofcode.com/2017/day/9

import sys

def calc(string):
	tokens = string
	opened_groups = 0
	is_garbage = False
	groups = 0
	score = 0

	i = 0
	gc = 0

	while i < len(tokens):
		c = tokens[i]
		i += 1

		if c == "!":
			i += 1	# skip next character
		elif is_garbage and c != ">":
			gc += 1 # count characters within garbage <*>
		elif c == "<":
			is_garbage = True
		elif c == ">":
			is_garbage = False
		elif c == "{":
			opened_groups += 1
			groups += 1
			score += opened_groups
		elif c == "}":
			opened_groups -= 1


	return (groups, score, gc)

# test group counting
assert(calc("{}")[0] == 1)
assert(calc("{{{}}}")[0] == 3)
assert(calc("{{},{}}")[0] == 3)
assert(calc("{{{},{},{{}}}}")[0] == 6)
assert(calc("{<{},{},{{}}>}")[0] == 1)
assert(calc("{<a>,<a>,<a>,<a>}")[0] == 1)
assert(calc("{{<a>},{<a>},{<a>},{<a>}}")[0] == 5)
assert(calc("{{<!>},{<!>},{<!>},{<a>}}")[0] == 2)

# test scores
assert(calc("{}")[1] == 1)
assert(calc("{{{}}}")[1] == 6)
assert(calc("{{},{}}")[1] == 5)
assert(calc("{{{},{},{{}}}}")[1] == 16)
assert(calc("{<a>,<a>,<a>,<a>}")[1] == 1)
assert(calc("{{<ab>},{<ab>},{<ab>},{<ab>}}")[1] == 9)
assert(calc("{{<!!>},{<!!>},{<!!>},{<!!>}}")[1] == 9)
assert(calc("{{<a!>},{<a!>},{<a!>},{<ab>}}")[1] == 3)

# test garbage (incl. counting)
gcs = [0, 17, 3, 2, 0, 0, 10]
for i,s in enumerate(["<>", "<random characters>", "<<<<>", "<{!>}>", "<!!>", "<!!!>>", "<{o\"i!a,<{i<a>"]):
	print(s, calc(s))
	assert(calc(s) == (0,0, gcs[i]))
		
with open(sys.argv[1]) as inputfile:
	tokens = inputfile.read().splitlines()[0]
	groups, score, gc = calc(tokens)

	print("part 1:")
	print("groups: ", groups)
	print("score", score)

	print()
	print("part 2:")
	print("garbage count:", gc)