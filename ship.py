from Queue import Queue
from threading import Thread
from collections import deque, namedtuple
from time import sleep, time

(SEARCH_PACKAGE, PACKAGE_DELIVERED) = range(0, 2)

Message = namedtuple('Message', ['sender', 'type', 'data'])

class Ship:

        def __init__(self, cranes, crates):
                self.cranes = cranes
                self.crates = crates
                self.createThread().start()

        def sendMessage(self, msg):
                for i in xrange(len(self.cranes)):
                        self.cranes[i].messages.put(msg)
        
        def mainLoop(self):
                self.sendMessage(Message(self, SEARCH_PACKAGE, self.crates))

        def createThread(self):
                return Thread(target=self.mainLoop, args=[])

