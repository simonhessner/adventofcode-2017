#!/usr/bin/python3

# Solution for task http://adventofcode.com/2017/day/1

"""
	Method that can be used for both part 1 and part 2 by specifying 1 resp. int(len(number)/2) as step parameter
"""
def calc_stepped_sum(number, step):
	# Create list of tuples that contain the pairs that should be checked
	pairs = [(int(number[idx]), int(number[(idx + step) % len(number)])) for idx in range(len(number))]

	#Filter all pairs that match and transform the list of tuples into a list of integers, e.g. [(5,5), (1,2), (3,3)] -> [5,3]
	filtered = [x[0] for x in filter(lambda x : x[0] == x[1], pairs)]
	
	#Sum up filtered integers to get final result
	return sum(filtered)

if __name__ == "__main__":
	print("Test given example values for part 1")
	for number, result in {"1122" : 3, "1111" : 4, "1234" : 0, "91212129" : 9}.items():
		hyp = calc_stepped_sum(number, 1)
		print(number, result, hyp, hyp == result)
		assert(hyp == result)

	print("\nTest given example values for part 2")
	for number, result in {"1212" : 6, "1221" : 0, "12345" : 0, "123123" : 12, "12131415" : 4}.items():
		hyp = calc_stepped_sum(number, int(len(number)/2))
		print(number, result, hyp, hyp == result)
		assert(hyp == result)

	with open("input") as inputfile:
		number = inputfile.read().replace('\n', '')
		print("\nCalculate result for part 1")		
		print(calc_stepped_sum(number, 1))
		
		print("\nCalculate result for part 2")
		print(calc_stepped_sum(number, int(len(number)/2)))	


"""
	Verbose solution for part 1
"""
def calc_sum_next_digit(number):	
	sumval = 0
	for index in range(len(number)):
		if number[index-1] == number[index]:
			sumval += int(number[index-1])
	return sumval

"""
	Verbose solution for part 2
"""
def calc_sum_halfway_round(number):
	sumval = 0	
	length = len(number)
	step = int(length/2)

	for index in range(length):		
		if number[index] == number[(index + step) % length]:
			sumval += int(number[index])
	return sumval