#!/usr/bin/env python

import sys

from peak_parser import Bedfile
from peak_parser import Gff_file

filename = sys.argv[1]

#newfile = Bedfile(path=filename)

#chr1 = newfile.chromosomes['chr1']

#for peak in chr1.peaks:
#	print(peak.mean)
	
		
#chr_name_list = newfile.chromosomes.keys()  	
#print(chr_name_list)

gff_file = Gff_file(path=filename)

chr1 = gff_file.chromosomes['Chr1']
for gene in chr1.genes:
	print(gene.ID)