#!/usr/bin/python3

import sys,os

last_country = None
max_city = None
max_val = 0

for line in sys.stdin:
	line = line.strip()
	country, city, year_2021 = line.split('\t')
	try:	
		if last_country and last_country != country:
			print(f"{last_country}\t{max_city}\t{max_val}")
			last_country = country
			max_city = city
			max_val = float(year_2021)
		else:
			last_country = country
			if(float(year_2021) > max_val):
				max_val = float(year_2021)
				last_city = max_city

	except ValueError:
		print("Errore con la linea...")

if last_country:
	print("{0}\t{1}\t{2}".format(last_country,max_city, max_val))
