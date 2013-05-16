from Queue import Queue
from threading import Thread
from collections import deque
from math import sqrt, atan2, cos, sin
from time import sleep

class Crane:
	(MOVE_ARM, HOOK_UP, HOOK_DOWN, GRAB, DROP) = range(0, 5)
	(TAKE_OFF, PASS_ON) = range(0+10, 2+10)

	def __init__(self, id, position, rangeSight, reach, height, neighbours = []):
		self.id = id
		self.position = position
		self.rangeSight = rangeSight
		self.reach = reach
		self.height = height
		self.angle = 0
		self.hookDistance = 1
		self.hookHeight   = height
		self.neighbours   = neighbours

		self.messages = Queue()
		self.tasks = deque()
		self.instructions = deque()

	def moveArm(self, alfa, dist):
		pass
	
	def hookDown(self, dist):
		pass

	def hookUp(self, dist):
		pass

	def grab(self):
		pass
	
	def drop(self):
		pass

	def moveContainer(self, pos1, pos2):
		def calcAngleAndShift(pos, armAngle):
			(dx, dy) = (pos[0] - self.position[0], pos[1] - self.position[1])
			rotate = ((atan2(dy,dx) - armAngle + pi) % (2*pi)) - pi
			hookShift = sqrt(dy*dy + dx*dx) - self.hookDistance
			return (rotate, hookShift)

		(rotate1, shift1) = calcAngleAndShift(pos1, self.angle)
		(rotate2, shift2) = calcAngleAndShift(pos2, self.angle+rotate1)
		stack1Size = 1
		stack2Size = 0

		return [
			(HOOK_UP, [height - self.hookHeight]),
			(MOVE_ARM, [rotate1, shift1]), 
			(HOOK_DOWN, [height - stack1Size]),
			(GRAB, []),
			(HOOK_UP, [height - self.hookHeight]),
			(MOVE_ARM, [rotate2, shift2]), 
			(HOOK_DOWN, [height - stack2Size]),
			(DROP, [])
		]

	def takeOff(self, pos):
		def findFreePosition():
			pass
		free = findFreePosition()
		return self.moveContainer(pos, free)

	def passOn(self, pos, craneId):
		def getCommonField(craneID):
			pass
		common = getCommonField(craneId)
		return self.moveContainer(pos, common)

	def sendMessage(self, msg):
		self.messages.put(msg)

	def addNeighbour(self, n):
		self.neighbours.append(n)

	def examineSurroundings(self):
		pass

	def readMessage(self, msg):
		pass

	def readMessages(self, left=5):
		while (left > 0 and self.messages):
			self.readMessage(self.messages.get())
			left -= 1

	def doInst(self, inst):
		cmd = {
			MOVE_ARM:  self.moveArm,
			HOOK_UP:   self.hookUp,
			HOOK_DOWN: self.hookDown,
			GRAB:      self.grab,
			DROP:      self.drop
		}.get(inst[0])
		cmd(*inst[1])
	
	def decomposeTask(self, task):
		dec = {
			TAKE_OFF: self.takeOff,
			PASS_ON:  self.passOn
		}.get(task[0])
		return dec(*task[1])

	def doWork(self):
		if not(self.instructions):
			if not(self.tasks):
				self.instructions.append(self.decomposeTask())
			else:
				self.instructions.append(self.decomposeTask(self.tasks.popleft()))
		self.doInst(self.instructions.popleft())
	
	def mainLoop(self):
		while True:
			self.examineSurroundings()
			self.readMessages()
			self.doWork()

	def createThread(self):
		return Thread(target=self.mainLoop, args=[])

