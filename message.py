class Message:
	(SEARCH_PACKAGE, PACKAGE_DELIVERED, HAVE_SHIP_PATH) = range(0, 3)
	def __init__(self, sender, type, data):
		self.sender = sender
		self.type   = type
		self.data   = data
