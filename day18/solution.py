#!/usr/bin/python3

# http://adventofcode.com/2017/day/18

from collections import defaultdict

regs = defaultdict(int)

def get(registers, src):
	try:
		return int(src)
	except:
		return registers[src]

with open("input") as inputfile:
	commands = [{"cmd" : x[0], "params" : x[1:]} for x in (x.split(" ") for x in inputfile.read().splitlines())]
	
	pos = 0
	last = 0

	while pos >= 0 and pos < len(commands):
		cmd = commands[pos]["cmd"]
		params = commands[pos]["params"]
		
		if cmd == "snd":
			last = get(regs, params[0])
		if cmd == "set":
			regs[params[0]]  = get(regs, params[1])			
		if cmd == "add":
			regs[params[0]] += get(regs, params[1])
		if cmd == "mul":
			regs[params[0]] *= get(regs, params[1])
		if cmd == "mod":
			regs[params[0]] %= get(regs, params[1])
		if cmd == "rcv":
			if get(regs, params[0]) != 0:
				print("part 1", last)
				break
		if cmd == "jgz":
			if regs[params[0]] > 0:
				pos += get(regs, params[1])
			else:
				pos += 1
		else:
			pos += 1

########### part 2

registersA = defaultdict(int)
registersA["p"] = 0

registersB = defaultdict(int)
registersB["p"] = 1

posA = 0
posB = 0

waitingA = []
waitingB = []

inA = []
inB = []
n = 0


def execute(registers, who, pos):
	global waitingA, waitingB
	global inA, inB
	global n

	cmd = commands[pos]["cmd"]
	params = commands[pos]["params"]
	
	if cmd == "snd":
		if who == "A":				
			inB.append(get(registers, params[0]))
		else:			
			n += 1
			inA.append(get(registers, params[0]))
	if cmd == "set":
		registers[params[0]]  = get(registers, params[1])			
	if cmd == "add":
		registers[params[0]] += get(registers, params[1])
	if cmd == "mul":
		registers[params[0]] *= get(registers, params[1])
	if cmd == "mod":
		registers[params[0]] %= get(registers, params[1])
	if cmd == "rcv":
		if who == "A":
			if len(inA) > 0:
				registers[params[0]] = inA.pop(0)
				waitingA = False
				return pos+1
			else:
				waitingA = True
				return pos
		else:			
			if len(inB) > 0:
				registers[params[0]] = inB.pop(0)
				waitingB = False
				return pos+1
			else:
				waitingB = True
				return pos
	if cmd == "jgz":
		# IMPORTANT: do not compare registers[params[0]] > 0 because
		# params[0] can also be an integer as well 
		if get(registers, params[0]) > 0:
			pos += get(registers, params[1])
		else:
			pos += 1
	else:
		pos += 1

	return pos

with open("input") as inputfile:
	commands = [{"cmd" : x[0], "params" : x[1:]} for x in (x.split(" ") for x in inputfile.read().splitlines())]

	while posA >= 0 and posA < len(commands) and posB >= 0 and posB < len(commands) and not (waitingA and waitingB):
		if posA >= 0 and posA < len(commands):
			posA = execute(registersA, "A", posA)

		if posB >= 0 and posB < len(commands):
			posB = execute(registersB, "B", posB)

	print("part 2", n)