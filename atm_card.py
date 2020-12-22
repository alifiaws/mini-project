class ATMCard:
	def __init__(self, defaultPin, defaultBalance):
		self.defaultPin = defaultPin
		self.defaultBalance = defaultBalance

	def getPin(self):
		return self.defaultPin

	def getBalance(self):
		return self.defaultBalance
