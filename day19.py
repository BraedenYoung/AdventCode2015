import itertools

import sys

sample_trans = """e => H
e => O
H => HO
H => OH
O => HH"""


base_molecule = "HOHOHO"


actual_trans = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg"""


actual_base = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"


def part_one(r):

	commands = []
	for line in actual_trans.splitlines():
		commands.append(line.split(' => '))

	distinct_str = []

	for command in commands:
		for occurence in find(actual_base, command[0]):
			temp = list(actual_base)
			if len(command[0]) == 1:
				temp[occurence] = command[1]
			elif len(command[0]) == 2:
				temp[occurence+1] = ''
				temp[occurence] = command[1]

			distinct_str.append(''.join(temp))

	print len(set(distinct_str))


def find(s, ch):
	if len(ch) == 1:
		return [i for i, ltr in enumerate(s) if ltr == ch]
	else:
		indexes = []
		for i, ltr in enumerate(s):
			if ltr+s[i+1] == ch:
				indexes.append(i)
			if i == len(s)-2:
				return indexes


def part_two(r):
	import re

	molecule = actual_base[::-1]

	reps = {line[1][::-1]: line[0][::-1] for line in [line.split(' => ') for line in actual_trans.splitlines()]}

	print reps

	def rep(x):
		return reps[x.group()]

	count = 0
	while molecule != 'e':
		molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
		count += 1

	print(count)


input = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"""


def test():
	commands = []
	for line in actual_trans.splitlines():
		commands.append(line.split(' => '))

	print commands

	for command in commands:
		if command[0] == 'e':
			get_molecule(command[1], commands, 1)

	print min_steps


def get_molecule(curr_molecule, commands, steps=sys.maxint):
	global min_steps

	curr_molecule = ''.join(curr_molecule)

	if len(curr_molecule) > len(actual_base):
		return

	if curr_molecule == actual_base:
		if min_steps > steps:
			min_steps = steps

	for command in commands:
		for occurence in find(curr_molecule, command[0]):
			temp = list(curr_molecule)
			if len(command[0]) == 1:
				temp[occurence] = command[1]

			elif len(command[0]) == 2:
				temp[occurence+1] = ''
				temp[occurence] = command[1]

			get_molecule(temp, commands, steps+1)


def find(s, ch):
	if len(ch) == 1:
		return [i for i, ltr in enumerate(s) if ltr == ch]
	else:
		indexes = []
		for i, ltr in enumerate(s):
			if ltr+s[i+1] == ch:
				indexes.append(i)
			if i == len(s)-2:
				return indexes