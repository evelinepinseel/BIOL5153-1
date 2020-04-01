# /usr/bin/env python3

import csv

# define the input file
infile = "shaver_etal.csv"

# open and parse shaver et al.
with open(infile, 'r') as shaver:
	
	# create a csv reader object
	reader = csv.reader(shaver, delimiter=",")

	for line in reader:
		# skip blank lines
		if not line:
			continue

		else:
			if(line[3] == 'Stepps'):
				print('\t'.join([line[3], line[7], line[8]]))