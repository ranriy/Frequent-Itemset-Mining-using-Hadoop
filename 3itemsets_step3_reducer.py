#!/usr/bin/env python

import sys

item1 = -1
item2 = -1
item3 = -1
current_count = 0

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
        # parse the input we got from mapper.py
	key1, key2, key3, count = line.split('\t', 3)
	key1= int(key1)
	key2= int(key2)
	key3= int(key3)
	# convert count (currently a string) to int
	try:
		count = int(count)
		
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	if (item1 == key1) and (item2 == key2) and (item3 == key3):
		current_count += count
	else:
		if item1!=-1 and item2!=-1 and item3!=-1 and current_count>=1000:
			print('%s\t%s\t%s' % (item1, item2, item3))
		current_count = count
		item1 = int(key1)
		item2 = int(key2)
		item3 = int(key3)

#last word
if item1 == key1 and item2 == key2 and item3 == key3 and current_count>=1000:
	print('%s\t%s\t%s' % (item1, item2, item3))
