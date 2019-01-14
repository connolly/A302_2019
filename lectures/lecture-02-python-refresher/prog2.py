#!/usr/bin/env python

import sys

print (sys.argv)

args = sys.argv
print(float(args[1])+float(args[2]))

# Better:
# print ' '.join(sys.argv)
