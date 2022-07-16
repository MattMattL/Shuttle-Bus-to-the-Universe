import math

class LineElements:

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

	# translations
	def rotate(self, centerX, centerY, radian):
		for i in range(len(self._xCoordinates)):
			newX = math.cos(radian) * (self._xCoordinates[i] - centerX) \
					- math.sin(radian) * (self._yCoordinates[i] - centerY)

			newY = math.sin(radian) * (self._xCoordinates[i] - centerX) \
					+ math.cos(radian) * (self._yCoordinates[i] - centerY)

			self._xCoordinates[i] = newX + centerX
			self._yCoordinates[i] = newY + centerY

	def translate(self, dx, dy):
		for i in range(len(self._xCoordinates)):
			self._xCoordinates[i] += dx
			self._yCoordinates[i] += dy