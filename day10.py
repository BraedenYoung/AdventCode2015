import itertools


def part_one(r):
	sample = "1113222113"
	for ind in range(0,50):
		sample = ''.join(str(len(list(number_list))) + letter for letter, number_list in itertools.groupby(sample))
		print ind
	print len(sample)


def part_two(r):
	input = "1113222113"
	output = []

	curr_count = 1
	prev_digit = input[0]

	for x in range(0,50):
		for curr_char in input:

			if prev_digit == curr_char:
				curr_count += 1
			else:
				output.append('{}{}'.format(curr_count, prev_digit))
				curr_count = 1
			prev_digit = curr_char
		output.append('{}{}'.format(curr_count, prev_digit))
		input = ''.join(output)
		output = []

	print len(input)

def test():
	input = "1113222113"
	output = []

	curr_count = 1
	prev_digit = input[0]

	for x in range(0,50):
		for curr_char in input:

			if prev_digit == curr_char:
				curr_count += 1
			else:
				output.append('{}{}'.format(curr_count, prev_digit))
				curr_count = 1
			prev_digit = curr_char
		output.append('{}{}'.format(curr_count, prev_digit))
		input = ''.join(output)
		output = []

	print len(input)
