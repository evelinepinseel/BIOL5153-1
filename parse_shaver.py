# /usr/bin/env python3

# define the input file
infile = "shaver_etal.csv"

# open and parse shaver et al.
with open(infile, 'r') as shaver:
	for line in shaver:
		line = line.rstrip("\n")

		fields = line.split(",")

		if(fields[3] == 'Stepps'):
			# print(fields[3], fields[7], fields[8])
			print('\t'.join([fields[3], fields[7], fields[8]]))