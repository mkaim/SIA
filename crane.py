from Queue import Queue
from threading import Thread
from collections import deque

class Crane:
	def __init__(self, position, rangeSight, reach, height, neighbours = []):
		self.position = position
		self.rangeSight = rangeSight
		self.reach = reach
		self.height = height
		self.angle = 0
		self.hookDistance = 1
		self.hookHeight   = 7
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
		(cmd, args) = inst
		cmd(*args)

	def decomposeTask(self, task):
		res = []
		return res

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

