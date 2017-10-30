#!/usr/bin/env python3

#with open("output_intersect") as input:
#    print zip(*(line.strip().split('\t') for line in input))                 

with open("output_intersect", "r") as f:
    lol= [x.strip().split("\t") for x in f]

    stuff=lol[4:]
    print(stuff)
