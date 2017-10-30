#! /usr/bin/env python3

from peak_parser import Bedfile
from peak_parser import Gff_file
from peak_parser import DE_genes
import argparse

parser = argparse.ArgumentParser(description="parses bedfiles.")
parser.add_argument("-f", "--files",
					help="the actual bedfile", required=True,
					nargs='+') #nargs means number of agruments = 1 or more. You can only have one parameter of one or more
parser.add_argument("-d", "--DE_genes", help="differential expression files with logfold change. Consistent format required",
					required=False)
parser.add_argument("-c","--chromosome",
					help="chromosome name", required=False) #False is default
parser.add_argument("-p", "--peaks",
					help="number of peaks in selected chromosome", required=False,
					default=1, type=int)
parser.add_argument("-x", "--expression", required=False,
					help="returns list of genes from selected chromosome with >2 Log2foldchange")
					#choices=lambda x:x if float(x) >= 1 else raise argparse.ArgumentTypeError("expression must be greater than 1"))
args=parser.parse_args()

#read in bedfile by looping through arg.files list and returning each file, so path=file
for file in args.files:
	bedfile = Bedfile(path=file)

	chr1 = bedfile.chromosomes[args.chromosome.lower]
	#print every peak object in our list of objects
	for peak in chr1.peaks[0:args.peaks]:
		print(peak)