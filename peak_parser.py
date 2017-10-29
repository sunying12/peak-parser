#! /usr/bin/env python3

#object will be path defined by user when this method is called:
#path = sys.argv[1]
#newfile = Bedfile(path=path)
class Bedfile(object):
	'''
	Class to read a bedfile type file.
	'''
	def __init__(self, path=None): #standard idiom when defining classes

		self.chromosomes = dict() # key=chromosome name, value=Chromosome object
		self.filepath = path
		
		list_of_chromosome_names = list()
		
		with open(path) as bedfile:
			for line in bedfile:
				line = line.rstrip()
				
				fields = line.split("\t")
				chr_name = fields[0]

				# get existing or create new chromosome				
				if chr_name in list_of_chromosome_names:
					chromosome =  self.chromosomes[chr_name]
				else:
					list_of_chromosome_names.append(chr_name)
					chromosome = Chromosome(name=chr_name)
					self.chromosomes[chr_name] = chromosome

				# create new peak from row
				new_peak = Peak() #create new object with Peak class method
				new_peak.start = int(fields[1]) #convert the string to an int
				new_peak.end = int(fields[2])
				new_peak.signal = float(fields[6])
				peak_average = str(fields[3]).split(":")
				new_peak.mean = peak_average[1]

				chromosome.peaks.append(new_peak)
			#print(chromosome.peaks)
	
	def chromosome_names(self):		
		return self.chromosomes.keys()  	
							
class Chromosome(object):
	def __init__(self,  name=None):
		self.name = name
		self.length = None	# number of base pairs
		self.peaks = list() # list of Peak objects
	
	
class Peak(object):
	def __init__(self):

		#parenthesis .start() means I'm calling a function. .start means it is a property (variable)
		#properties for holding peak information. Must be defined here as something or nothing, in this case, None.
		#avoid placeholder properties until you know what you want: it takes up memory and other things
		self.start = None
		self.end = None
		self.signal = None
		self.mean = None
		
	def width(self):
		return (self.end - self.start) #must use this variable (property) within this class because it hasn't been defined elsewhere.
	
	def intersects_with(self, other_peak):
		pass # return True or False
		
#class Gff_file():
#	def __init__(self)		
		
		
		
