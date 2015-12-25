import re


dubs_regex = re.compile(r'((\w)\2)',  re.IGNORECASE)
sneaky_chars_regex = re.compile(r'[iol]',  re.IGNORECASE)

def part_one(r):
	sample = 'vzbxkghc'
	get_next(sample)


def part_two(r):
	sample = 'vzbxxzaa'
	get_next(sample)


def test():
	pass


def is_valid(sample):
	if len(set(dubs_regex.findall(sample))) < 2:
		return False
	if sneaky_chars_regex.findall(sample):
		return False
	else:
		sequence_length = 1
		for ind, c in enumerate(sample[1:]):
			if str(chr(ord(sample[ind]) + 1)) == c:
				sequence_length += 1
			else:
				sequence_length = 1
			if sequence_length >= 3:
				return True
	return False


def incr_value(value):
	value += 1
	if value in (105, 111, 108):
		value += 1
	return value


def get_next(sample):
	sample_values = [ord(char) for char in sample]
	print sample_values
	while not is_valid(sample):

		sample_values[-1] = incr_value(sample_values[-1])

		if sample_values[-1] >= 123:
			sample_values[-1] = 97
			sample_values[-2] = incr_value(sample_values[-2] + 1)
			if sample_values[-2] >= 123:
				for ind, value in reversed(list(enumerate(sample_values[:-1]))):
					if sample_values[ind] >= 123:
						sample_values[ind] = 97
						if not ind == 0:
							sample_values[ind-1] = incr_value(sample_values[ind-1])
						else:
							sample_values[ind-1] = 97

		sample = ''.join([chr(value) for value in sample_values])
	print sample


