#!/usr/bin/env python

# run script like this ./bed_tools_usr.py -M TSS_position.bed -f ./narrowPeak_files/* 


import subprocess
import sys
import argparse
import pandas as pd
import os.path

parser = argparse.ArgumentParser(description="This is a script to intersect 2 files with bedtools",
                                 usage="bed_tools_usr.py -M <file_to_append_to> -f <list_of_files>")


# Files are in a directory, all files can be bed
parser.add_argument ("-f", "--files",
                      help="list of files to process",
                      required=True,
                      nargs="+")

# This is a master file
parser.add_argument ("-M", "--master",
                      help="file to append to",
                      required=True)

# Parse through the arguements
args = parser.parse_args()

# read TSS_position.bed into a dataframe with the headers
file_master_df = pd.read_csv(args.master,sep="\t", names=["chromosome", "start", "stop", "ID"])

# open a file that will write the final output
intersect_master = open("output_intersect", "w")
# write header to intersect_master # we never actually did this
intersect_master.close()

# for loop to execute stuff on these scripts
for filepath in args.files: 
    # This will execute bash scripts.
    process = subprocess.run (["bedtools", "intersect", "-a", "TSS_position.gff", "-b", filepath, "-c"], stdout = subprocess.PIPE )

    # this is the directory that the files are located
    filename = os.path.basename(filepath) # get the base filename from the path
    # use the names of the files in the directory as an objet
    intersect_file_name = "intersect_file_{}".format(filename)
    # open file and make it a variable
    intersect_file = open(intersect_file_name, "w")
    # for each line in the output of the bash command, 
    for line in process.stdout.decode('utf-8').split("\n"):
     # write "line" to file
        intersect_file.write(line +"\n")    
    # close the file after you open it
    intersect_file.close()

    # Read the newly made file into a dataframe
    intersect_file_df = pd.read_csv(intersect_file_name, sep="\t", header=None)
    # Append the 5th column of this dataframe along with the file name as header into a "master list"
    file_master_df[intersect_file_name] = intersect_file_df.iloc[:,4].astype(int)
# Add header to this here
file_master_df.to_csv("output_intersect",header=True, index=False, sep='\t', mode ='a')  
