import itertools

import sys

weapons ={
	'Dagger':       [8,     4,      0],
	'Shortsword':  	[10,    5,      0],
	'Warhammer':    [25,    6,      0],
	'Longsword':    [40,    7,      0],
	'Greataxe': 	[74,    8,      0],
}

Armor = {
	'Leather': 		[13,    0,      1],
	'Chainmail':    [31,    0,      2],
	'Splintmail':   [53,    0,      3],
	'Bandedmail':   [75,    0,      4],
	'Platemail':   	[102,   0,      5],
	'':				[0,		0,		0]
}

Rings = {
	'Damage +1':   	[25,    1,      0],
	'Damage +2': 	[50 ,   2,      0],
	'Damage +3': 	[100,   3,      0],
	'Defense +1': 	[20,    0,      1],
	'Defense +2': 	[40,    0,      2],
	'Defense +3': 	[80,	0,		3],
	'':				[0,		0,		0]
}

player = {
	'Hit Points': 100,
	'Damage': 0,
	'Armor': 0,
}
boss = {
	'Hit Points': 104,
	'Damage': 8,
	'Armor': 1,
}



def part_one(r):
	player = {
		'Hit Points': 100,
		'Damage': 0,
		'Armor': 0,
		'cost':0
	}
	boss = {
		'Hit Points': 104,
		'Damage': 8,
		'Armor': 1,
	}
	armour_comb = []

	ring_comb = []
	for ind in range(0,3):
		ring_comb.extend(itertools.combinations(Rings.keys(), ind))

	armor_comb = Armor.keys()
	armor_comb.append('')
	weapons_comb = weapons.keys()

	combinations = list(itertools.product(*list([armor_comb,weapons_comb, ring_comb])))

	current_cost = sys.maxint

	for config in combinations:

		player = {
			'Hit Points': 100,
			'Damage': 0,
			'Armor': 0,
			'cost': 0
		}
		make_player(player, config)


		if fight(player,boss):
			print player['cost']
			if player['cost'] < current_cost:
				current_cost = player['cost']

	print current_cost


def make_player(player, config):

	player['cost'] = sum([Armor[config[0]][0], weapons[config[1]][0], sum([Rings[ring][0] for ring in config[2]])])
	player['Damage'] += Armor[config[0]][1] + weapons[config[1]][1] + sum([Rings[ring][1] for ring in config[2]])
	player['Armor'] += Armor[config[0]][2] + weapons[config[1]][2] + sum([Rings[ring][2] for ring in config[2]])



def fight(player, boss):
	player_won = None
	player_dmg = player['Damage'] - boss['Armor']
	if player_dmg <= 0:
			player_dmg = 1
	boss_dmg = boss['Damage'] - player['Armor']
	if boss_dmg <= 0:
		boss_dmg = 1

	while player['Hit Points'] >= 0 and boss['Hit Points'] >= 0:
		boss['Hit Points'] = boss['Hit Points'] - player_dmg
		if boss['Hit Points'] <= 0:
			player_won = True
			break

		player['Hit Points'] = player['Hit Points'] - boss_dmg
		if player['Hit Points'] <= 0:
			player_won = False
			break

	player['Hit Points'] = 100
	boss['Hit Points'] = 104

	return player_won


def part_two(r):
	for line in r.text.splitlines():
		pass


temp_cost = 0

def test():
	#-41, 43, 73
	player = {
		'Hit Points': 100,
		'Damage': 0,
		'Armor': 0,
		'cost':0
	}
	boss = {
		'Hit Points': 104,
		'Damage': 8,
		'Armor': 1,
	}
	armour_comb = []

	ring_comb = []
	for ind in range(0,3):
		ring_comb.extend(itertools.combinations(Rings.keys(), ind))

	armor_comb = Armor.keys()
	armor_comb.append('')
	weapons_comb = weapons.keys()

	combinations = list(itertools.product(*list([armor_comb,weapons_comb, ring_comb])))

	current_cost = 0

	for config in combinations:

		player = {
			'Hit Points': 100,
			'Damage': 0,
			'Armor': 0,
			'cost': 0
		}
		make_player(player, config)


		if not fight(player,boss):
			print player['cost']
			if player['cost'] > current_cost:
				current_cost = player['cost']

	print current_cost


def make_player(player, config):

	player['cost'] = sum([Armor[config[0]][0], weapons[config[1]][0], sum([Rings[ring][0] for ring in config[2]])])
	player['Damage'] += Armor[config[0]][1] + weapons[config[1]][1] + sum([Rings[ring][1] for ring in config[2]])
	player['Armor'] += Armor[config[0]][2] + weapons[config[1]][2] + sum([Rings[ring][2] for ring in config[2]])



def fight(player, boss):
	player_won = None
	player_dmg = player['Damage'] - boss['Armor']
	if player_dmg <= 0:
			player_dmg = 1
	boss_dmg = boss['Damage'] - player['Armor']
	if boss_dmg <= 0:
		boss_dmg = 1

	while player['Hit Points'] >= 0 and boss['Hit Points'] >= 0:
		boss['Hit Points'] = boss['Hit Points'] - player_dmg
		if boss['Hit Points'] <= 0:
			player_won = True
			break

		player['Hit Points'] = player['Hit Points'] - boss_dmg
		if player['Hit Points'] <= 0:
			player_won = False
			break

	player['Hit Points'] = 100
	boss['Hit Points'] = 104

	return player_won