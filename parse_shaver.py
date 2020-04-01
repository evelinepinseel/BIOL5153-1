# /usr/bin/env python3

import csv

# define the input file
infile = "shaver_etal.csv"


#open the output file
with open("shaver_tabbed.txt", 'w') as output:

	# open and parse shaver et al.
	with open(infile, 'r') as shaver:
		
		# create a csv reader object
		reader = csv.reader(shaver, delimiter=",")

		for line in reader:
			# skip blank lines
			if not line:
				continue

			else:
				linewriter = csv.writer(output, delimiter='\t', quotechar='"')
				linewriter.writerow(line)
	