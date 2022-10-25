#!/usr/bin/env python3

def parse_puzzle_input(day_id):
    output = []
    with open('../data/day_{}_input.txt'.format(day_id)) as infile:
        for line in infile:
            output.append(line.rstrip('\n'))
    return output
