import itertools
from functools import reduce
from operator import mul


packages = [1, 2, 3, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]


def part_one(r):
	group_weight = sum(packages) / 3
	for curr_length in range(len(packages)):
		combs = get_combinations(curr_length, group_weight)
		if combs:
			print min([reduce(mul, comb)for comb in combs])
			break


def part_two(r):
	group_weight = sum(packages) / 4
	for curr_length in range(len(packages)):
		combs = get_combinations(curr_length, group_weight)
		if combs:
			print min([reduce(mul, comb)for comb in combs])
			break


def get_combinations(length, group_weight):
	return [comb for comb in itertools.combinations(packages, length) if sum(comb) == group_weight]


def test():
	pass