import sys
from math import *
from field import *
from display import *
from crane import *

class Map:

	def __init__(self, rowNum, colNum, display):
		self.rowNum = rowNum
		self.colNum = colNum
		self.display = display
		self.map = [[Field(Field.STORAGE_TYPE, []) for col in xrange(colNum)] for row in xrange(rowNum)]
		
		self.map[0][0] = Field(Field.STORAGE_TYPE, [Crate(1, 3), Crate(5, 2), Crate(22, 3)])
		self.map[4][4] = Field(Field.STORAGE_TYPE, [Crate(8, 3), Crate(772, 2)])
		self.map[3][2] = Field(Field.STORAGE_TYPE, [Crate(7, 3)])
		self.map[2][3] = Field(Field.CRANE_TYPE, [Crane(1, (2, 3), 3, 1, 10, [], self)])
		self.map[3][5] = Field(Field.CRANE_TYPE, [Crane(2, (3, 5), 2, 2, 10, [], self)])
	
	
	def fieldType(self, row, col):
		return self.map[row][col].type

		
	def field(self, row, col):
		return self.map[row][col]
		
	
	def drawMap(self):
		self.display.drawMap(self)
		
		
