
def part_one():
    input_val = r.text
    print sum(map(lambda x: 1 if x == '(' else -1, input_val))


def part_two():
    input_val = r.text
    	sum([1 if i == '(' else -1 for i in input_val])
    	floor = 0
    	value = input_file.input_value.rstrip()
    	for idx, val in enumerate(value):
    		print idx
    		if floor < 0:
    			print 'floor {f}, index {ind}'.format(f=floor, ind=idx)
    			break
    		elif val == '(':
    			floor = floor + 1
    		else:
    			floor = floor - 1
    	print 'floor {f}, index {ind}'.format(f=floor, ind=idx+1)
