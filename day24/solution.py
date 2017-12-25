#!/usr/bin/python3

# http://adventofcode.com/2017/day/24

def generate_paths(path, components):
	path = path or [(0,0)]
	b = path[-1][1]
	for comp in components:
		if comp[0] == b and tuple(comp) not in path and tuple(comp[::-1]) not in path:
			newpath = path + [tuple(comp)]
			yield newpath
			yield from generate_paths(newpath, components)
		elif comp[1] == b and tuple(comp[::-1]) not in path and tuple(comp) not in path:
			newpath = path + [tuple(comp[::-1])]
			yield newpath
			yield from generate_paths(newpath, components)


with open("input", "r") as inputfile:
	components = sorted([sorted([int(x[0]), int(x[1])]) for x in (x.split("/") for x in inputfile.read().splitlines())], key=lambda key : key[0])
	paths = list(generate_paths(None, components))
	print(len(paths), "paths found")

	pathscores = [sum([a+b for a,b in path]) for path in paths]

	print("part 1", max(pathscores))	
	
	maxlen = max([len(x) for x in paths])
	filtered = [path for path in paths if len(path) == maxlen]
	scores = [sum([a+b for a,b in path]) for path in filtered]
	print("part 2", max(scores))