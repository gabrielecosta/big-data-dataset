#!/usr/bin/python3

import sys

for line in sys.stdin:
	line = line.strip()
	column = line.split(",")
	city = column[1]
	country = column[2]
	year_2021 = column[3]
	print('{0}\t{1}\t{2}'.format(country,city,year_2021))

	
