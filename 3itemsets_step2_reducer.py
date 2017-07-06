#!/usr/bin/env python

import sys

items3 = []
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the from mapper
	key1, key2, value = line.split('\t', 2)

	try:
		value = int(value)
		items3.append(line)   #store the three itemset until value is an integer
	except:
		for i in items3:
			a,b,c = i.split('\t', 2)
			if a==key1 and b==key2:  #if satisfied then a,b is frequent
				print('%s\t%s\t%s' % (c,a, b))
		items3 = []
		continue
