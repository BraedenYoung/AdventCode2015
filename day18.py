

board = []


def part_one(r):
	for ind, line in enumerate(r.text.splitlines()):
		if ind == 0:
			board.append([0,]*(len(line)+2))
		new_line = [0,]
		new_line.extend([(1 if c == '#' else 0) for c in line])
		new_line.extend([0,])
		board.append(new_line)

	board.append([0,]*(len(line)+2))

	for step in range(0, 100):

		current_count = compute_neigbours(board)

		for xind, x in enumerate(current_count):
			for yind, y in enumerate(x):
				if board[xind][yind] == 1:
					if y == 2 or y == 3:
						board[xind][yind] = 1
					else:
						board[xind][yind] = 0
				else:
					if y == 3:
						board[xind][yind] = 1
					else:
						board[xind][yind] = 0

	print sum([sum(x) for x in board])


def part_two(r):
	for ind, line in enumerate(r.text.splitlines()):
		if ind == 0:
			board.append([0,]*(len(line)+2))
		new_line = [0,]
		new_line.extend([(1 if c == '#' else 0) for c in line])
		new_line.extend([0,])
		board.append(new_line)

	board.append([0,]*(len(line)+2))

	for step in range(0, 100):

		current_count = compute_neigbours_corners_on(board)

		for xind, x in enumerate(current_count):
			for yind, y in enumerate(x):
				if board[xind][yind] == 1:
					if y == 2 or y == 3:
						board[xind][yind] = 1
					else:
						board[xind][yind] = 0
				else:
					if y == 3:
						board[xind][yind] = 1
					else:
						board[xind][yind] = 0

				board[1][1] = 1
				board[len(board)-2][1] = 1
				board[1][len(board)-2] = 1
				board[len(board)-2][len(board)-2] = 1

	print sum([sum(x) for x in board])


def test():
	pass


def compute_neigbours(board):

    shape = len(board), len(board[0])
    N = [[0,]*(shape[0]) for i in range(shape[1])]

    for x in range(1,shape[0]-1):
        for y in range(1,shape[1]-1):

			if x > 0:
				N[x][y] += board[x-1][y] + board[x-1][y-1] + board[x+1][y] + board[x+1][y+1] + board[x][y-1] + board[x+1][y-1] + board[x][y+1] + board[x-1][y+1]

    return N


def compute_neigbours_corners_on(board):

	board[1][1] = 1
	board[len(board)-2][1] = 1
	board[1][len(board)-2] = 1
	board[len(board)-2][len(board)-2] = 1

	for item in board:
		print item[0], ', '.join(map(str, item[1:]))

	print ''

	shape = len(board), len(board[0])
	N = [[0,]*(shape[0]) for i in range(shape[1])]

	for x in range(1,shape[0]-1):
		for y in range(1,shape[1]-1):

			if x > 0:
				N[x][y] += board[x-1][y] + board[x-1][y-1] + board[x+1][y] + board[x+1][y+1] + board[x][y-1] + board[x+1][y-1] + board[x][y+1] + board[x-1][y+1]

	return N

