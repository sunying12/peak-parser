#! /usr/bin/env python3

#object will be path defined by user when this method is called:
#path = sys.argv[1]
#newfile = Bedfile(path=path)
class Bedfile(object):
	'''
	Class to read a bedfile type file.
	'''
	def __init__(self, path=None): #standard idiom when defining classes

		self.dict_bedfile = dict() #always define a property in the class with "self.variable = ..."

		with open(path, "r") as bedfile:
			for line in bedfile:
				line = line.rstrip()
				fields = line.split('\t')
				#print(fields)
				new_peak = Peak() #create new object with Peak class method
				new_peak.start = int(fields[1]) #convert the string to an int
				new_peak.end = int(fields[2])
				new_peak.chromosome = fields[0] 
				if new_peak.chromosome not in self.dict_bedfile:
					self.dict_bedfile[new_peak.chromosome] = ""			
				else:
					self.dict_bedfile[new_peak.chromosome] = [new_peak.start, new_peak.end]
				# add the new Peak to the dictionary
					
				print(self.dict_bedfile)
				
class Peak(object):
	def __init__(self):

		#parenthesis .start() means I'm calling a function. .start means it is a property (variable)
		#properties for holding peak information. Must be defined here as something or nothing, in this case, None.
		#avoid placeholder properties until you know what you want: it takes up memory and other things
		self.chromosome = None
		self.start = None
		self.end = None
		
	def width(self):
		return (self.end - self.start) #must use this variable (property) within this class because it hasn't been defined elsewhere.
	
	def intersects_with(self, other_peak):
		pass # return True or False