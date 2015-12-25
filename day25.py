import numpy as np


req_row, req_col = 3010, 3019


def part_one(r):
	max_dim = (req_row + 1) + (req_col + 1) - 1

	code_array = np.zeros((max_dim, max_dim), int)

	cur_row = 0
	cur_col = 0
	last_row = 0
	last_col = 0

	value_gen = get_next_value(20151125)

	max_length = sum(xrange(max_dim))

	for ind in range(0, max_length):

		code_array[cur_row][cur_col] = next(value_gen)

		if cur_row == 0 or cur_col == max_dim - 1:
			if last_row != max_dim - 1:
				cur_row = last_row + 1
				cur_col = 0
			else:
				cur_row = last_row
				cur_col = last_col + 1
				last_col = cur_col

			last_row = cur_row
		else:
			cur_row -= 1
			if cur_col != max_dim - 1:
				cur_col += 1

	print code_array[req_row-1][req_col-1]


def part_two(r):
	pass


def test(r):
	pass


def get_next_value(starting_val):
	previous_val = starting_val
	while True:
		yield previous_val
		previous_val = (previous_val * 252533) % 33554393



