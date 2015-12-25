

def part_one(r):

    houses_visited = 0

	s_pos = [0,0]

	seen_houses = []
	seen_houses.append(s_pos)

	for line in r.text.splitlines():
		for move in line:
			new_loc = []
			if move == '^':
				new_loc = [s_pos[0], s_pos[1] + 1]
			elif move == 'v':
				new_loc = [s_pos[0], s_pos[1]- 1]
			elif move == '>':
				new_loc = [s_pos[0] + 1, s_pos[1]]
			elif move == '<':
				new_loc = [s_pos[0] - 1, s_pos[1]]

			s_pos = new_loc

			if new_loc not in seen_houses:
				seen_houses.append(new_loc)

	print len(list(k for k, _ in itertools.groupby(seen_houses)))


def part_two(r):

    houses_visited = 0

	s_pos = [0,0]
	r_pos = [0,0]

	s_turn = True

	seen_houses = []
	seen_houses.append(r_pos)

	for line in r.text.splitlines():
		for move in line:
			new_loc = []
			if move == '^':
				new_loc = [s_pos[0], s_pos[1] + 1] if s_turn else [r_pos[0], r_pos[1] + 1]
			elif move == 'v':
				new_loc = [s_pos[0], s_pos[1]- 1] if s_turn else [r_pos[0], r_pos[1] - 1]
			elif move == '>':
				new_loc = [s_pos[0] + 1, s_pos[1]] if s_turn else [r_pos[0] + 1, r_pos[1] ]
			elif move == '<':
				new_loc = [s_pos[0] - 1, s_pos[1]] if s_turn else [r_pos[0] - 1, r_pos[1] ]
			print'%s, %s ' % (s_pos, r_pos)

			if s_turn:
				s_pos = new_loc
			else:
				r_pos = new_loc

			if new_loc not in seen_houses:
				seen_houses.append(new_loc)

			s_turn = False if s_turn else True

	print len(list(k for k, _ in itertools.groupby(seen_houses)))
