import sys
from math import radians, sin, cos, sqrt
import pygame
from pygame.locals import *
from field import *


class Display:

	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)

	
	def __init__(self, width, height, fieldSize, fontSize):
		self.width = width  # in pixels
		self.height = height  # in pixels
		self.fieldSize = fieldSize  # in pixels
		
		pygame.init()
		self.clock = pygame.time.Clock()
		
		self.windowSurface = pygame.display.set_mode((self.width, self.height), 0, 32)
		pygame.display.set_caption("Agents in the Harbour")
		
		self.fontSize = fontSize
		self.basicFont = pygame.font.SysFont(None, self.fontSize)
		
		self.windowSurface.fill(Display.WHITE)
	
	
	def crateIdToString(self, x):
		if x < 10:
			return "00" + str(x)
		if x < 100:
			return "0" + str(x)
		else:
			return str(x)
	
	
	def drawStuff(self, map):
		cranesList = []
		for row in xrange(map.rowNum):
			for col in xrange(map.colNum):
				rect = pygame.draw.rect(self.windowSurface, Display.BLACK, (10 + col * self.fieldSize, 10 + row * self.fieldSize, self.fieldSize, self.fieldSize), 1)
				
				if map.fieldType(row, col) == Field.CRANE_TYPE:
					crane = map.field(row, col).getCrane()
					craneRect = pygame.draw.circle(self.windowSurface, (100, 100, 100), (rect.centerx, rect.centery), self.fieldSize / 2, 0)
					cranesList.append((crane, craneRect))
					
					craneIdText = self.basicFont.render(str(crane.id), True, Display.WHITE, (100, 100, 100))
					craneIdTextRect = craneIdText.get_rect()
					craneIdTextRect.centerx = craneRect.centerx - self.fieldSize / 4
					craneIdTextRect.centery = craneRect.centery - self.fieldSize / 4
					self.windowSurface.blit(craneIdText, craneIdTextRect)
					
					if crane.crate == None:
						heldCrateId = "---"
					else:
						heldCrateId = self.crateIdToString(crane.crate.id)
					craneHeldCrateId = self.basicFont.render(heldCrateId, True, Display.WHITE, (100, 100, 100))
					craneHeldCrateIdRect = craneHeldCrateId.get_rect()
					craneHeldCrateIdRect.centerx = craneRect.centerx
					craneHeldCrateIdRect.centery = craneRect.centery + self.fieldSize / 4
					self.windowSurface.blit(craneHeldCrateId, craneHeldCrateIdRect)
					continue
				
				if map.field(row, col).countCrates() == 0:
					continue
				ids = map.field(row, col).getAllCratesIds()
				for i in xrange(len(ids)):
					pygame.draw.rect(self.windowSurface, Display.BLACK, (rect.centerx - ((self.fontSize / 2) * 3 + 8) / 2, rect.bottom - (self.fontSize + 1) - (self.fieldSize / 4) * i, (self.fontSize / 2) * 3 + 10, self.fontSize + 2), 1)
					crateId = self.basicFont.render(self.crateIdToString(ids[i]), True, Display.BLACK, Display.WHITE)
					crateIdRect = crateId.get_rect()
					crateIdRect.centerx = rect.centerx
					crateIdRect.centery = rect.bottom - (self.fieldSize / 4) * i - self.fontSize / 2
					self.windowSurface.blit(crateId, crateIdRect)

		for i in xrange(len(cranesList)):
			(crane, craneRect) = (cranesList[i][0], cranesList[i][1])
			armLen = sqrt(2) * crane.reach * self.fieldSize
			pygame.draw.line(self.windowSurface, Display.BLACK, (craneRect.centerx, craneRect.centery), (craneRect.centerx + cos(crane.angle) * armLen, craneRect.centery + sin(crane.angle) * armLen), 3)


					
	def drawMap(self, map):
		self.clock.tick(30)
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
		self.windowSurface.fill(Display.WHITE)
			
		self.drawStuff(map)
				
		pygame.display.update()
		
