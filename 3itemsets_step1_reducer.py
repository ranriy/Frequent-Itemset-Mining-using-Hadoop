#!/usr/bin/env python

import sys

prevkey=-1
prevval = -1
lst1 =[]  #using lst1 and lst2 to store sets with same key
lst2 =[]
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	key, value = line.split('\t', 1)
	value = int(value)

	if prevkey == key:
		lst1.append(line)
		lst2.append(line)
	elif prevkey == -1 and prevval ==-1:
		lst1.append(line)
		lst2.append(line)
		prevkey = key
		prevval = value
	else:
		prevkey = key
		prevval = value

		for i in lst1:
			key1, value1 = i.split('\t', 1)
			value1= int(value1)
			for j in lst2:
				key2,value2 = j.split('\t', 1)
				value2 = int(value2)
				if key1 == key2 and value1<value2:
					print('%s\t%s\t%s' % (value1, value2, key1))
		lst1 =[]
		lst2 =[]
		lst1.append(line)
		lst2.append(line)
for i in lst1:
	key1, value1 = i.split('\t', 1)
	value1= int(value1)
	for j in lst2:
		key2,value2 = j.split('\t', 1)
		value2 = int(value2)
		if key1 == key2 and value1<value2:
			print('%s\t%s\t%s' % (value1, value2, key1))
