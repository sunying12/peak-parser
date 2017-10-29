#!/usr/bin/env python

import sys

from peak_parser import Bedfile

filename = sys.argv[1]

newfile = Bedfile(path=filename)

#chr1 = newfile.chromosomes['chr1']

#for peak in chr1.peaks:
#	print(peak.mean)
	
		
chr_name_list = newfile.chromosomes.keys()  	
print(chr_name_list)