import matplotlib.pyplot as plt

class LineElements(object):

	_xCoordinates = []
	_yCoordinates = []

	_color = 'black'
	_thickness = 1

	def __init__(self):
		self._xCoordinates = []
		self._yCoordinates = []
		pass

	# setters
	def setColor(self, colorIn: str):
		self._color = colorIn

	def setThickness(self, thicknessIn):
		self._thickness = thicknessIn

	def addLineElement(self, x, y):
		self._xCoordinates.append(x)
		self._yCoordinates.append(y)

	# getters
	def getColor(self):
		return self._color

	def getThickness(self):
		return self._thickness

	def getXCoordinates(self):
		return self._xCoordinates

	def getYCoordinates(self):
		return self._yCoordinates

	def getLastCoordinates(self):
		return self._xCoordinates[-1], self._yCoordinates[-1]

	def getLineElements(self):
		return self._xCoordinates, self._yCoordinates