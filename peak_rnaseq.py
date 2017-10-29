#! /usr/bin/env python3

import sys

#RNA DE gene list parser
	#script will be converted to function and maybe class-based pipeline analysis
def DE_gene_parser(rnaseq_table):
	with open(rnaseq_table, "r") as rnaseq_file:
		expression_values_dict = dict() #gene_id as key, logfold change list as values
		for line in rnaseq_file:
			line = line.rstrip()
			fields = line.split('\t')
			if fields[2] not in expression_values_dict:
				expression_values_dict[fields[2]] = fields[3:16]
	return expression_values_dict		
			
rnaseq_table = sys.argv[1]

print(DE_gene_parser(rnaseq_table))			
			