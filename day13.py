import json
import re
from collections import defaultdict

import sys

import itertools

input_sample = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""



def part_one(r):
	preferences = defaultdict(lambda: defaultdict(int))

	for line in r.text.splitlines():
		input_list = line.strip().split(" ")
		p1, p2, gain_or_lose, happiness_val = (input_list[0], input_list[-1][:-1], input_list[2],input_list[3])
		preferences[p1][p2] = int('-'+happiness_val if gain_or_lose == 'lose' else happiness_val)

	best_seating = -100
	g_route = []
	print preferences
	for perm in itertools.permutations(preferences.keys(), len(preferences)):
		current_seating_val = []
		for ind, person in enumerate(perm):

			current_seating_val.append(preferences[perm[ind]][perm[ind+1 if ind != len(perm)-1 else 0]])
			current_seating_val.append(preferences[perm[ind+1 if ind != len(perm)-1 else 0]][perm[ind]])

			if ind == len(perm)-1:
				possible_shortest = sum(current_seating_val)
				print current_seating_val
				print possible_shortest
				best_seating = best_seating if possible_shortest < best_seating else possible_shortest

				current_seating_val = []
				break
		# print perm
	print best_seating

def part_two(r):
	preferences = defaultdict(lambda: defaultdict(int))

	for line in r.text.splitlines():
		input_list = line.strip().split(" ")
		p1, p2, gain_or_lose, happiness_val = (input_list[0], input_list[-1][:-1], input_list[2],input_list[3])
		preferences[p1][p2] = int('-'+happiness_val if gain_or_lose == 'lose' else happiness_val)
		preferences[p1]['Me'] = 0

	#Include me
	for key in preferences.keys():
		preferences['Me'][key] = 0

	best_seating = -100
	g_route = []
	print preferences
	for perm in itertools.permutations(preferences.keys(), len(preferences)):
		current_seating_val = []
		for ind, person in enumerate(perm):

			current_seating_val.append(preferences[perm[ind]][perm[ind+1 if ind != len(perm)-1 else 0]])
			current_seating_val.append(preferences[perm[ind+1 if ind != len(perm)-1 else 0]][perm[ind]])

			if ind == len(perm)-1:
				possible_shortest = sum(current_seating_val)
				print current_seating_val
				print possible_shortest
				best_seating = best_seating if possible_shortest < best_seating else possible_shortest

				current_seating_val = []
				break
		# print perm
	print best_seating


def test():
	preferences = defaultdict(lambda: defaultdict(int))

	for line in input_sample.splitlines():
		input_list = line.strip().split(" ")
		p1, p2, gain_or_lose, happiness_val = (input_list[0], input_list[-1][:-1], input_list[2],input_list[3])
		preferences[p1][p2] = int('-'+happiness_val if gain_or_lose == 'lose' else happiness_val)

	best_seating = -100
	g_route = []
	print preferences
	for perm in itertools.permutations(preferences.keys(), len(preferences)):
		current_seating_val = []
		for ind, person in enumerate(perm):

			current_seating_val.append(preferences[perm[ind]][perm[ind+1 if ind != len(perm)-1 else 0]])
			current_seating_val.append(preferences[perm[ind+1 if ind != len(perm)-1 else 0]][perm[ind]])

			if ind == len(perm)-1:
				possible_shortest = sum(current_seating_val)
				print current_seating_val
				print possible_shortest
				best_seating = best_seating if possible_shortest < best_seating else possible_shortest

				current_seating_val = []
				break
		# print perm
	print best_seating