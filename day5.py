import re


def part_one(r):

    dubs_regex = re.compile(r'((\w)\2)', re.IGNORECASE)
    bad_series_regex = re.compile(r'ab|cd|pq|xy', re.IGNORECASE)
    vowel_regex = re.compile(r'([aeiou])', re.IGNORECASE)

    nice_strings = 0
    for line in r.text.splitlines():
     	if (dubs_regex.findall(line) and len(vowel_regex.findall(line))>=3 and not bad_series_regex.findall(line)):
    	   nice_strings = nice_strings + 1
    print nice_strings


def part_two(r):

    dubs_regex = re.compile(r'((\w\w).*\2)',  re.IGNORECASE)
    repeated_letter_regex = re.compile(r'((\w)\w\2)', re.IGNORECASE)

    nice_strings = 0

    for line in r.text.splitlines():
        if dubs_regex.findall(line) and repeated_letter_regex.findall(line):
            nice_strings = nice_strings + 1
    print nice_strings
