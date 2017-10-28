#! /usr/bin/env python3

#object will be path defined by user when this method is called:
#path = sys.argv[1]
#newfile = Bedfile(path=path)
class Bedfile(object):
	'''
	Class to read a bedfile type file.
	'''
	def __init__(self, path=None): #standard idiom when defining classes
		with open(path, "r") as bedfile:
			for line in bedfile:
				line = line.rstrip()
				field = line.split('\t')
				print(field)
				
				
class Peak(object):
	def __init__(self, path=None):

		#properties for holding peak information. Must be defined here as something or nothing, in this case, None.
		#avoid placeholder properties until you know what you want: it takes up memory and other things
		self.chromosome = None
		self.start = None
		self.end = None
