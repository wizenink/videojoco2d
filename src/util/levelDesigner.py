import pygame
import csv 
import sys,os

dirname = os.path.dirname(__file__)
UTIL_FOLDER = os.path.join(dirname,"../util")
class Designer:

	def __init__(self,filename):
		self.filename = os.path.join(UTIL_FOLDER,filename)

	def writeFile(self,item,position):
		f = open(self.filename,'a')
		f.write(item+" "+str(position[0])+" "+str(position[1])+"\n")
		f.close()
		
	def readFile(self):
		result = []
		with open(self.filename,'r') as f:
			reader = csv.reader(f,delimiter=' ')
			for row in reader:
				if row[0] == "#":
					continue
				item = row[0]
				position = (float(row[1]),float(row[2]))
				result.append((item,position))
		
		return result


