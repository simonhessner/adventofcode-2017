#!/usr/bin/python3

# http://adventofcode.com/2017/day/7

removable = []
programs  = []
children  = {}
weights   = {}

def get_weight(node):
	weight = weights[node]
	for child in children[node]:
		weight += get_weight(child)
	return weight

def get_child_weights(node):
	return [get_weight(n) for n in children[node]]

def is_balanced(node):
	if children[node] == []:
		return True
	weights = get_child_weights(node)
	return len(set(weights)) == 1

def find_inbalanced_child(node):
	child_weights = get_child_weights(node)
	for child in children[node]:
		weight = get_weight(child)
		if child_weights.count(weight) == 1:
			return child
	return None

def calc_weight_diff(root):
	deepest_unbalanced_node = root
	# go down the hierarchy until the last unbalanced node (children have different weights) is found
	while not is_balanced(deepest_unbalanced_node):
		parent = deepest_unbalanced_node
		deepest_unbalanced_node = find_inbalanced_child(deepest_unbalanced_node)
	
	# This is a node in the unbalanced node that occurs more often than deepest_unbalanced_node
	other_node = list(set(children[parent]) - set([deepest_unbalanced_node]))[0]
	
	return weights[deepest_unbalanced_node] - get_weight(deepest_unbalanced_node) + get_weight(other_node)

with open("input") as inputfile:
	lines =  inputfile.read().splitlines()	

	for line in lines:
		blocks = [x for x in line.split(" ")]

		name = blocks[0]
		weight = int(blocks[1].replace("(", "").replace(")", ""))
		
		weights[name] = weight
		programs.append(name)

		if name not in children:
			children[name] = []

		if len(blocks) > 2:
			for child in [x.replace(",", "") for x in blocks[3:]]:
				removable.append(child)
				children[name].append(child)


	root = list(set(programs)-set(removable))[0]
	print("part 1", root)

	print("part 2", calc_weight_diff(root))