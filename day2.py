from operator import mul


def part_tone(r):
    for line in r.text.splitlines():
		dims = sorted([int(i) for i in line.split('x')])

		total = (reduce(mul, dims, 1) + min([dims[0]*dims[1], dims[1]*dims[2], dims[2]*dims[0]]))
		total_feet = total_feet + total

	print total_feet


def part_two(r):
    for line in r.text.splitlines():
		dims = sorted([int(i) for i in line.split('x')])

		total = (reduce(mul, dims, 1) + dims[0]+dims[0]+dims[1]+dims[1])
		total_feet = total_feet + total

	print total_feet
