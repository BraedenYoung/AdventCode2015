from itertools import permutations

egg_nog = 150
container_sizes = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]
count = 0
current_min = 0


def part_one(r):
	subset_sum(container_sizes, partial=[])
	print(count)


def subset_sum(containers, partial):
	global count

	s = sum(partial)

	if s == egg_nog:
		count += 1
	if s >= egg_nog:
		return

	for i in range(len(containers)):
		n = containers[i]
		remaining = containers[i+1:]
		subset_sum(remaining, partial + [n])


def part_two(r):
	min_subset_sum(container_sizes, partial=[])
	print(count)


def min_subset_sum(containers, partial):
	global count, current_min

	s = sum(partial)
	if s == egg_nog:
		if current_min == 0 or current_min > len(partial):
			current_min = len(partial)
			count = 0
			print current_min
		if len(partial) == current_min:
			count += 1

	if s >= egg_nog:
		return

	for i in range(len(containers)):
		n = containers[i]
		remaining = containers[i+1:]
		min_subset_sum(remaining, partial + [n])


def test():
	global count
	for r in range(1,5):

		perm_list = set([tuple(sorted(perm)) for perm in permutations(container_sizes, r)])
		for perm in perm_list:
			if sum(perm) == egg_nog:
				count += 1
		if count > 0:
			break
	print r,  count
