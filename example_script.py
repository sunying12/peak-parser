#!/usr/bin/env python

import sys

#from peak_parser import Bedfile
from peak_parser import Gff_file
from peak_parser import DE_genes

filename = sys.argv[1]

#newfile = Bedfile(path=filename)

#chr1 = newfile.chromosomes['chr1']

#for peak in chr1.peaks:
#	print(peak.mean)
	
		
#chr_name_list = newfile.chromosomes.keys()  	
#print(chr_name_list)

# gff_file = Gff_file(path=filename)
# 
# chrM = gff_file.chromosomes['ChrM']
# for gene in chrM.genes:
# 	print(gene.ID, gene.tss, gene.tss_1kb_upstream)

newfile = DE_genes(path=filename)

print(type(newfile))
gene_name = newfile.expression_values_dict["Tp1g17590_AT1G19770"]

for gene in gene_name.degenes:
	print(gene.ID, type(gene.ID), gene.foldchange, type(gene.foldchange), gene.annotation, type(gene.annotation))

