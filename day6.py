import numpy
import re


def part_one(r):

    lights = numpy.zeros((1000, 1000))

    find_first_num = re.compile(r'\d')

    for line in r.text.splitlines():

        cmd_sep = find_first_num.search(line).start()

        command = line[:cmd_sep].strip()

        start_cord, _ , end_cord = line[cmd_sep:].rpartition('through')
        start_cord = [int(c) for c in start_cord.split(',')]
        end_cord = [int(c) for c in end_cord.split(',')]

        if command == 'turn on':
            for x in range(start_cord[0], end_cord[0]+1):
                for y in range(start_cord[1], end_cord[1]+1):
                    lights[x,y] = 1

        elif command == 'turn off':
            for x in range(start_cord[0], end_cord[0]+1):
                for y in range(start_cord[1], end_cord[1]+1):
                    lights[x,y] = 0
        else:
            for x in range(start_cord[0], end_cord[0]+1):
                for y in range(start_cord[1], end_cord[1]+1):
                    lights[x,y] = 1 if lights[x,y] == 0 else 0

    lights_on = 0
    for light in numpy.nditer(lights):
        if light == 1:
            lights_on = lights_on + 1
    print lights_on


def part_two(r):

    lights = numpy.zeros((1000, 1000))

    find_first_num = re.compile(r'\d')

    for line in r.text.splitlines():

        cmd_sep = find_first_num.search(line).start()

        command = line[:cmd_sep].strip()

        start_cord, _ , end_cord = line[cmd_sep:].rpartition('through')
        start_cord = [int(c) for c in start_cord.split(',')]
        end_cord = [int(c) for c in end_cord.split(',')]

        if command == 'turn on':
            for x in range(start_cord[0], end_cord[0]+1):
                for y in range(start_cord[1], end_cord[1]+1):
                    lights[x,y] = lights[x,y] + 1

        elif command == 'turn off':
            for x in range(start_cord[0], end_cord[0]+1):
                for y in range(start_cord[1], end_cord[1]+1):
                    lights[x,y] = lights[x,y] - 1 if not lights[x,y] <= 0 else 0
        else:
            for x in range(start_cord[0], end_cord[0]+1):
                for y in range(start_cord[1], end_cord[1]+1):
                    lights[x,y] = lights[x,y] + 2

    brightness = 0
    for light in numpy.nditer(lights):
        brightness = brightness + light
    print brightness
