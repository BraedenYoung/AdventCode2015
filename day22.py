
import random
import sys

mana = 500

spells = {
	'magic missile': {'mana': 53, 'dmg': 4},
	'drain': {'mana': 73, 'dmg':2, 'heal': 2},
	'shield': {'mana': 113, 'effect': 6, 'armor': 7},
	'poison': {'mana': 173, 'effect': 6, 'dmg': 3},
	'recharge': {'mana': 229, 'effect': 5, 'perk': 101},

}

player = {
	'hp': 50,
	'mana':500,
	'armor': 0,
	'shield':0,
	'recharge':0,
	'spent':0
}

boss = {
	'hp': 71,
	'dmg':10,
	'armor':0,
	'poisoned':0,
}

# def part_one(r):
# 	for line in r.text.splitlines():
# 		pass
#
#
# def part_two(r):
# 	for line in r.text.splitlines():
# 		pass


def test():
	#+2030,2050
	global player, boss, spells
	least_mana = sys.maxint

	spells_comb = list(spells.keys())
	spells_comb.extend(spells.keys())
	spells_comb.extend(spells.keys())


	for x in range(0,1000000):
		if fight(player, boss):
			if player['spent'] < least_mana:
				least_mana = player['spent']
		player = {
			'hp': 50,
			'mana': 500,
			'armor': 0,
			'shield': 0,
			'recharge': 0,
			'spent': 0
		}

		boss = {
			'hp': 71,
			'dmg': 10,
			'armor': 0,
			'poisoned': 0,
		}

	print least_mana


def fight(player, boss):

	player_won = None

	while player['hp'] >= 0 and boss['hp'] >= 0:
			player['hp'] = player['hp'] - 1
			if player['hp'] <= 0:
				player_won = False
				break

			evalutate(player, boss)
			if player['mana'] <= 0:
				player_won = False
				break

			spell = random.choice(spells.keys())

			while not cast_spell(player, boss, spell):
				spell = random.choice(spells.keys())

			if boss['hp'] <= 0:
				player_won = True
				break

			boss_dmg = boss['dmg'] - player['armor']
			if boss_dmg <= 0:
				boss_dmg = 1

			evalutate(player, boss)
			player['hp'] = player['hp'] - boss_dmg
			if player['hp'] <= 0:
				player_won = False
				break

	player['hp'] = 50
	boss['hp'] = 71

	return player_won


def cast_spell(player, boss, spell):

	if spell == 'magic missile':
		boss['hp'] = boss['hp'] - spells['magic missile']['dmg']
		player['mana'] = player['mana'] - spells['magic missile']['mana']
		player['spent'] += spells['magic missile']['mana']

	elif spell == 'drain':
		boss['hp'] = boss['hp'] - spells['drain']['dmg']
		player['hp'] = player['hp'] + spells['drain']['heal']
		player['mana'] = player['mana'] - spells['magic missile']['mana']
		player['spent'] += spells['drain']['mana']

	elif spell == 'shield':
		if player['shield'] > 0:
			return False
		player['armor'] =  spells['shield']['armor']
		player['shield'] = spells['shield']['effect']
		player['mana'] = player['mana'] - spells['shield']['mana']
		player['spent'] += spells['shield']['mana']

	elif spell == 'poison':
		if boss['poisoned'] > 0:
			return False
		boss['poisoned'] = spells['poison']['effect']
		player['mana'] = player['mana'] - spells['poison']['mana']
		player['spent'] += spells['poison']['mana']

	elif spell == 'recharge':
		if player['recharge'] > 0:
			return False
		player['recharge'] = spells['recharge']['effect']
		player['mana'] = player['mana'] - spells['recharge']['mana']
		player['spent'] += spells['recharge']['mana']
	return True


def evalutate(player, boss):
	if player['shield'] > 0:
		player['shield'] = player['shield'] -1
	else:
		player['armor'] = 0

	if player['recharge'] > 0:
		player['recharge'] = player['recharge'] -1
		player['mana'] = player['mana'] + spells['recharge']['perk']

	if boss['poisoned'] > 0:
		boss['hp'] = boss['hp'] - spells['poison']['dmg']
		boss['poisoned'] = boss['poisoned'] - 1


