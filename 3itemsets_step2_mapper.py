#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.strip()
	if len(line) >= 8: #if file opened has candidate 3 itemsets
		key1, key2, value= line.split('\t', 2)
		print('%s\t%s\t%s' % (key1, key2,value))
	else:
		key1, key2 = line.split('\t', 1)#if file opened has frequent 2 itemsets
		print('%s\t%s\t%s' % (key1, key2, 'T')) #value ='T' indicates that (key1,key2) is a frequent itemset
	
