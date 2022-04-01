#!/usr/bin/python3

import sys

for line in sys.stdin:
	line = line.strip()
	column = line.split(",")
	city = column[1]
	country = column[2]
	year_2021 = column[3]
	city1 = "".join(c for c in city if c.isalpha())
	country1 = "".join(c for c in country if c.isalpha())
	#year_2021_1 = "".join(c for c in year_2021 if c.isalpha())
	print('{0}\t{1}\t{2}'.format(country1,city1,year_2021))

	
