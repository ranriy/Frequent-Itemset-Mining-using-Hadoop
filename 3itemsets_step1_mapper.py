#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	key, value = line.split('\t', 1)
	print('%s\t%s' % (key, value)) 
