import time
from termcolor import cprint
import requests
import sys


def main():

	from day25 import part_one, part_two, test

	day = sys.argv[1]

	exercise = sys.argv[3]

	cprint("Part %s for day %s" % (exercise, day), 'magenta')

	if exercise == '1':
		r = requests.get('http://adventofcode.com/day/%s/input' % day, cookies=dict(session=sys.argv[2]))
		start = time.time()
		part_one(r)
	elif exercise == '2':
		r = requests.get('http://adventofcode.com/day/%s/input' % day, cookies=dict(session=sys.argv[2]))
		start = time.time()
		part_two(r)
	else:
		# r = requests.get('http://adventofcode.com/day/%s/input' % day, cookies=dict(session=sys.argv[2]))
		r = None
		start = time.time()
		test(r)

	cprint("Process time: %s" % (time.time() - start), 'yellow')

if __name__ == '__main__':
	main()
