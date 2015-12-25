count = 0
def part_one(r):

    pass


def part_two(r):

    pass


def test(r):

    input_val = """
        lx -> a
    #     123 -> x
    #     456 -> y
    #     x AND y -> d
    #     x OR y -> e
    #     x LSHIFT 2 -> f
    #     y RSHIFT 2 -> g
    #     NOT x -> h
    #     NOT y -> i
    #     f -> df
    #     NOT df -> p
    # """.strip()

    funcs = {
        'AND': lambda a,b: a & b,
        'OR': lambda a,b: a | b,
        'LSHIFT': lambda a,b: a << b,
        'RSHIFT': lambda a,b: a >> b,
        'NOT': lambda a: ~a,
    }

    state = {}

    for line in r.text.splitlines():

        value, left_operand, operator, right_operand, destination = None, None, None, None, None

        line = line.strip()

        left_side, _, destination = line.rpartition('->')

        destination = destination.strip()
        left_side = left_side.strip()

        if left_side.isdigit():
            state[destination] = int(left_side)
        elif len(left_side) <= 2:
            state[destination] = (None, left_side)

        elif left_side.startswith('NOT'):
            operator, right_operand = left_side.split(' ')
            state[destination] = ('NOT', right_operand)

        else:
            left_operand, operator, right_operand = left_side.split(' ')
            if operator == 'AND':
                state[destination] = ('AND', (left_operand, right_operand))
            if operator == 'OR':
                state[destination] = ('OR', (left_operand, right_operand))
            if operator == 'LSHIFT':
                state[destination] = ('LSHIFT', (left_operand, int(right_operand)))
            if operator == 'RSHIFT':
                state[destination] = ('RSHIFT', (left_operand, int(right_operand)))

    #{'d': ('AND', ('x', 'y')), 'g': ('RSHIFT', ('y', 2)), 'f': ('LSHIFT', ('x', 2))



    def get_state(symbol):
        if isinstance(symbol, int):
            return symbol
        elif symbol.isdigit():
            return int(symbol)

        value = state[symbol]

        if not isinstance(value, tuple):
            return value

        command, args = value
        if not command:
            # If no command, it must be a simple assignment
            result = get_state(args)
            # store result
            state[symbol] = result
            return result
        else:
            if isinstance(args, tuple):
                args = [get_state(x) for x in args]
                result = funcs[command](*args)
            else:
                args = get_state(args)
                result = funcs[command](args)
            # store result
            state[symbol] = result
        return state[symbol]

    print state
    a = 0

    a = get_state('a')

    print state
    print a
