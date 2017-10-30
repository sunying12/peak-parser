#1/usr/bin/env python3

class Bedfile(object):
    def__init__(self,path=None):
    with open(path,"r") as bedfile:
        for line in bedfile:
            print(line)
