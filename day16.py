from collections import defaultdict
from itertools import izip


ticker_tape = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1,
}


def part_one(r):
	aunts = defaultdict(lambda: defaultdict(int))
	for line in r.text.splitlines():
		line = str(line).translate( None, ':,').split(' ')
		for prop, value in izip(line[2::2], line[3::2]):
			aunts[line[1]].update({prop: int(value)})

	for key in aunts.keys():
		all_valid = True
		for prop in aunts[key]:
			if aunts[key][prop] != ticker_tape[prop]:
				all_valid = False
		if all_valid:
			print key


def part_two(r):
	aunts = defaultdict(lambda: defaultdict(int))
	for line in r.text.splitlines():
		line = str(line).translate( None, ':,').split(' ')
		for prop, value in izip(line[2::2], line[3::2]):
			aunts[line[1]].update({prop: int(value)})

	for key in aunts.keys():
		all_valid = True
		for prop in aunts[key]:
			if prop in ('cats', 'trees'):
				if aunts[key][prop] > ticker_tape[prop]:
					continue
				else:
					all_valid = False
			if prop in ('pomeranians', 'goldfish'):
				if aunts[key][prop] < ticker_tape[prop]:
					continue
				else:
					all_valid = False
			if aunts[key][prop] != ticker_tape[prop]:
				all_valid = False
		if all_valid:
			print key, aunts[key]


def test(r):
	pass


