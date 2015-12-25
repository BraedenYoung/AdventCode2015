import itertools
from collections import defaultdict

import sys


def part_one(r):

	distances = defaultdict(lambda: defaultdict(int))

	for line in r.text.splitlines():
		l, r = line.strip().split(" = ")
		c1, c2 = l.split(" to ")
		distances[c1][c2] = int(r)
		distances[c2][c1] = int(r)

	shortest = sys.maxint
	g_route = []

	for perm in itertools.permutations(distances.keys(), len(distances)):
		print perm
		curr_trip = []
		for ind in range(0, len(perm)):
			if ind == len(perm)-1:
				total = sum(curr_trip)
				if total < shortest:
					shortest = total
					g_route = list(perm)



				break
			curr_trip.append(distances[perm[ind]][perm[ind+1]])

	print shortest
	print g_route


		# perm = list(perm)
		# leg1 = distances[perm[0]][perm[1]]
		# print sum(distances[perm[0]][perm[1]] )


	# list_o_places = []
	# for departure, destinations in distances.iteritems():
	# 	for destination in destinations.iteritems():
	# 		list_o_places.append(destination)
	#


	# print list_o_places
	# d = itertools.permutations(list_o_places)
	#
	# trips = []
	# for location, distances in d.iteritems():
	# 	trips.append(sum(distances))
	#
	# print min(trips)

	# print(list_o_places)

	# distances = [int(s) for s in input.split() if s.isdigit()]
	# perms = itertools.permutations(distances, len(distances)-1)
	# print min([sum(route) for route in perms])




# def part_one(r):
# 	# w 333, 2664
#
# 	place_index = {}
# 	distance_matrix = [[0 for x in range(8)] for x in range(8)] #8
#
# 	for line in r.text.splitlines():
# 		if len(line) <=0:
# 			continue
#
# 		l, r = line.strip().split(" = ")
#
# 		c1, c2 = l.split(" to ")
#
# 		if c1 not in place_index:
# 			place_index[c1] = len(place_index)
# 		if c2 not in place_index:
# 			place_index[c2] = len(place_index)
#
# 		distance_matrix[place_index[c1]][place_index[c2]] = int(r)
#
# 	distances = defaultdict(lambda: defaultdict(int))
# 	print place_index
#
# 	for line in distance_matrix:
# 		print line
#
# 	shortest_dist = 9999999
#
# 	x_start = 0
# 	for attempt in range(0, len(place_index)):
# 		curr_route = []
# 		curr_dist = 0
#
# 		for x in range(x_start, len(place_index)):
# 			for y in range(0, len(place_index)):
# 				if distance_matrix[x][y] == 0 or (x,y) in curr_route:
# 					continue
#
# 				curr_route.append((x,y))
# 				curr_dist += distance_matrix[x][y]
#
# 				x = y
# 				break
# 		if curr_dist < shortest_dist:
# 			shortest_dist = curr_dist
# 			print shortest_dist
#
# 		curr_dist = 0
# 		curr_route = []
#
# 		++x_start




def part_two(r):
	difference = 0
	for line in r.text.splitlines():
		difference += 2 + line.count('\\') + line.count('"')
	print difference


def test():
	input = """Belfast to Faerun = 1
	Faerun to London = 2
	London to Dublin = 4
London to Belfast = 3
Dublin to Belfast = 7
"""

	place_index = {}
	distance_matrix = [[0 for x in range(4)] for x in range(4)] #8

	for line in input.splitlines():
		if len(line) <= 0:
			continue

		l, r = line.strip().split(" = ")

		c1, c2 = l.split(" to ")

		if c1 not in place_index:
			place_index[c1] = len(place_index)
		if c2 not in place_index:
			place_index[c2] = len(place_index)

		distance_matrix[place_index[c1]][place_index[c2]] = int(r)

	distances = defaultdict(lambda: defaultdict(int))
	print place_index
	print distance_matrix

	print (sorted([i[:2], i[2:]] for i in set(itertools.permutations(itertools.chain.from_iterable(distance_matrix)))))


	# shortest_route = 999999999
	# route = []
	# curr_trip = 0
	#
	# for y in range(0, len(place_index)):
	# 	for x in range(0, len(place_index)):
	# 		if len(set(route)) == len(place_index):
	#
	# 				print route
	#
	# 				if shortest_route > curr_trip:
	# 					print curr_trip
	# 					shortest_route = curr_trip
	# 					curr_trip = 0
	# 					route = []
	#
	# 		if distance_matrix[x][y] == 0:
	# 			continue
	#
	#
	# 		route.append((x, y))
	#
	# 		# print [list(place_index.keys())[list(place_index.values()).index(x)],
	# 		# list(place_index.keys())[list(place_index.values()).index(y)]]
	#
	#
	# 		for inner_x in range(0, len(place_index)):
	# 			if inner_x in route or inner_x == 0:
	# 				# May break if we return places
	# 				continue
	# 			route.append((inner_x,y))
	#
	#
	#
	# print shortest_route
	# print route








