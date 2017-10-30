#!/usr/bin/env Python3

file = open("spforward_genes.gff", "r")

start_position = []
end_position = []
gene_ID = []
chromosome = []



for line in file:
    line= line.strip()
    line= line.split("\t")
    chromosome.append(line[0])
    start_position.append(line[3])
    end_position.append(line[4])
    #gene_ID.append(line[8])

    #print (chromosome, start_position, end_position, gene_ID)

	if start_position > 1000:
		start_modified = [int(x)-1000 for x in start_position]


final =open("SpTSS_position.gff","w")
for i in list (zip(chromosome, start_modified, start_position)):
    final_for_print = ("\t".join([str(x) for x in i]))
    

    final.write(final_for_print + "\n")

#print (start_modified)
