from Queue import Queue
from threading import Thread
from collections import deque, namedtuple
from time import sleep, time
from message import Message

class Ship:

	def __init__(self, cranes, crates):
		self.cranes = cranes
		self.crates = crates
		self.createThread().start()

	def sendMessage(self, msg):
		for i in xrange(len(self.cranes)):
			self.cranes[i].addMessage(msg)
		
	def mainLoop(self):
		self.sendMessage(Message(self, Message.SEARCH_PACKAGE, self.crates))

	def createThread(self):
		return Thread(target=self.mainLoop, args=[])

