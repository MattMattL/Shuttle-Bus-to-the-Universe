import math

from src.utilities.deprecated_marker import Deprecated
from src.graphics.line_elements import LineElements

class GraphicsObject:

	_DEGREE_TO_RADIAN_FACTOR = math.pi / 180

	_allLineElements: [LineElements] = []
	_centerX = 0
	_centerY = 0

	_currentLineElements: LineElements = None
	_currentAngle = 0

	def __init__(self):
		self._allLineElements = []

	# set graphics properties and draw
	def newLineElements(self):
		self._currentLineElements = LineElements()
		return self

	def setColor(self, color: str):
		self._currentLineElements.setColor(color)
		return self

	def setThickness(self, thickness):
		self._currentLineElements.setThickness(thickness)
		return self

	def startFrom(self, x, y):
		self._currentLineElements.addLineElement(x, y)
		return self

	def setAngle(self, relative=None, absolute=None): # in degree angles
		if relative is not None:
			self._currentAngle += relative * self._DEGREE_TO_RADIAN_FACTOR
		elif absolute is not None:
			self._currentAngle = absolute * self._DEGREE_TO_RADIAN_FACTOR
		else:
			self._currentAngle = 0

		return self

	def moveBy(self, length):
		x0, y0 = self._currentLineElements.getLastCoordinates()

		x = x0 + length * math.cos(self._currentAngle)
		y = y0 + length * math.sin(self._currentAngle)

		self._currentLineElements.addLineElement(x, y)

		return self

	def endElements(self):
		self._allLineElements.append(self._currentLineElements)
		return self

	# optional
	def updateCenter(self):
		allX, allY = [], []

		for element in self._allLineElements:
			allX += element.getXCoordinates()
			allY += element.getYCoordinates()

		self._centerX = (min(allX) + max(allX)) / 2
		self._centerY = (min(allY) + max(allY)) / 2

		return self

	# translations
	def rotate(self, degree):
		for element in self._allLineElements:
			element.rotate(self._centerX, self._centerY, degree * self._DEGREE_TO_RADIAN_FACTOR)

		return self

	def translate(self, dx, dy):
		for element in self._allLineElements:
			element.translate(dx, dy)

		return self

	# getters
	def getAllLineElements(self):
		return self._allLineElements

	def getCentre(self):
		return self._centerX, self._centerY
