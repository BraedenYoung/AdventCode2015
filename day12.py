import json
import re


def part_one(r):
	get_values = re.compile(r'-?[0-9]\d*')
	print sum([int(val) for val in get_values.findall(str(r.text))])


def part_two(r):
	json_value = json.loads(r.text)
	print get_sum_with_red(json_value)


def get_sum_with_red(json_value):
	if isinstance(json_value, dict):
		if any(val for val in json_value.values() if val == 'red'):
			return 0
		return sum(get_sum_with_red(v) for k, v in json_value.iteritems())
	elif isinstance(json_value, list):
		return sum(get_sum_with_red(i) for i in json_value)
	try:
		return int(json_value)
	except:
		return 0
	return 0


def test():
	json_value = json.loads('{"4": 5, "6": 7}')
	values = []
  	for key, value in json_value.items():
		if unicode(value).isnumeric():
			values.append(value)

	print sum(values)
