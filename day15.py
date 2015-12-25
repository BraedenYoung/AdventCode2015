from collections import defaultdict
from itertools import izip

input ="""Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1"""

sample="""
Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

ingredients = defaultdict(lambda: defaultdict(int))
max_teaspoons = 100
ingredients_list = []

def part_one(r):
	for sample in r.text.splitlines():
		pass


def part_two(r):
	for line in r.text.splitlines():
		pass

greatest = 0
def test():

	global ingredients_list

	for ingredient in input.splitlines():
		line = ingredient.translate(None, ':,').split(' ')
		for prop, value in izip(line[1::2], line[2::2]):
			ingredients[line[0]].update({prop: int(value)})
			ingredients_list.append(line[0])
		ingredients_list = list(set(ingredients_list))

	print ingredients

	best_value = remaining_teaspoons(0, 0, [], 100)

	print greatest


def remaining_teaspoons(ingredient, current_best, mass_list, remaining):
	global greatest

	if ingredient == len(ingredients_list)-1:
		mass_list.append(remaining)
		best_val = find_ingredient_value(ingredient, mass_list)

		if best_val > greatest:
			print mass_list
			greatest = best_val

		mass_list.pop()
		return best_val

	for left_over in range(0, remaining):
		mass_list.append(remaining - left_over)
		best_score = remaining_teaspoons(ingredient+1, current_best, mass_list, left_over)
		mass_list.pop()

	return greatest


def find_ingredient_value(ingredient, mass_list):
	if mass_list == [44, 56]:
		o =0

	ingredient_vals = []
	score = 1
	curr_val = {'capacity': 0, 'durability': 0, 'flavor': 0, 'texture': 0, 'calories':0}

	for ind, key in enumerate(ingredients_list):
		if mass_list[ind] == 0:
			continue
		ingredient = ingredients[key]
		for prop, value in ingredient.iteritems():
			if prop != 'calories':
				curr_val[prop] += (value * mass_list[ind])
			else:
				curr_val['calories'] += (value * mass_list[ind])

	if curr_val['calories'] != 500:
		return 0

	for key in curr_val.keys():
		print score
		if key != 'calories':
			score *= (curr_val[key] if curr_val[key] >= 0 else 0)
	return score


def eval_curr_ingredients(ind, ind2):
	total = 0
	for prop in ind.keys():
		value = ind[prop] + ind2[prop]
		if value < 0:
			value = 0
		total += value
	return total