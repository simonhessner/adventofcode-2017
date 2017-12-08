#!/usr/bin/python3

# http://adventofcode.com/2017/day/2

with open("input") as inputfile:
		instructions = [x.split(" ") for x in inputfile.read().splitlines()]

		registers = {}
		tempmax = 0

		def get_reg(reg):
			if reg not in registers:
				registers[reg] = 0
			return registers[reg]

		def set_reg(reg, val):
			registers[reg] = val

		for instruction in instructions:
			register = instruction[0]
			cmd 	 = instruction[1]
			val 	 = int(instruction[2])
			cond_reg = instruction[4]
			cond_op  = instruction[5]
			cond_val = int(instruction[6])

			valid = False
			if cond_op == ">" and get_reg(cond_reg) > cond_val:
				valid = True
			if cond_op == "<" and get_reg(cond_reg) < cond_val:
				valid = True
			if cond_op == ">=" and get_reg(cond_reg) >= cond_val:
				valid = True
			if cond_op == "<=" and get_reg(cond_reg) <= cond_val:
				valid = True
			if cond_op == "==" and get_reg(cond_reg) == cond_val:
				valid = True
			if cond_op == "!=" and get_reg(cond_reg) != cond_val:
				valid = True

			if valid:
				if cmd == "inc":
					set_reg(register, get_reg(register) + val)
				if cmd == "dec":
					set_reg(register, get_reg(register) - val)

			tempmax = max(tempmax, get_reg(register))


		print("part 1", max(registers.values()))
		print("part 2", tempmax)