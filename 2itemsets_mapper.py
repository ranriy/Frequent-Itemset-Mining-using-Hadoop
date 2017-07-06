#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into digits
	words = re.findall(r'\d+', line)
	
	lst =[]        
	for i in words:
		lst.append(i)    #lst contains items in each transaction
	for item1 in words:
		for item2 in lst:
			if item1!=item2 and lst:  
				print('%s\t%s\t%s' % (item1, item2, 1))  #outputs frequent 2itemsets with value 1 and key=item1, item2
		lst.pop(0)
      
