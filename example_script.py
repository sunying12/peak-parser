#!/usr/bin/env python

import sys

#from peak_parser import Bedfile
from peak_parser import Gff_file
from peak_parser import DE_genes

filename_gff = sys.argv[1]
filename_rnaseq = sys.argv[2]
# newfile = Bedfile(path=filename)

#chr1 = newfile.chromosomes['chr1']

#for peak in chr1.peaks:
#	print(peak.mean)
	
		
# chr_name_list = newfile.chromosomes.keys()  	
# print(chr_name_list)

##gff file parse to list geneIDs and then report if there is sig DE genes for those ids in our DE expression file.
gff_file = Gff_file(path=filename_gff)

chr1_genes = list()
chr1 = gff_file.chromosomes['Chr1'] #chr1 is now a chromosome object
for gene in chr1.genes:
	chr1_genes.append(gene.ID)
	
# print(chr1_genes, type(chr1_genes), type(chr1_genes[0])) #checks for making list of strings

de_genes = list()
DE_file = DE_genes(path=filename_rnaseq)
# print(DE_file)
for key, value in DE_file.expression_values_dict:
	if chr1_genes
print(de_genes)
for gene in de_genes.degenes:
	print(gene.ID, gene.foldchange)

# for gene in gene_name.degenes:
# 	print(gene.ID, type(gene.ID), gene.foldchange, type(gene.foldchange), gene.annotation, type(gene.annotation))
# 
# if "Tp1g17590_AT1G19770" in newfile.expression_values_dict:
# 	print(gene.cluster, gene.foldchange)
