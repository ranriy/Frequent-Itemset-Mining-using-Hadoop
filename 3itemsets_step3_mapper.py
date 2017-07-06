#!/usr/bin/env python

import sys
import re

lst =[]
file1 = open('candidates', 'r')
for line in file1:
	line = line.strip()
	lst.append(line) #lst stores all candidates generated after step2
for line_retail in sys.stdin:
	line_retail = line_retail.strip()
	for i in lst:
		item1, item2, item3= i.split('\t', 2)
		if (item1 in line_retail) and (item2 in line_retail) and (item3 in line_retail):
			print('%s\t%s\t%s\t%s' % (item1, item2, item3,1))		
