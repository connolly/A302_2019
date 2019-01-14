#!/usr/bin/env python

import argparse

# Create a parser object and add the arguments that are part of the program
parser = argparse.ArgumentParser(description='Read in some entries and add them.')

parser.add_argument('a', metavar='float_1', type=float, help='a float')
parser.add_argument('b', metavar='float_2', type=float, help='another float')

# return an object with all of the arguments
args = parser.parse_args()

print (args.a + args.b)
