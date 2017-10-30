#! /usr/bin/env python3

from peak_parser import Bedfile
import argparse

parser = argparse.ArgumentParser(description="parses bedfiles.")
parser.add_argument("-f", "--files",
					help="the actual bedfile", required=True,
					nargs='+') #nargs means number of agruments = 1 or more. You can only have one parameter of one or more
parser.add_argument("-c","--chromosome",
					help="chromosome name", required=False) #False is default
parser.add_argument("-p", "--peaks",
					help="number of peaks in selected chromosome", required=False,
					default=1, type=int)
args=parser.parse_args()
#read in bedfile by looping through arg.files list and returning each file, so path=file
for file in args.files:
	bedfile = Bedfile(path=file)

	chr1 = bedfile.chromosomes[args.chromosome]
	#print every peak object in our list of objects
	for peak in chr1.peaks[0:args.peaks]:
		print(peak)