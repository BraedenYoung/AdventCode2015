from functools import reduce


def part_one(r):
	curr_house = 150000
	curr_total = 0
	while curr_total < 29000000:
		number = []
		curr_house += 1
		for x in factors(curr_house):
   			number.append(x*10)
		curr_total = sum(number)

	print curr_house


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def part_two(r):
	number = []
	curr_house = 80000
	curr_total = 0
	while curr_total < 29000000:
		number = []
		curr_house += 1
		factor = list(factors(curr_house))
		for x in factor:
			if curr_house/x > 50:
				continue
   			number.append(x*11)
		curr_total = sum(number)

	print curr_house


def test():
	# +1705884, +1740006, +1740005, 718200
	number = []
	curr_house = 80000
	curr_total = 0
	while curr_total < 29000000:
		number = []
		curr_house += 1
		factor = list(factors(curr_house))
		for x in factor:
			if curr_house/x > 50:
				continue
   			number.append(x*11)
		curr_total = sum(number)

	print curr_house


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
