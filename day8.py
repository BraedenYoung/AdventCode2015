
def part_one(r):
	difference = 0

	for line in r.text.splitlines():
		difference += len(line) - len(eval(line))
	print difference


def part_two(r):
	difference = 0
	for line in r.text.splitlines():
		difference += 2 + line.count('\\') + line.count('"')
	print difference


def test():
	pass