from collections import defaultdict

input="""Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds."""


new_input = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

deer = defaultdict(lambda: defaultdict(int))


def part_one(r):
	for line in input.splitlines():
		i_s = line.split(" ")
		deer[i_s[0]] = {'speed': int(i_s[3]),'time': int(i_s[6]),'rest': int(i_s[-2])}

	time = 2503
	max = 0

	for d in deer.keys():
		print d
		counter = 0
		current_time = 0
		added_dist = 0

		while time >= current_time:
			if deer[d]['time'] <= (time - current_time):
				current_time += deer[d]['time']
				counter += 1
				current_time += deer[d]['rest']

			else:
				if current_time < time:
					diff = time - current_time
					added_dist = diff * deer[d]['speed']
				current_time += 1000

		dist = added_dist + (counter * deer[d]['speed'] * deer[d]['time'])
		if dist > max:
			max = dist
		print dist

	print 'max : %s' % max




def part_two(r):
	for line in input.splitlines():
		print line
		i_s = line.split(" ")
		deer[i_s[0]] = {'speed': int(i_s[3]),'time': int(i_s[6]),'rest': int(i_s[-2]), 'dist':0, 'time_trvld': 0, 'points':0, 'resting':0}

	time = 2503
	max = 0

	for time_incr in range(1, time):
		for d in deer.keys():

			if deer[d]['resting'] == 0 and deer[d]['time_trvld'] < deer[d]['time']:
				deer[d]['dist'] += deer[d]['speed']
				deer[d]['time_trvld'] += 1
			else:
				if deer[d]['resting']+1 < deer[d]['rest']:
					deer[d]['resting'] += 1
				else:
					deer[d]['resting'] = 0
				deer[d]['time_trvld'] = 0

		gets_point = [None, 0, []]# deer, dist, others
		for d in deer.keys():
			if deer[d]['dist'] > gets_point[1] and deer[d]['dist'] > 0:
				gets_point = [d, deer[d]['dist'], []]
				gets_point[-1] = []

			elif deer[d]['dist'] == gets_point[1] and deer[d]['dist'] > 0 :
				gets_point[-1].append(d)

		if gets_point[-1]:
			for d in gets_point[-1]:
				deer[d]['points'] += 1

		deer[gets_point[0]]['points'] += 1


	for d in deer.keys():
		if deer[d]['points'] > max:
			max = deer[d]['points']

	print deer
	print max

def test():
	pass