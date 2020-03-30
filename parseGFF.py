#! /usr/bin/env python3

# specify the input files
gff_file   = 'watermelon.gff'
fasta_file = 'watermelon.fsa'


# open the GFF file
gff = open(gff_file, 'r')


# list for gene names
gene_names = []

# read GFF file, line by line
for line in gff:

	# remove line breaks
	line = line.rstrip('\n')
	
	# split each line on the tab character
	# sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')
	fields = line.split('\t')

	# split the attributes field (index = 8), each attribute is separated by ' ; '

	attributes = fields[8].split(' ; ')

	# we only need the first item in this list
	# print(attributes[0])
	gene_fields = attributes[0].split('Gene ')

	# print the gene name
	# print(gene_fields[1])

	# store the gene name
	gene_names.append(gene_fields[1])


	# extract the DNA sequence from the genome for this feature

	# print the DNA sequence for this feature

	# calculate the GC content for this feature, and print it to the screen

# print the genes in alphabetical order
for gene in sorted(gene_names):
	print(gene)



gff.close()


















