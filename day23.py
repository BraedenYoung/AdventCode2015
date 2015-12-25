
reg = {'a': 0, 'b': 0}

inst = {
	'hlf':lambda r: reg[r] / 2,
	'tpl':lambda r: reg[r] * 3,
	'inc':lambda r: reg[r] + 1,
	'jmp':lambda offset: offset,
	'jie':lambda r, offset: offset if reg[r] % 2 == 0 else 0,
	'jio':lambda r, offset: offset if reg[r] == 1 else 0,
}


def part_one(r):

	program = []
	for instruction in r.text.splitlines():

		cmd = str(instruction).translate(None, ',').split(' ')
		inst = cmd[:1]
		cmd = tuple(cmd[1:])

		program.append((inst[0], cmd))

	curr_inst = 0
	while curr_inst < len(program):
		curr_inst = evaluate_inst(program[curr_inst], curr_inst)
		curr_inst += 1
	print reg


def part_two(r):
	global reg
	reg['a'] = 1

	program = []
	for instruction in r.text.splitlines():

		cmd = str(instruction).translate(None, ',').split(' ')
		inst = cmd[:1]
		cmd = tuple(cmd[1:])

		program.append((inst[0], cmd))

	curr_inst = 0
	while curr_inst < len(program):
		curr_inst = evaluate_inst(program[curr_inst], curr_inst)
		curr_inst += 1
	print reg


def test(r):

	pass


def evaluate_inst(instruction, index):
	global reg

	if len(instruction[1]) == 1 and instruction[0] != 'jmp':
		register = instruction[1][0]
		reg[register] = inst[instruction[0]](*instruction[1])
	else:
		jump_to = inst[instruction[0]](*instruction[1])
		if jump_to != 0:
			index = index + int(jump_to) - 1 # minus one to counter incr
		return index

	return index
