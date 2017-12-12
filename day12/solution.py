#!/usr/bin/python3

# http://adventofcode.com/2017/day/12

connections = {}

# breadth-first search using a queue
def find_group(start):
	res = []
	queue = [start]
	
	while len(queue) > 0:
		node = queue.pop(0)
		
		if node not in res:
			res.append(node)
		for connected_node in connections[node]:
			if connected_node not in queue and connected_node not in res:
				queue.append(connected_node)
	
	return res

with open("input") as inputfile:
	lines = inputfile.read().splitlines()
	for line in lines:
		tokens = line.split(" <-> ")
		from_node = int(tokens[0])
		to_nodes = [int(x) for x in tokens[1].split(", ")]
		if from_node not in connections:
			connections[from_node] = []

		for to_node in to_nodes:
			connections[from_node].append(to_node)
			if to_node not in connections:
				connections[to_node] = []
			connections[to_node].append(from_node)
	
	print("part 1", len(find_group(0)))


	groups = 0
	nodes = list(connections.keys())

	# Iteratively start from the first node in the list of left nodes and
	# find group this node belongs to. Then delete all items of that group
	# This will do one iteration for every group
	while len(nodes) > 0:
		node = nodes[0]
		group = find_group(node)		
		nodes = list(set(nodes) - set(group))
		groups += 1
	print("part 2", groups)